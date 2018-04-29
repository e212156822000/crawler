# crawler

寫的第一支爬蟲程式，用來解決工作上的實務問題。這支爬蟲程式解決了兩個不同的問題，原則上來說只有第一個問題牽涉到爬蟲，第二、三個問題是靠著別人寫的爬蟲來解決問題，我自己只做了一些爬下來的檔案處理而已，但兩個問題都還滿實際的，我想就寫在一起吧。

## 問題一：爬下資料製成excel檔案

![幫我解決問題](https://github.com/e212156822000/crawler/blob/master/readme_images/dialog.png)

![接受挑戰](https://github.com/e212156822000/crawler/blob/master/readme_images/Challenge-Accepted.jpg)

### 程式碼範圍

Problem1 這個資料夾

### 怎麼執行

1. 確定裝好了python，bs4，xlsxwriter 套件。
2. 在終端機下`cd Problem1 && python write_data_into_excel.py` 即可
3. 輸出檔案為plan.xlsx

### 程式步驟

1. `image_crawler.py`會把圖片都先裝好放在`images_new/`裡面
2. 然後`write_data_into_excel.py` 再去把圖片貼到xlsx裡面
3. 至於，`text_crawler.py`只是抓文字的主要程式碼，這段程式已經併寫到`write_data_into_excel.py` 裡面了，所以只是作為方便理解與debug用。

### 思考過程

先觀察網站架構，以下是網站的大概樣子。

![網站架構](https://github.com/e212156822000/crawler/blob/master/readme_images/website.png)

然後我們打開檢查原始碼來看：

![內部](https://github.com/e212156822000/crawler/blob/master/readme_images/structure.png)

我們發現圖片都是廠商的logo，所以沒有疑慮直接在抓img的tag就可以。
而廠商的敘述則是都放在class為right的div裡面。

後來發現抓下來的logo好小，點進去各別的網頁才發現有解析度更清晰的版本，規則如下：
- "xxxxx_A.jpg"是小的縮圖。
- "xxxxx_B.jpg"是大的原圖。

因此在`image_crawler.py`中有段程式碼特意把網址中的A改成了B。

## 問題二：給你廠商的名字，希望你找出所有廠商的logo

### 程式碼範圍

Problem2,3 這個資料夾

