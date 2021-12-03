from selenium.webdriver import Chrome
import time, json
from bs4 import BeautifulSoup

# 建立 driver, 開啟加碼券中獎網頁
driver = Chrome('./chromedriver.exe')
url = 'https://vhpi.5000.gov.tw/'
driver.get(url)
time.sleep(3)

# 取得網頁原始碼，並取得各種加碼券的名稱
soup = BeautifulSoup(driver.page_source, 'html.parser')
titles_soup = soup.select("img")
titles = [title["alt"] for title in titles_soup]

#建立空 Dict
dict = {}

#以 selenium 點擊周次後，將各週中獎號碼加入 Dict
for week in range(1,5):
    # 按下週次按鍵
    driver.find_element_by_xpath(f'/html/body/div[1]/div/div/ul/li[{week}]/a').click()
    time.sleep(2)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    numbers_soup = soup.select("ul.p-num")
    numbers = []
    for i in numbers_soup:
        number_i = i.select("li")
        tmp = []
        for j in number_i:
            tmp.append(j.text)
        numbers.append(tmp)

    for x, y in zip(titles, numbers):
        try:
            dict[x] = dict[x] + y
        except:
            dict[x] = y
    print("week",week," Finally!")

#關閉瀏覽器
driver.close()

#將結果存為 Json檔保存
fileName = "List_of_winners2.json"
file = open(fileName, "w")
json.dump(dict, file)
file.close()