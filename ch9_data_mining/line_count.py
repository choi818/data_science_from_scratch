import sys

count = 0
for line in sys.stdin:
    count += 1

# 출력값은 sys.stdout으로 보낸다
print(count)

# 커맨드라인에서 적용
# type SomeFile.txt | python egrep.py "[0-9]" | python line_count.py
