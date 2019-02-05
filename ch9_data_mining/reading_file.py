from collections import Counter
import re

# 'r'는 read-only를 의미함
file_for_reading = open('reading_file.txt', 'r')

# 'w'는 write를 의미함 (해당 파일이 이미 존재한다면, 기존 파일을 제거함)
file_for_writing = open('writing_file.txt', 'w')

# 'a'는 append를 의미함 (파일의 맨 끝에 덧붙임)
file_for_appending = open('appending_file.txt', 'a')

# 작업이 끝났다면 파일을 닫음
file_for_writing.close()

# 파일을 저절로 닫아주는 with
with open('filename', 'r') as f:
    data = function_that_gets_data_from(f)
# 이 시점부터는 f가 이미 종료되었기 때문에 f를 다시 사용할 수 없음

# 파일 전체가 필요할 때
starts_with_hash = 0
with open('input.txt', 'r') as f:
    for line in f:               # file의 각 줄을 살펴봄
        if re.match("^#", line):    # regex를 사용해서 줄이 #로 시작하는지 확인
            starts_with_hash += 1   # #로 시작한다면 1을 추가

# example
def get_domain(email_address):
    """
        '@' 기준으로 주소를 자르고 마지막 부분을 반환
    """
    return email_address.lower().split("@")[-1]

with open('email_addresses.txt', 'r') as f:
    domain_counts = Counter(get_domain(line.strip())
                            for line in f
                            if "@" in line)
