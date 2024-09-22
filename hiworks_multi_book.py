import sys
import api_module
import func_module

# 로그인
login_result = api_module.login()

if login_result == False:
    sys.exit()

# 예약 대상 회의실 선택
func_module.input_room_number()

# 예약 날짜 입력
func_module.input_book_date()

# 예약
func_module.multi_book()
