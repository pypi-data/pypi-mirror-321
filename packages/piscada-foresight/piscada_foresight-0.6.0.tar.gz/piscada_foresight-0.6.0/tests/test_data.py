from datetime import datetime, timezone

import pandas as pd
import pytest

from piscada_foresight.data import get_values


@pytest.fixture
def get_values_response():
    return {
        "entityId_0": {
            "name": "360001 Temperature",
            "trait": {
                "quantity": {
                    "values": [
                        {"eventTime": "2025-01-14T09:59:59.786Z", "value": "19.5"},
                        {"eventTime": "2025-01-14T10:00:03.743Z", "value": "19.559999"},
                        {"eventTime": "2025-01-14T10:00:11.683Z", "value": "19.5"},
                        {"eventTime": "2025-01-14T10:00:15.622Z", "value": "19.559999"},
                        {"eventTime": "2025-01-14T10:00:36.901Z", "value": "19.5"},
                        {"eventTime": "2025-01-14T10:00:44.77Z", "value": "19.559999"},
                        {"eventTime": "2025-01-14T10:00:48.708Z", "value": "19.5"},
                    ]
                }
            },
        },
        "entityId_1": {
            "name": "360001 Temperature Setpoint",
            "trait": {
                "quantity": {
                    "values": [
                        {"eventTime": "2025-01-14T09:32:32.176Z", "value": "19.5"}
                    ]
                }
            },
        },
    }


@pytest.fixture
def no_values_response(get_values_response):
    response = get_values_response
    response["entityId_0"]["trait"]["quantity"]["values"] = []
    response["entityId_1"]["trait"]["quantity"]["values"] = []
    return response


def test_get_values_success(mocker, get_values_response):
    mock_client = mocker.Mock()
    mock_client.execute.return_value = get_values_response

    df = get_values(
        mock_client,
        entity_ids=[
            "brick:Supply_Air_Temperature_Sensor:00000000-0000-0000-0000-000000000001",
            "brick:Effective_Supply_Air_Temperature_Setpoint:00000000-0000-0000-0000-000000000002",
        ],
        start=datetime.now(tz=timezone.utc),
    )
    assert len(df) == 8  # noqa: PLR2004
    assert pd.isna(df["360001 Temperature"].iloc[0])


def test_get_values_missing_values(mocker, no_values_response):
    # No data for the tags at the specified time range
    mock_client = mocker.Mock()
    mock_client.execute.return_value = no_values_response
    with pytest.raises(RuntimeError):
        get_values(
            mock_client,
            entity_ids=[
                "brick:Supply_Air_Temperature_Sensor:00000000-0000-0000-0000-000000000001",
                "brick:Effective_Supply_Air_Temperature_Setpoint:00000000-0000-0000-0000-000000000002",
            ],
            start=datetime(1993, 2, 12, tzinfo=timezone.utc),
            end=datetime(1993, 2, 13, tzinfo=timezone.utc),
        )


def test_get_values_start_later_than_end(mocker):
    with pytest.raises(
        ValueError,
        match="The 'start' datetime cannot be later than the 'end' datetime.",
    ):
        get_values(
            client=mocker.Mock(),
            entity_ids=["entity1", "entity2"],
            start=datetime(2023, 2, 1, tzinfo=timezone.utc),
            end=datetime(2023, 1, 31, tzinfo=timezone.utc),
        )


def test_get_values_start_or_end_not_timezone_aware(mocker):
    with pytest.raises(ValueError, match="The start parameter must be timezone aware."):
        get_values(
            client=mocker.Mock(),
            entity_ids=["entity1", "entity2"],
            start=datetime(2023, 2, 1),
            end=datetime(2023, 1, 31, tzinfo=timezone.utc),
        )
        get_values(
            client=mocker.Mock(),
            entity_ids=["entity1", "entity2"],
            start=datetime(2023, 2, 1),
            end=datetime(2023, 1, 31),
        )
    with pytest.raises(ValueError, match="The end parameter must be timezone aware."):
        get_values(
            client=mocker.Mock(),
            entity_ids=["entity1", "entity2"],
            start=datetime(2023, 2, 1, tzinfo=timezone.utc),
            end=datetime(2023, 1, 31),
        )
