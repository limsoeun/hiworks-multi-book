import requests

import global_resource

def login():
    """ 로그인 API 호출 """
    url = 'https://auth-api.office.hiworks.com/office-web/login'
    hiworks_id = input('Hiworks ID를 입력하세요 : ')
    hiworks_pw = input('Hiworks 비밀번호를 입력하세요 : ')
    
    headers = {
        'Accept': 'application/json'
    }
    data = {
        "id": hiworks_id,
        "password": hiworks_pw,
        "ip_security_level": "1"
    }
    response = requests.post(url, headers=headers, json=data)
    print("Response : ", response, response.text)
    if response.status_code == 200:
        global_resource.set_cookie(response.cookies)
        print('로그인 완료')
        return True
    else:
        print('로그인 실패')
        return False

def booking(date):
    """ 하이웍스 1번 회의실 예약 API 호출 """
    cookie = global_resource.cookie
    book_reason = global_resource.book_reason
    start_time = global_resource.start_time
    end_time = global_resource.end_time
    resource_no = global_resource.resource_no

    url = 'https://booking.office.hiworks.com/softcamp.co.kr/booking/bookingAjax/addBooking'
    
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    data = {
        'category_no': '868',
        'resource_no[]': resource_no, #'2341', # 1번 회의실
        'date': date,
        'booking_reason': book_reason,
        'start_time': f'{date} {start_time}:00:00',
        'end_time': f'{date} {end_time}:00:00'
    }
    response = requests.post(url, headers=headers, data=data, cookies=cookie)
    print("Response : ", response, response.text)
