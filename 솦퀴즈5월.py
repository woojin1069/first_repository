n=int(input())
card=list(map(int,input().split()))
point=0
size=n
for i in range(n-2):
    #print(card[point])
    size=(n-i-1)
    temp=card[point]
    del card[point]
    point=(temp+point)%size
    
#print(card[point])
print(card[(point+1)%2])
