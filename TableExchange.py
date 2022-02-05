import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize
import json
import math
import re

def to_dict(day,target):
    day_list = {}
    for i in range(len(day)):
        day_temp = day[i]
        classroom = []
        professors = []
        try:
            math.isnan(day_temp)
            day_list[i+1] = "empty"
        except:
            course_temp = day[i].split(" ")
            course_name = course_temp[0]
            if len(course_temp) == 1 or course_name == "班週會及導師時間":
                pass
            elif len(course_temp) == 2:
                if bool(re.search(r'\d',course_temp[1])):
                    classroom.append(course_temp[1])
                else:
                    professors.append(course_temp[1])
            else:
                classroom.append(course_temp[-1])
                for professor in course_temp[1:-1]:
                    professors.append(professor)

            day_list_temp = {
                "course_name": course_name,
                "professor": professors,
                "classroom": classroom,
                "code": get_course_code(course_name,target)
            }
            day_list[i+1] = day_list_temp
    return day_list

def get_course_code(name,target):

    if name == "班週會及導師時間":
        return ""

    with open("./temps/"+target,"r") as f:
        lines = f.readlines()
    for line in lines:
        if name in line:
            code = line.split(";")[1].split("\"")[0].split("=")[1]
            return code

def Exchange(target):
    with open("./temps/"+target,"r") as f:
        lines = f.readlines()
    with open("./temps/"+target,"w") as f:
        for line in lines:
            if line.startswith("<tr><td align=\"center\" colspan=\"6\">") == False:
                f.write(line)

    table_MN = pd.read_html("./temps/"+target,encoding='utf-8')
    table_dataframe = pd.DataFrame(table_MN[0])

    mon = to_dict(table_dataframe["一"].tolist(),target)
    tue = to_dict(table_dataframe["二"].tolist(),target)
    wed = to_dict(table_dataframe["三"].tolist(),target)
    thu = to_dict(table_dataframe["四"].tolist(),target)
    fri = to_dict(table_dataframe["五"].tolist(),target)
    try:
        sat = to_dict(table_dataframe["六"].tolist())
    except:
        sat = {}
    

    total_list = {
        "mon": mon,
        "tue": tue,
        "wed": wed,
        "thu": thu,
        "fri": fri,
        "sat": sat
    }

    with open("./temps/"+target+".json","w",encoding="utf-8") as f:
        json.dump(total_list,f,ensure_ascii=False)