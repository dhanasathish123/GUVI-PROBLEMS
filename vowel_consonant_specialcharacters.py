n=input()
if(n>='a' && n<='z')||(n>='A' && n<='B'):
  if(n=='a' || n=='e' || n=='i' || n=='o' || n=='u' || n=='A' || n=='E' || n=="I" || n=='O' || n=='U'):
    print("Vowel")
  else:
    print("Consonant")
elif(n>=0 && n<=9):
  print("digit")
else:
  print("invalid")
