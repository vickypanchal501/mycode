import re

filename = open("text.txt")


line_count = 0
line_number =[]

for line in filename :
    line_count += 1
    if re.findall("\A#---",line):
        line_number.append(line_count)
# print(line_number)
# 
filename.close()
filename = open("text.txt",'r')
readfile= filename.readlines()
print(readfile)
def func(line_number,readfile):
    li = []
    max_num = max(line_number)
    i = 0
    ques_num = 0
    while max_num > i:
        if re.findall("\A#---",readfile[i]):
            print(readfile[i])
            ques_num +=1
            li.append({"Question {}".format(ques_num):{}})

        if re.findall("\ALevel ",readfile[i]):
            g= readfile[i].split()
            li[-1]["Question {}".format(ques_num)][g[0]] = g[1]
            while True:
                i+=1
                if re.findall("\AQuest",readfile[i]):
                    continue

                if re.findall("\AHints:",readfile[i]):
                    break

                if "Question" not in li[-1]["Question {}".format(ques_num)]  :
                    # print("helo")
                    li[-1]["Question {}".format(ques_num)]["Question"] = str(readfile[i]).strip()
                                
                elif "Question"  in li[-1]["Question {}".format(ques_num)]  :
                    li[-1]["Question {}".format(ques_num)]["Question"] += str(readfile[i]).strip()
            
        
        
        
        
        if re.findall("\AHints:",readfile[i]):
            while True:
                i+=1
                if re.findall("\ASolution:",readfile[i]):
                    break
                if "Hints" not in li[-1]["Question {}".format(ques_num)]  :
                    # print("helo")
                    li[-1]["Question {}".format(ques_num)]["Hints"] = str(readfile[i]).strip()
                                
                elif "Hints"  in li[-1]["Question {}".format(ques_num)]  :
                    li[-1]["Question {}".format(ques_num)]["Hints"] += str(readfile[i]).strip()

        if re.findall("\ASolution:",readfile[i]):
            
            while True:
                i+=1
                if re.findall("\A#---",readfile[i]):
                    break
                if "Solution" not in li[-1]["Question {}".format(ques_num)]  :
                    # print("helo")
                    li[-1]["Question {}".format(ques_num)]["Solution"] = str(readfile[i]).strip()
                                
                elif "Solution"  in li[-1]["Question {}".format(ques_num)]  :
                    li[-1]["Question {}".format(ques_num)]["Solution"] += str(readfile[i]).strip('\n')
        i+=1  
        
         
    return li
op = func(line_number,readfile)
print(op)
