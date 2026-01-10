def zero_div_error(num):
        try:
            z= 10/num
            print(num)
        except ZeroDivisionError as zeroerr:
            print(zeroerr)

#zero_div_error(0)
#_________________________
#age cannoot be negative ,calaucate ratire ment age 

def get_age(age_val):
    if  age_val<=0:
        raise ValueError("value cannot be 0 or nrgative")
    ret_age = 60- age_val
    return ret_age

# try:
#     print(get_age(0))
# except ValueError as valerr:
#      print(f'error:{valerr}')

#____________________________________________
'''You have a function that checks passwords. The rule is that the password must be at least 10 characters long.
 If the password is too short, you must manually stop the function and signal a ValueError'''   

def check_pass(passwd):
    if len(passwd)<10:
        raise ValueError("password is to short")
    return passwd
     
# try:
#     print(check_pass('kavyabairgkavya'))
# except ValueError as verr:
#      print(f'error:{verr}')
#____________________________________________________________
'''You are trying to convert user input to an integer. If the input is invalid (e.g., "hello"), 
a ValueError will be raised. You want to print a success message only if no error occurs.'''

def chek_int(val):
    try:
        int_val =int(val)
        print(f"value is {int_val}")
    except ValueError as verr:
        print(verr)
    else:
        print("sucessful, given value is int")
#chek_int('hello')
#__________________________________________________________________________________
#custom exception
class insuffientFund(Exception):
    def __init__(self,amount,tt_am):
        msg = "it has insuffient fund "
        super().__init__(msg)


def withdaw(amo,bal):
    if amo>bal:
        raise insuffientFund(amo,bal)
    return bal - amo

# try:
#     print(withdaw(150,100))
# except insuffientFund as err:
#     print(err)

#---------------------------------------------------------------------------
'''You have performed an API call that returns the following JSON response representing a warehouse inventory. You need to validate the data integrity.'''
'''Task: Write a function/script that parses this data (assume it is passed as a list/array of objects) and iterates through the items. The script must print an error log to the console for any item that violates the following rules:
Price cannot be negative.
Product Name cannot be empty.
Stock cannot be null/missing.
Note: Ensure your code handles potential exceptions (e.g., missing keys).'''

# def validate_data(ls):
#     for dict_ in ls:
#         price = dict_.get('price',0)
#         pd_name = dict_.get('name','')
#         st = dict_.get('stock',None)
#         if price<0:
#             print("value cannot be negative")
#         if pd_name =='':
#             print('pd_name cannot be missing')
#         if st == None:
#             print("it cannot be none")

def validate_date(ls):
    try:
        for dict_ in ls:
            price = dict_.get('price')
            pd_name = dict_.get('name')
            st = dict_.get('stock')
            if price<0:
                print("value cannot be negative")
            if pd_name =='':
                print('pd_name cannot be missing')
            if st == None:
                print("it cannot be none")
    except KeyError as ker:
        print(ker)
        

ls = [
  {"id": 101, "name": "Wireless Mouse", "price": 25.50, "stock": 50},
  {"id": 102, "name": "", "price": 150.00, "stock": 10},
  {"id": 103, "name": "HDMI Cable", "price": -5.00, "stock": 100},
  {"id": 104, "name": "Monitor", "price": 200.00, "stock": None}
]
#validate_data(ls)
#----------------------------------------------------------------------------
'''program attempts to read a configuration file (config.txt). This operation can fail if:
The file doesn't exist (FileNotFoundError).
The program lacks permission to read it (PermissionError).
You must ensure that if the file is opened, it is closed, regardless of any error encountered during reading or processing'''

def check_file():
    try:
        with open('sample.txt','r')as f1:
            file_content = f1.read()
            print('file is suceddfully reading')
    except FileNotFoundError as ferr:
        print(ferr)
    except PermissionError as perr:
        print(perr)
    
    finally:
        f1.close()
        print('finally excuted sucessfully')
# check_file()
#___________________________________________________________________________________________
user_data = {
    1: {"name": "Charlie", "email": "charlie@example.com"},
    2: {"name": "Dana", "phone": "555-1234"}, # Missing 'email' key
    3: {"name": "Eve", "email": "eve@example.com"}
}
#1.missing uid we have to handle 
#uid is there but missing email keyword we have to handle 
def get_validate_data(user_data,uid):
    try:
        email_ = user_data[uid]['email']
        print("suceful this is the mail id for givem uid")
    except KeyError:
        if not user_data.get(uid):
            print('uid key is missing')
        else:
            print('email is missing')
    except Exception as e:
        print(e)

get_validate_data(user_data,2)

#____________________________________________________________-
'''the Scenario A function fetch_user_data() simulates querying a database. Since the database is remote, the connection might drop, 
which is usually signaled by a low-level error (we'll simulate this with a TimeoutError). 
Your system must retry the connection exactly once before giving up.'''

# slove this problem 




    



          
     
    
    

