import re

pattern = r"(apple)\Z"

match = re.search(pattern, "apple pie apple")
if match:
    print("Yes")