def compare(input_no):
    import json

    if len(input_no) != 3:
        err = "輸入錯誤!請輸入三位數字!!"
        print("輸入錯誤!請輸入三位數字!!")
        return err

    fileName = "List_of_winners2.json"
    with open(fileName) as f:
        data = json.load(f)
    result = []

    for key in data.keys():
        if input_no[1:3] in data[key]:
            result.append(key)

        elif input_no in data[key]:
            result.append(key)

    if len(result) != 0:
        ans = ""
        for i in result:
            ans += i + ", "

        return "恭喜你中了 " + ans[:-2] + "!!"

    else:
        ans = "恭喜你成為國家認證邊緣人!!"
        return ans

# a = input("請輸入身分證後三碼: ")
# compare(a)
