import requests  # http 요청 라이브러리
from datetime import datetime
from email.utils import parsedate_to_datetime
import pytz

start_time = datetime.now()
url = "https://for-s.seoultech.ac.kr/view/login.jsp"  # 실제 수강신청 사이트 URL 입력
response = requests.get(url)
server_date = response.headers.get("Date")
server_time_utc = parsedate_to_datetime(server_date)

# UTC → 한국 시간(KST) 변환
kst = pytz.timezone("Asia/Seoul")
server_time_kst = server_time_utc.astimezone(kst)
finish_time = datetime.now()
print("서버 -> 내pc 시간:", server_time_kst - server_time_utc)
print("서버 시간:", server_time_kst)
print("서버 요청-응답 걸리는 시간:", finish_time - start_time)

# 어떤 방법으로 문제를 해결할 것인가
# 최대한 시간 보정, 네트워크 지연 시간 + ms 단위까지
# 여러번 요청하는 툴 만들기(시스템별) : 최댓값-평균값 확인 후 요청만하면 되므로 평균값 활용