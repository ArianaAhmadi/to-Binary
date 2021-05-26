''''
n=int(input("Enter a binary number:"))
i=0
final=0
while(n!=0):
  temp=n%10
  temp=temp*(2**i)
  i=i+1
  final=final+temp
  n=n//10
print(final)
'''
''''
n=int(input("Enter decimal number:"))
L=[]
final_value=0
while(n!=0):
  temp=n%2
  L.append(temp)
  n=n//2
print(L[::-1])
'''