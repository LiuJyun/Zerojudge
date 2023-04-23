from datetime import datetime

# 讀取測試數量
T = int(input())

# 逐一處理每個測試案例
for i in range(T):
    # 讀取今天日期和出生日期
    input()
    today = datetime.strptime(input().strip(), "%d/%m/%Y")
    birthdate = datetime.strptime(input().strip(), "%d/%m/%Y")

    # 計算年齡
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    # 根據年齡進行輸出
    if age < 0:
        print("Case #{}: Invalid birth date".format(i + 1))
    elif age > 130:
        print("Case #{}: Check birth date".format(i + 1))
    else:
        print("Case #{}: {}".format(i + 1, age))