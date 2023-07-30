str1="Python Programing"

n=len(str1)

i=0

print("Forward Direction:")
while i<n:
    print(str1[i],end="")
    i+=1

print("\nBackWord Direction :")

i=-1

while i>=-n:
    print(str1[i],end="")
    i=i-1
