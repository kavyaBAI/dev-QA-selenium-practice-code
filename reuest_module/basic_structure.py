import requests
#below is input
response = requests.post(
    url="https://api.example.com/v1/login",
    json={"username": "admin", "password": "123"},
    headers={"Content-Type": "application/json"}
)
#reposne object contain all the info,we will check the stttus code based on theat we will fetch the data
#this is the response 
print(response.status_code)  #status 200 
print(response.json())       # The data returned by server,it will coberst raw json to dictionary 