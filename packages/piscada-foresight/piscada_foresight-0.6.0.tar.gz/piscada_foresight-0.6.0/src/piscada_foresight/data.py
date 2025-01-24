"""Access to Foresight timeseries data."""

import re
from datetime import datetime, timezone
from json import loads
from typing import Optional
from uuid import UUID

import jinja2
from gql import Client, gql
from pandas import DataFrame, concat, to_datetime


def get_value(
    client: Client, entity_id: UUID, moment: Optional[datetime] = None
) -> float:
    """Retrieve the latest value of a `foresight:Datapoint` entity before a point in time (default=now).

    Parameters
    ----------
    client : Client
        The GQL client to use.
    entity_id : str
        The ID of the entity to retrieve the value for.
    moment : Optional[datetime], optional
        The point in time to retrieve a value for, by default `datetime.now(tz=timezone.utc)`.

    Returns
    -------
    float
        The numeric value at the specified moment.

    Raises
    ------
    RuntimeError
        When the value cannot be retrieved from the server.
    RuntimeError
        When the retrieved value cannot be converted to float.

    """
    if not moment:
        moment = datetime.now(tz=timezone.utc)
    query = gql(
        """
    query value($entityId: ID!, $eventTime: DateTime) {
        entity(id: $entityId) {
            trait(id: "foresight:Datapoint") {
                quantity(key: "Value") {
                    value(eventTime: $eventTime) {
                        value
                    }
                }
            }
        }
    }
    """
    )
    variables = {"entityId": entity_id, "eventTime": moment.isoformat()}
    response = client.execute(query, variables)
    try:
        return float(response["entity"]["trait"]["quantity"]["value"]["value"])
    except KeyError:
        raise RuntimeError("Cloud not retrieve value.")
    except ValueError:
        raise RuntimeError(
            f"Could not parse value {response['entity']['trait']['quantity']['value']['value']}"
        )


def get_values(
    client: Client,
    entity_ids: list[str],
    start: datetime,
    end: Optional[datetime] = None,
) -> DataFrame:
    """Retrieve values of `foresight:Datapoint` entities for a time range.

    The most recent value before 'start' is included. 'end' defaults to 'now'.

    Parameters
    ----------
    client : Client
        The GQL client to use.
    entity_ids : list[str]
        The IDs of the entities to retrieve values for.
    start : datetime
        The starting point in time from which to receive values. Must include timezone info.
        The most recent value before this point is also included in the response.
    end : Optional[datetime], optional
        The end point in time until which to receive values. Must include timezone info. By default `datetime.now(tz=timezone.utc)`.

    Returns
    -------
    DataFrame
        A Pandas DataFrame containing the timestamped values within the specified range.

    Raises
    ------
    ValueError
        When start or end datetimes are not timezone-aware.
    RuntimeError
        When values cannot be retrieved from the server.
    """
    if not end:
        end = datetime.now(tz=timezone.utc)
    if start.tzinfo is None or start.tzinfo.utcoffset(start) is None:
        raise ValueError("The start parameter must be timezone aware.")
    if end.tzinfo is None or end.tzinfo.utcoffset(end) is None:
        raise ValueError("The end parameter must be timezone aware.")
    if start > end:
        raise ValueError(
            "The 'start' datetime cannot be later than the 'end' datetime."
        )

    query_template = """
    query value(
        {% for variable_name in variable_names -%}
        ${{variable_name}}: ID!
        {% endfor -%}
        $startEventTime: DateTime!
        $endEventTime: DateTime!
    ) {
        {% for variable_name in variable_names -%}
        {{variable_name}}: entity(id: ${{variable_name}}) {
            name
            trait(id: "foresight:Datapoint") {
                quantity(key: "Value") {
                    values(startEventTime: $startEventTime, endEventTime: $endEventTime) {
                        eventTime
                        value
                    }
                }
            }
        }
        {% endfor -%}
    }
    """

    entity_variables = {
        f"entityId_{i}": entity_id for i, entity_id in enumerate(entity_ids)
    }
    environment = jinja2.Environment(autoescape=jinja2.select_autoescape())
    template = environment.from_string(query_template)
    query = template.render(variable_names=entity_variables.keys())

    variables = {
        **entity_variables,
        "startEventTime": start.isoformat(),
        "endEventTime": end.isoformat(),
    }

    response = client.execute(gql(query), variables)
    series = []
    for variable_name, entity_id in entity_variables.items():
        try:
            values = response[variable_name]["trait"]["quantity"]["values"]
            name = response[variable_name]["name"]
            frame = DataFrame(values).set_index("eventTime")["value"]
            frame.index = to_datetime(frame.index, format="ISO8601")
            frame = frame.astype(float)
            frame.name = name
            series.append(frame)
        except KeyError as exc:
            raise RuntimeError(
                f"Cloud not retrieve values for entity {entity_id} in time range {start} - {end}."
            ) from exc
        except TypeError as exc:
            raise RuntimeError(f"Cloud not find entity {entity_id}.") from exc
    df = concat(series, axis=1)
    df = df.ffill()
    return df


def get_all_values(text: str) -> list[DataFrame]:
    """Extract all pairs of id, name, and values from a graph query and return them as a list of DataFrames.

    The query needs to be of the form:

    ```
    id
    name
    trait(id: "foresight:Datapoint") {
        quantity(key: "Value") {
            values(startEventTime: "2024-10-01T00:00:00Z", endEventTime: "2024-10-02T00:00:00Z") {
                eventTime
                value
            }
        }
    }
    ```

    Parameters
    ----------
    text : str
        The string form of the query, usually `str(fs_client.execute(query))`.
        Must contain id, name, and datapoint values in the expected format.

    Returns
    -------
    list[DataFrame]
        A list of DataFrames, one for each id-name-values combination found in the string.
        Each DataFrame is indexed by timestamp and contains a value column named "{name}|{id}".

    """
    values_regex = re.compile(
        r"'id'\:\s*'([\:\w\s\-_]*?)',\s*'name'\:\s*'([\w\s\-_]*?)',\s*'trait':\s*{'quantity'\:\s*\{'values'\:\s*\[([\{'\w\:\-\s\.\},]*)"
    )
    dfs = []
    for m in values_regex.findall(text):
        eid = m[0].split(":")[-1]
        name = m[1]
        values = f"[{m[2]}]".replace("'", '"')
        df = DataFrame(
            [
                {"ts": v["eventTime"], f"{name}|{eid}": float(v["value"])}
                for v in loads(values)
            ]
        )
        df = df.set_index("ts")
        df.index = to_datetime(df.index, format="ISO8601")
        dfs.append(df)
    return dfs
