n=input()
val=0
for i in n:
    if not i.isdigit() and not i.isalpha():
        val=val+1
print(val)
