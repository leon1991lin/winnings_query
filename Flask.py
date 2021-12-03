from flask import Flask, request, render_template
import compare

app = Flask(__name__)

@app.route("/", methods  = ["GET","POST"])
def poker():
    outStr = """
    <h1>加碼券中獎查詢</h1>
    <h3>請輸入你的身分證後三碼:</h3>
    <form action = "/" method = "POST">
        <input name = "ID">
        <button type = "submit">查詢</button>
    </form>
    """

    method = request.method
    if method == "GET":
        return outStr
    if method == "POST":
        input_no = request.form.get("ID")
        rus = compare.compare(str(input_no))

        outStr2 = f"""
        <h1>{rus}</h1>
        <h3>注意事項1: 藝Fun券(紙本) 資格限定 18 歲以下或 65 歲以上</h3>
        <h3>注意事項2: 每週次僅能中簽加碼券一次，重複者依據登記排序取優先者</h3>
        <form action = "/" method = "GET">
            <button type = "submit">返回查詢</button>
        """
        return outStr2
    return ""

if __name__ == "__main__":
    app.run(host='127.0.0.1' ,port='12345',debug=True) #debug 可自動偵測網頁更新，無須重啟程式