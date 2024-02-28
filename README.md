# Hiworks multi book

지정한 기간의 월~금요일에 [같은 회의실/같은 시간/같은 회의 예약 사유]로 예약해줍니다.

## Reason for production

매일 같은 시간 회의를 진행하면서 같은 회의실을 하루씩 반복 예약하는 번거로움을 해결하기 위해 만들게 되었습니다.

<br/>

## Get Start

##### Install dependencies

```
pip install requests 
```

## Execute

##### install pyinstaller

```
pip install pyinstaller
```

##### do build

```
pyinstaller hiworks_multi_book.py
```

##### artifacts path

```
<project dir>/dist
```

##### execution

```shell
Hiworks ID를 입력하세요 : ididid@hiworks.com
Hiworks 비밀번호를 입력하세요 : pwpwpw
Response :  <Response [200]> {"data":{"office_main":""}}
로그인 완료
예약 시작 날짜를 입력하세요 [202x-0x-0x] : 2024-05-07
예약 종료 날짜를 입력하세요 [202x-0x-0x] : 2024-05-08
예약 시작 시간을 입력하세요 [9 ~ 18] : 9
예약 종료 시간을 입력하세요 [9 ~ 18] : 10
예약 기간과 시간은 다음과 같습니다. 
2024-05-07 ~ 2024-05-08
09:00 ~ 10:00
예약 사용 용도를 입력하세요. [Daily Scrum] : Daily Scrum
요청 날짜 : 2024-05-07
Response :  <Response [200]> {"resultCode":"SUCCESS","result":null,"message":null,"layerID":null}
요청 날짜 : 2024-05-08
Response :  <Response [200]> {"resultCode":"SUCCESS","result":null,"message":null,"layerID":null}
...
```
