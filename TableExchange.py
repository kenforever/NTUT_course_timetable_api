import os
import FileCreate
import re
def Exchange(target):
    
    f = open(target,'r',encoding='utf-8')
    
    def separate():
        sp = line.split('>')
        sp = sp[1]
        sp = sp.split('<')
        sp = sp[0]
        return sp

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
            course = re.search('<a href="Curr.jsp?',line)
            
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
            
            if pe:
                Course_Code=re.findall(r'(?<=code=)\w+',line)[0]
                total = ["體育",Course_Code]
                dayCount(total)
                count +=1
                line = f.readline()
                break
            
            if course:
                is_finish = False
                total = []
                
                Course_Name_Temp = separate()
                total.append(Course_Name_Temp)
                Course_Code=re.findall(r'(?<=code=)\w+',line)[0]
                line = f.readline()
                while is_finish != True:
                    teacher = re.search('Teach',line)
                    Classroom = re.match(r'<a href="Croom.jsp',line)
                    stop_td = re.match(r'</td>',line)
                    if teacher:
                        teacher_Name_Temp = separate()
                        total.append(teacher_Name_Temp)
                        line =f.readline()
                        
                    if Classroom:
                        classroom_Temp = separate()
                        total.append(classroom_Temp)
                        total.append(Course_Code)
                        is_finish = True
                        break
                    if stop_td:
                        is_finish = True
                        break
                line = f.readline()
                dayCount(total)
                count +=1
            if free:
                dayCount("班週會及導師時間")
                count +=1
            
            if emptyCourse:
                a = ""
                dayCount(a)
                count +=1
            
            line = f.readline()
        f.close
    test = open("temp","w",encoding='utf-8') 
    json = {}
    del Mon[4]
    del Tue[4]
    del Wed[4]
    del Thu[4]
    del Fri[4]
    json["mon"]=Mon
    json["tue"]=Tue 
    json["wed"]=Wed
    json["thu"]=Thu
    json["fri"]=Fri
    json["target_uid"]=target
    print(json,file=test)
    test.close()
    test = open("temp","r",encoding='utf-8')
    soruse = test.read()
    test.close()
    test=open("temp","w",encoding='utf-8')
    ttest = soruse.replace("'","\"")
    test.write(ttest)
    test.close()
    target = target+".json"
    os.rename("temp",target)

