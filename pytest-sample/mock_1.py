import requests
import requests_mock

def login_to_portal(username, password):
    url = "https://api.secureapp.com/v1/login"
    payload = {"user": username, "pass": password}
    response = requests.post(url, json=payload)
    return response.json()

def test_successful_login():
    with requests_mock.Mocker() as m:
        m.post("https://api.secureapp.com/v1/login", 
               json={"token": "SECRET_JWT_123", "status": "authenticated"}, 
               status_code=200)
        
        result = login_to_portal("senior_eng", "password123")
        assert result["token"] == "SECRET_JWT_123"
        assert result["user"] == "senior_eng"
        