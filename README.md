[![works badge](https://cdn.jsdelivr.net/gh/nikku/works-on-my-machine@v0.2.0/badge.svg)](https://github.com/nikku/works-on-my-machine)
# 北科大課表API

## installation
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/kenforever/NTUT_course_timetable_api)

`` pip install -r requirements.txt``

run ``app.py`` using flask 

## usage

### /pubkey
get pubkey for encrypting password 

```curl https://ntuttimetableapi.herokuapp.com/pubkey```

#### response
```
{"pubkey":"-----BEGIN PUBLIC KEY-----{{your_public_key}}-----END PUBLIC KEY-----"}
```
### /geTable
get timetable using post without password encryption
```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{
    "uid":{uid},
    "password":{password},
    "year":{year},
    "sem":{sem},
    "target":{search_target}
    }' \
  https://ntuttimetableapi.herokuapp.com/geTable
```
### /sec_geTable
get timetable using post with password encryption
```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{
    "uid":{uid},
    "password":{encrypted_password_using_RSA},
    "year":{year},
    "sem":{sem},
    "target":{search_target}
    }' \
  https://ntuttimetableapi.herokuapp.com/sec_geTable
```

#### response

```
{
    "info": {
        "sem": {samester},
        "target": {Student_id_of_your_search},
        "year": {year}
    },
    "fri": {
        "1": "empty",
        "10": {
            "classroom": [],
            "code": "297115",
            "course_name": "企業資料通訊",
            "professor": []
        },
        "11": {
            "classroom": [],
            "code": "297115",
            "course_name": "企業資料通訊",
            "professor": []
        },
        "2": "empty",
        "3": "empty",
        "4": "empty",
        "5": "empty",
        "6": "empty",
        "7": {
            "classroom": [],
            "code": "302562",
            "course_name": "體育",
            "professor": [
                "豐東洋"
            ]
        },
        "8": {
            "classroom": [],
            "code": "302562",
            "course_name": "體育",
            "professor": [
                "豐東洋"
            ]
        },
        "9": {
            "classroom": [],
            "code": "297115",
            "course_name": "企業資料通訊",
            "professor": []
        }
    },
    "mon": {
        "1": "empty",
        "10": "empty",
        "11": "empty",
        "2": "empty",
        "3": "empty",
        "4": "empty",
        "5": "empty",
        "6": "empty",
        "7": {
            "classroom": [
                "科研大樓240e"
            ],
            "code": "297114",
            "course_name": "管理資訊系統",
            "professor": [
                "阮明燦"
            ]
        },
        "8": {
            "classroom": [
                "科研大樓240e"
            ],
            "code": "297114",
            "course_name": "管理資訊系統",
            "professor": [
                "阮明燦"
            ]
        },
        "9": {
            "classroom": [
                "科研大樓240e"
            ],
            "code": "297114",
            "course_name": "管理資訊系統",
            "professor": [
                "阮明燦"
            ]
        }
    },
    "sat": {},
    ......etc
}
```




------
## 參數
參數     | type      | 註解
---------|-----------|--------
uid      | string    | 學號
password | string    | 密碼(在 ``sec_geTable`` 使用前請先用 ``/pubkey`` 以 RSA 加密)
year     | string    | 年度
sem      | string    | 學期
target	 | string    | 查詢對象(空值則會自動調用 ``uid`` 之值)

------
## 注意事項
**本 API 部分以明文傳遞帳號密碼等信息，在生產環境使用前請先自行評估安全性。**

## ToDo
- 下載json檔
- ~~查詢其他課表~~
- 英文版
- ~~api平台~~
- 取得年度與學期資料
- 直接使用 cookies 取得資料
