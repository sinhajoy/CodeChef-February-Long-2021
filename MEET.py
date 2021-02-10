def convert24(str1): 
	if str1[-2:] == "AM" and str1[:2] == "12": 
		return "00" + str1[2:-3] 
	elif str1[-2:] == "AM": 
		return str1[:-2] 
	elif str1[-2:] == "PM" and str1[:2] == "12": 
		return str1[:-3] 
		
	else: 
		return str(int(str1[:2]) + 12) + str1[2:5] 
    
def is_between(time, time_range):
    if time_range[1] < time_range[0]:
        if(time >= time_range[0] or time <= time_range[1]):
            return 1
        else:
            return 0
    if(time_range[0] <= time <= time_range[1]):
        return 1
    else:
        return 0

try:
    a=int(input())
    cur=[]
    star=[]
    en=[]

    for i in range(a):
        l=input()
        cur.append(convert24(l))
        one=[]
        x=int(input())
        start=[]
        end=[]
        for i in range(x):
            b=input()
            start.append(convert24(b[0:8]))
            end.append(convert24(b[9:len(b)]))
        star.append(start)
        en.append(end)


    faug=[]    
    for j in range(a):
        pubg=[]
        c=cur[j]
        s=star[j]
        e=en[j]
        for i in range(len(s)):
            pubg.append(str(is_between(c,(s[i],e[i]))))
        faug.append(pubg)
    
    for i in faug:
        sumation=''
        for j in i:
            sumation +=j
        print(sumation)
except :
    pass