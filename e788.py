def sort_students(student_data):
    # 解析學生資料並存儲在列表中
    students = []
    for data in student_data:
        parts = data.split()
        student_id = parts[0]
        name = parts[1]
        students.append((student_id, name))

    # 排序規則：
    # 1. 依照學院代碼A~Z的順序。
    # 2. 若學院代碼相同，依學號開頭由小到大，4(學士) à 6(碩士) à 8 (博士)。
    # 3. 若學院代碼、學號開頭皆相同，則依報名順序排列。
    sorted_students = sorted(students, key=lambda student: (student[0][-1], student[0][0]))

    # 輸出排序結果
    for student in sorted_students:
        print(f"{student[0][-1]}: {student[1]}")

# 範例輸入
# student_data = [
#     "60547020S Wayne",
#     "40547036S Lisa",
#     "40707001A Alber",
#     "80652135E Frank",
#     "40923313A Roger"
# ]

student_data = []

n = int(input())
for i in range(n):
    student_data.append(input())

# 進行排序並輸出結果
sort_students(student_data)