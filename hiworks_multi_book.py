import api_module
import func_module

# 로그인
login_result = api_module.login()

# 예약 날짜 입력
func_module.input_book_date()

# 입력 데이터 유효성 검사
inputValid = func_module.check_input_valid()

if inputValid == True:
    func_module.multi_book()
