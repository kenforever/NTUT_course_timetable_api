import requests
from bs4 import BeautifulSoup as bs
import TableExchange

def geTable(uid,password,year,sem):
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

    response = session.get('https://aps.ntut.edu.tw/course/tw/Select.jsp?format=-2&code='+uid+"&year="+year+"&sem="+sem,cookies = TCookie)
    TCookie = session.cookies.get_dict()

    soup = bs(response.text,"html.parser")
    table = soup.find('table')

    f = open("table","w")
    print(table,file=f)
    
    f.close()


