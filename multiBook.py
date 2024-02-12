import re
import requests
from datetime import datetime, timedelta

def checkInputValid(vaild):
    """ 입력값의 형식 유효성 검사 """
    if not vaild:
        return -1
    
    global startDate
    global endDate
    global startTime
    global endTime
    datePattern = r'^\d{4}-\d{2}-\d{2}$'
    dateValid = True if re.match(datePattern, startDate) and re.match(datePattern, endDate) else False
    timePattern = r'^(9|1[0-8])$'
    timeValid = True if re.match(timePattern, startTime) and re.match(timePattern, endTime) else False
    
    inputVaild = True if dateValid and timeValid else False
    if not inputVaild:
        return -2
    
    # 입력 시간 포멧에 맞게 수정
    if len(startTime) == 1 and startTime.isdigit():
        startTime = '0' + startTime
    if len(endTime) == 1 and endTime.isdigit():
        endTime = '0' + endTime
    
    startDateObj = datetime.strptime(startDate, '%Y-%m-%d')
    endDateObj = datetime.strptime(endDate, '%Y-%m-%d')
    startMilliSec = startDateObj.timestamp()
    endMilliSec = endDateObj.timestamp()
    
    dateRangeVaild = True if startMilliSec <= endMilliSec else False

    if dateRangeVaild:
        return 1
    else:
        return 0

def booking(date, cookie, book_reason):
    """ 하이웍스 1번 회의실 예약 API 호출 """
    global startTime
    global endTime
    url = 'https://booking.office.hiworks.com/softcamp.co.kr/booking/bookingAjax/addBooking'
    
    headers = {
        'Cookie': cookie,
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    data = {
        'category_no': '868',
        'resource_no[]': '2341', # 1번 회의실
        'date': date,
        'booking_reason': book_reason,
        'start_time': f'{date} {startTime}:00:00',
        'end_time': f'{date} {endTime}:00:00'
    }
    print("data : ", data)
    response = requests.post(url, headers=headers, data=data)
    print("Response : ", response, response.text)



startDate = input("예약 시작 날짜를 입력하세요 [202x-0x-0x] : ")
endDate = input("예약 종료 날짜를 입력하세요 [202x-0x-0x] : ")
startTime = input("예약 시작 시간을 입력하세요 [9 ~ 18] : ")
endTime = input("예약 종료 시간을 입력하세요 [9 ~ 18] : ")

dataVaild = True if startDate and endDate and startTime and endTime else False

inputValid = checkInputValid(dataVaild)

if inputValid == 1:
    print(f"예약 기간과 시간은 다음과 같습니다. \n{startDate} ~ {endDate} \n{startTime}:00 ~ {endTime}:00")
    cookie = input("하이웍스 로그인 후 취득되는 쿠키를 입력하세요 : ")
    book_reason = input("예약 사용 용도를 입력하세요. [CloudR&D부 Daily Scrum] : ")
    
    endDateObj = datetime.strptime(endDate, '%Y-%m-%d')
    currentDateObj = datetime.strptime(startDate, '%Y-%m-%d')
    date = startDate
    # 다중 예약을 위한 반복문
    while True:
        # 요일 확인 토/일은 제외
        if currentDateObj.weekday() > 4:
            currentDateObj = currentDateObj + timedelta(days=1)
            continue
        # endDate를 넘기면 중단
        if currentDateObj.timestamp() > endDateObj.timestamp():
            break
        
        date = currentDateObj.strftime("%Y-%m-%d")
        print(f"요청 날짜 : {date}")

        booking(date, cookie, book_reason)
        currentDateObj = currentDateObj + timedelta(days=1)
elif inputValid == 0:
    print("종료 시간이 시작 시간보다 이전 날짜입니다.")
elif inputValid == -1:
    print("필수 값이 입력되지 않았습니다.")
elif inputValid == -2:
    print("입력 데이터 형식이 유효하지 않습니다.")
else:
    print("Error")