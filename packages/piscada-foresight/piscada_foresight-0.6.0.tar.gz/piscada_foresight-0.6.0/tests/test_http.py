from piscada_foresight import http


def test_get_state_file():
    state_file = http._get_state_file("test")
    assert str(state_file).endswith("/.test_state")
    assert str(state_file).startswith("/")
