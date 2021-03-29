import os
import FileCreate

def Exchange(uid):
    
    f = open('table','r')
    import re
    def courseRead():
        sp = line.split('>')
        sp = sp[1]
        sp = sp.split('<')
        sp = sp[0]
        CourseName.append(sp)
    
    def dayCount(inp):
        if count == 0:
            Mon.append(inp)
        if count == 1:
            Tue.append(inp)
        if count == 2:
            Wed.append(inp)
        if count == 3:
            Thu.append(inp)
        if count == 4:
            Fri.append(inp)
    line = f.readline()
    count = 0
    Mon = []
    Tue = []
    Wed = []
    Thu = []
    Fri = []
    for i in range(len(line)):
        while line:
            time = re.match(r'<th>',line)
            emptyCourse = re.match(r'<td>',line)
            course = re.match(r'<a',line)
            stop = re.search((r'</th>'),line)
            free = re.search(r'班週會及導師時間',line)
            pe = re.search(r'體育',line)
            
            if count >= 6:
                count = 0
                print()
            if stop:
                count = 0
                print()
            if time:
                sp = line.split('<br/>')
    
            if course:
                CourseName=[]
                for i in range(3):
                    courseRead()
                    line = f.readline()
                dayCount(CourseName)
                count +=1
            if free:
                dayCount("班週會及導師時間")
                count +=1
            if pe:
                dayCount("體育")
                count +=1
            if emptyCourse:
                a = ""
                dayCount(a)
                count +=1
            
            line = f.readline()
        f.close
    test = open("temp","w") 
    json = {}
    json["mon"]=Mon
    json["tue"]=Tue    
    json["wed"]=Wed
    json["thu"]=Thu
    json["fri"]=Fri
    print(json,file=test)
    test.close()
    test = open("temp","r")
    soruse = test.read()
    test.close()
    test=open("temp","w")
    ttest = soruse.replace("'","\"")
    test.write(ttest)
    test.close()
    uid = uid+".json"
    os.rename("temp",uid)

