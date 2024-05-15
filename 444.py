def magic_data(str_data):
    data = str_data[:2]
    month = str_data[3:5]
    year = str_data[8:]
    s = int(data) * int(month)
    print(s)
    print(year)

    if int(data) * int(month) == int(year):
        return True
    else:
        return False


str = input("введите дату ")
if magic_data(str):
    print("магическая")
else:
    print("не магическая")