import re
import os
import json
from datetime import datetime, timedelta

import global_resource
import api_module

def input_room_number():
    """ 예약 회의실 입력 """
    with open('config.json', 'r', encoding='utf-8') as file:
        config = json.load(file)
    room_infos = config.get('resource_no', {})
    codes = list(map(lambda x: x['code'], room_infos))
    for data in room_infos:
        print(f"{data['name']} Number: {data['code']}")
    room_no = input("예약할 회의실 번호를 입력하세요 : ")
    if room_no not in codes:
        print("존재하지 않는 회의실 번호입니다.")
        input_room_number()
    else:
        resource_info = next(filter(lambda x: x['code'] == room_no, room_infos), None)
        resource_no = resource_info['resource_no']
        global_resource.set_resource_no(resource_no)

def input_book_date():
    """ 예약 날짜 입력 """
    start_date = input("예약 시작 날짜를 입력하세요 [202x-0x-0x] : ")
    global_resource.set_start_date(start_date)
    end_date = input("예약 종료 날짜를 입력하세요 [202x-0x-0x] : ")
    global_resource.set_end_date(end_date)
    start_time = input("예약 시작 시간을 입력하세요 [9 ~ 18] : ")
    global_resource.set_start_time(start_time)
    end_time = input("예약 종료 시간을 입력하세요 [9 ~ 18] : ")
    global_resource.set_end_time(end_time)

    inputValid = check_input_valid()
    if inputValid == False:
        input_book_date()

def check_input_valid():
    """ 입력값의 형식 유효성 검사 """
    start_date = global_resource.start_date
    end_date = global_resource.end_date
    start_time = global_resource.start_time
    end_time = global_resource.end_time
        
    valid = get_input_valid()

    if not valid:
        print("필수 값이 입력되지 않았습니다.")
        return False
    
    date_pattern = r'^\d{4}-\d{2}-\d{2}$'
    date_valid = True if re.match(date_pattern, start_date) and re.match(date_pattern, end_date) else False
    time_pattern = r'^(9|1[0-8])$'
    time_valid = True if re.match(time_pattern, start_time) and re.match(time_pattern, end_time) else False
    
    input_valid = True if date_valid and time_valid else False
    if not input_valid:
        print("입력 데이터 형식이 유효하지 않습니다.")
        return False
    
    # 입력 시간 포멧에 맞게 수정
    if len(start_time) == 1 and start_time.isdigit():
        global_resource.set_start_time('0' + start_time)
    if len(end_time) == 1 and end_time.isdigit():
        global_resource.set_end_time('0' + end_time)
    
    start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
    end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')
    start_milli_sec = start_date_obj.timestamp()
    end_milli_sec = end_date_obj.timestamp()
    
    date_range_valid = True if start_milli_sec <= end_milli_sec else False

    if date_range_valid:
        return True
    else:
        print("종료 시간이 시작 시간보다 이전 날짜입니다.")
        return False

def get_input_valid():
    start_date = global_resource.start_date
    end_date = global_resource.end_date
    start_time = global_resource.start_time
    end_time = global_resource.end_time
        
    return True if start_date and end_date and start_time and end_time else False 

def multi_book():
    """ 다중 예약 호출 반복문 """
    start_date = global_resource.start_date
    end_date = global_resource.end_date
    start_time = global_resource.start_time
    end_time = global_resource.end_time
    
    print(f"예약 기간과 시간은 다음과 같습니다. \n{start_date} ~ {end_date} \n{start_time}:00 ~ {end_time}:00")
    book_reason = input("예약 사용 용도를 입력하세요. [CloudR&D부 Daily Scrum] : ")
    global_resource.set_book_reason(book_reason)

    end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')
    current_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
    # 다중 예약을 위한 반복문
    while True:
        # 요일 확인 토/일은 제외
        if current_date_obj.weekday() > 4:
            current_date_obj = current_date_obj + timedelta(days=1)
            continue
        # end_date를 넘기면 중단
        if current_date_obj.timestamp() > end_date_obj.timestamp():
            break
        
        current_date = current_date_obj.strftime("%Y-%m-%d")
        print(f"요청 날짜 : {current_date}")

        api_module.booking(current_date)
        current_date_obj = current_date_obj + timedelta(days=1)

