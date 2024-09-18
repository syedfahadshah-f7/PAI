import re
txt = "12/09/2023 2023-09-12 Sep 12,2023."
p1 = r'\b(\d{1,2}/\d{1,2}/\d{4}|\d{4}-\d{1,2}-\d{1,2}|[A-Z|a-z]{3,}\s\d{1,2},\d{4})\b'

ans = re.findall(p1,txt)

for i in ans:
    print(i)