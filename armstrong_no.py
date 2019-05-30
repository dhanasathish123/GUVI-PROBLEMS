n=int(input())
sum=0
while(n!=0):
  rem=n%10
  sum=sum+rem**3
  n=n//10
if n==sum:
  print("yes")
else:
  print("no")
