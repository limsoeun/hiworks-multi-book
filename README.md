# Hiworks multi book
지정한 기간의 월~금요일에 [같은 회의실/같은 시간/같은 회의 예약 사유]로 예약해줍니다.

## Reason for production
매일 같은 시간 회의를 진행하면서 같은 회의실을 하루씩 반복 예약하는 번거로움을 해결하기 위해 만들게 되었습니다.


## Usage

```shell
$ py ./multiBook.py
예약 시작 날짜를 입력하세요 [202x-0x-0x] : 2024-04-11
예약 종료 날짜를 입력하세요 [202x-0x-0x] : 2024-04-30
예약 시작 시간을 입력하세요 [9 ~ 18] : 9
예약 종료 시간을 입력하세요 [9 ~ 18] : 10
예약 기간과 시간은 다음과 같습니다. 
2024-04-11 ~ 2024-04-30
09:00 ~ 10:00
하이웍스 로그인 후 취득되는 쿠키를 입력하세요 : h_idremember=false; h_officeid=softcamp.co.kr; PHPSESSID=....
예약 사용 용도를 입력하세요. [CloudR&D부 Daily Scrum] : CloudR&D부 Daily Scrum
요청 날짜 : 2024-04-11
data :  {'category_no': '868', 'resource_no[]': '2341', 'date': '2024-04-11', 'booking_reason': 'CloudR&D부 Daily Scrum', 'start_time': '2024-04-11 09:00:00', 'end_time': '2024-04-11 10:00:00'}
Response :  <Response [200]> {"resultCode":"SUCCESS","result":null,"message":null,"layerID":null}
...
```

## Build

### install dependencies

```
pip install requests 
```

### Compiles for development

```
py ./multiBook.py
```
