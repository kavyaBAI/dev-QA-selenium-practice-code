import pytest
from apis import  api_retry

print("hello")
@pytest.mark.flaky(reruns=3,reruns_delay=1)
def test_get_user_data():
    uid = 4
    try:
        data= api_retry.get_user_data(uid)
        print("data")
        assert data.get("user_id") == uid
        assert data.get("status") =="active"
        print("data fetch is correct and sussful")
    except IOError as e:
        print(f"fetching data  failed due to tempory error or transient error,{e}")
        #the raise keyword inside except tell pytest function is failed trigger again 
        raise




