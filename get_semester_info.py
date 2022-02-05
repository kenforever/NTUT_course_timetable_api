import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
  

def get_semester_info(uid,password,target):

    session = requests.Session()
    headers = {"referer":"https://nportal.ntut.edu.tw/index.do"} 
    ac = {'muid':uid, 'mpassword':password}
    response = session.post('https://nportal.ntut.edu.tw/login.do',data = ac, headers=headers)
    Cookies = session.cookies.get_dict()

    session = requests.Session()
    response = session.get('https://nportal.ntut.edu.tw/ssoIndex.do?apUrl=https://aps.ntut.edu.tw/course/tw/courseSID.jsp&apOu=aa_0010-&sso=true',cookies=Cookies)
    soup = bs(response.text,"html.parser")
    value = soup.find('input', {'name': 'sessionId'}).get('value')

    response = session.get('https://aps.ntut.edu.tw/course/tw/courseSID.jsp?sessionId='+value+'&reqFrom=Portal&userid='+uid+'&userType=50')
    TCookie = session.cookies.get_dict()

    response = session.get('https://aps.ntut.edu.tw/course/tw/Select.jsp?format=-3&code='+target,cookies = TCookie)
    TCookie = session.cookies.get_dict()

    soup = bs(response.text,"html.parser")

    table = soup.find_all('table')
    df = pd.read_html(str(table[0]))

    data = str(pd.DataFrame(df[0])).split("\n")[1:]

    semesters = []
    for row in data:
        row = row.split(" ")
        year = row[2]
        sem = row[-2]
        semester = [year,sem]
        semesters.append(semester)
        
    return semesters