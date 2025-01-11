from requests.cookies import RequestsCookieJar

global cookie
global book_reason
global start_date
global end_date
global start_time
global end_time
global resource_no

def set_cookie(param: RequestsCookieJar):
    global cookie
    cookie = param

def set_book_reason(param: str):
    global book_reason
    book_reason = param

def set_start_date(param: str):
    global start_date
    start_date = param

def set_end_date(param: str):
    global end_date
    end_date = param

def set_start_time(param: str):
    global start_time
    start_time = param

def set_end_time(param: str):
    global end_time
    end_time = param
   
def set_resource_no(param: str):
    global resource_no
    resource_no = param
