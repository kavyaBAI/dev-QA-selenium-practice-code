import random 
import time

#we use random here to test the flaky test,rusing radom we will get the unpreditable number,just real world to mimic same we use random
#random will genrate the float value from 0.0 to 1,0
def get_user_data(uid):
    time.sleep(0.1)
    print(random.random())
    if random.random() < 0.5:
        #transient error to use the retry 
        raise IOError("connection time out ,rettry again")
    return {"user_id":uid,"user_name":f"username_{uid}","status":"active"}


# print(get_user_data(3))
