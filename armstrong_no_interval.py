n,k=map(int,input().split())
for i in range(n,k):
    temp=i
    sum=0
    while(temp!=0):
        rem=temp%10
        sum=sum+rem**3
        temp=temp//10
    if i==sum:
        print(i,end=" ")
