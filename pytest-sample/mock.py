import pytest
import requests
import requests_mock

# real application code
def check_server_status(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False


#mock-fixture
@pytest.fixture
def api_mocker():
    with requests_mock.Mocker() as m:
        yield m

def test_check_status_success(api_mocker):
    target_url = "https://myserver.com/health"
    api_mocker.get(target_url, status_code=200)
    result = check_server_status(target_url) #when the mock see the request.get ,python stop calling real request i mock the request_mock
    print(result,"resssssssssssssssssssssss")
    assert result is True
    assert api_mocker.called  

def test_check_status_failure(api_mocker):
    target_url = "https://myserver.com/health"
    api_mocker.get(target_url, status_code=500) 
    result = check_server_status(target_url)
    print(result,"resssssssssssssssssssssss11111111111111111111111!!!!!!!")
    assert result is False

