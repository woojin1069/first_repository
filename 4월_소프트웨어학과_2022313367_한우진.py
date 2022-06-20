n=int(input())
'''
n=5
table=[[14,10,8,8,9],[12,9,7,4,1],[4,0,8,2,3],[4,1,7,12,13],[6,2,10,2,3]]
'''
table=[]
for i in range(n):
    s=list(map(int,input().split()))
    table.append(s)
    


def transfer(count):

    flag=((count)//3)%4
    if flag==0:
        return [0,1,0,1]#y,부호,x,부호
    elif flag==1:
        return [-1,-1,-1,1]
    elif flag==2:
        return [0,-1,0,-1]
    elif flag==3:
        return [-1,1,-1,-1]
        

def serch(제한,table,지나간_곳들,목적지,현재위치,절대위치,count,count_case): #내 칸에서 갈 수 있는 선택지 중, 내가 이미 지나간 칸이거나, 가로막힌 칸인 경우는 제외하고 완전탐색)
    #print(현재위치,절대위치)
    if count>제한:
        return 0
    #if count==8:
        #print(지나간_곳들)
    #print("절대위치: %s, 현재위치: %s"%(절대위치,현재위치))
    if count>0 and count%3==0:
        temp_pos=현재위치[0]
        현재위치[0]=len(table)-1-현재위치[1]
        현재위치[1]=temp_pos
        temp_pos=목적지[0]
        목적지[0]=len(table)-1-목적지[1]
        목적지[1]=temp_pos
        #지나간_곳들+=[[현재위치[0],현재위치[1]]]
    if 현재위치==목적지:
            #print(지나간_곳들)
            #print("!!",목적지,현재위치,절대위치)
            #print(지나간_곳들)
        #if count==12:
            #print(목적지)
            #print(지나간_곳들)
        count_case.append(count)
            
        
        
    else:
        #print(현재위치,"\n",지나간_곳들,"\n\n\n")
        order=transfer(count)
        for i in range(5):
            if i!=4:
                temp_절대위치=[절대위치[0],절대위치[1]]
                temp_change=절대위치[abs((1-(i%2))+order[0])]+order[(1-(i%2))*2+1]*2*((1-(i//2))-1/2)
                temp_절대위치[abs((1-(i%2))+order[0])]=temp_change
            if i==0: #현재위치에서 x +1
                if  (temp_절대위치 not in 지나간_곳들) and ((table[현재위치[0]][현재위치[1]])%2 !=1): #모서리 조건도 추가?
                    temp=지나간_곳들+[temp_절대위치]
                    temp_목적지=목적지[:]
                    serch(제한,table,temp,temp_목적지,[현재위치[0],현재위치[1]+1],temp_절대위치,count+1,count_case)
            elif i==1: # 현재위치에서 y+1
                if (temp_절대위치 not in 지나간_곳들) and ((table[현재위치[0]][현재위치[1]])%4 <2):
                     temp=지나간_곳들+[temp_절대위치]
                     temp_목적지=목적지[:]
                     serch(제한,table,temp,temp_목적지,[현재위치[0]+1,현재위치[1]],temp_절대위치,count+1,count_case)
            elif i==2: #현재위치에서 x -1
                if (temp_절대위치 not in 지나간_곳들) and( (table[현재위치[0]][현재위치[1]])%8 <4):
                    temp=지나간_곳들+[temp_절대위치]
                    temp_목적지=목적지[:]
                    serch(제한,table,temp,temp_목적지,[현재위치[0],현재위치[1]-1],temp_절대위치,count+1,count_case)
            elif i==3: #현재위치에서 y+1
                if (temp_절대위치 not in 지나간_곳들) and ((table[현재위치[0]][현재위치[1]])<8):
                    temp=지나간_곳들+[temp_절대위치]
                    temp_목적지=목적지[:]
                    serch(제한,table,temp,temp_목적지,[현재위치[0]-1,현재위치[1]],temp_절대위치,count+1,count_case)
            else:     # 현재위치 유지
                    temp_목적지=목적지[:]
                    temp=지나간_곳들[:]
                    serch(제한,table,temp,temp_목적지,[현재위치[0],현재위치[1]],[절대위치[0],절대위치[1]],count+1,count_case)
                
    return 0
제한=min(3*4,2*n-1)
while 1:
    지나간_곳들=[]
    목적지=[n-1,n-1]
    현재위치=[0,0]
    count=0
    count_case=[]
    절대위치=[0,0]
    serch(제한,table,지나간_곳들,목적지,현재위치,절대위치,count,count_case)
    #print("!")
    if len(count_case)!=0:
        print(min(count_case))
        break
    else:
        #print(제한)
        #print(지나간_곳들)
        제한+=1

