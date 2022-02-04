# 北科大課表API

## installation
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/kenforever/NTUT_course_timetable_api)

`` pip install -r requirements.txt``

run ``app.py`` using flask 

## usage

### /pubkey
get pubkey for encrypting password 

```curl {your_api_url}/pubkey```

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
  {your_api_url}/geTable
```

#### response

```
{
    "target_uid": {target_uid},
    "fri": [
        "",
        "",
        "",
        "",
        "",
        [
            "體育",
            "1001002"
        ],
        [
            "體育",
            "1001002"
        ],
        [
            "企業資料通訊"
        ],
        ""
    ],
    "mon": [
        "",
        "",
        "",
        "",
        "",
        [
            "管理資訊系統",
            "阮明燦",
            "科研大樓240e",
            "AB03001"
        ],
        [
            "管理資訊系統",
            "阮明燦",
            "科研大樓240e",
            "AB03001"
        ],
        [
            "管理資訊系統",
            "阮明燦",
            "科研大樓240e",
            "AB03001"
        ],
        "",
        ""
    ],
    "thu": [
        "",
        [
            "金融市場",
            "六教627(e)",
            "AB02016"
        ],
        [
            "金融市場",
            "六教627(e)",
            "AB02016"
        ],
        [
            "金融市場",
            "六教627(e)",
            "AB02016"
        ],
        [
            "創業之品牌管理與行銷",
            "陳春山",
            "二教206(e)",
            "1418008"
        ],
        [
            "創業之品牌管理與行銷",
            "陳春山",
            "二教206(e)",
            "1418008"
        ],
        "",
        [
            "財務金融實習",
            "梁亦鴻"
        ],
        [
            "企業資料通訊"
        ]
    ],
    "tue": [
        "",
        "",
        "班週會及導師時間",
        "班週會及導師時間",
        [
            "統計(二)",
            "丁秀儀",
            "六教627(e)",
            "AB02006"
        ],
        [
            "統計(二)",
            "丁秀儀",
            "六教627(e)",
            "AB02006"
        ],
        [
            "統計(二)",
            "丁秀儀",
            "六教627(e)",
            "AB02006"
        ],
        "",
        "",
        ""
    ],
    "wed": [
        "",
        "",
        "",
        "",
        "",
        "",
        [
            "哲學入門",
            "黃偉雄",
            "二教207(e)",
            "1410171"
        ],
        [
            "哲學入門",
            "黃偉雄",
            "二教207(e)",
            "1410171"
        ],
        "",
        [
            "企業資料通訊"
        ]
    ]
}
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
  {your_api_url}/sec_geTable
```

------
## 參數
參數     | type      | 註解
---------|-----------|--------
uid      | string    | 學號
password | string    | 密碼
year     | string    | 年度
sem      | string    | 學期
target	 | string    | 查詢對象(若無請傳送空值)

------
## 注意事項
**本 API 部分以明文傳遞帳號密碼等信息，在生產環境使用前請先自行評估安全性。**

## ToDo
- 下載json檔
- ~~查詢其他課表~~
- 英文版
- api平台
