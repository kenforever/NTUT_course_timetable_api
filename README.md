# 北科大課表API

## 使用教學
1. 安裝flask, requests, bs4
2. 運行 main.py
3. 發送POST請求到/geTable
------
## 參數
參數     | type      | 註解
---------|-----------|--------
uid      | string    | 學號
password | string    | 密碼
year     | string    | 年度
sem      | string    | 學期

------
## 注意事項
**本API以明文傳遞帳號密碼等信息，請勿將其使用於生產環境。**

## ToDo
- 下載json檔
- 查詢其他課表
- 英文版
- api平台