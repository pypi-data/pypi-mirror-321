from kaizen_cyber_lib.ddos_tools import send_http_requests

def test_send_http_requests(mocker):
    mock_get = mocker.patch("requests.get")
    send_http_requests("http://example.com", 5)
    assert mock_get.call_count == 5
