num=input("Enter value:\n")
list2=[]
oppositevalue=""
length=len(num)
for i in range(length):
    list2.append(num[i])
for i in range(length):
    num=list2[length-i-1]
    oppositevalue=oppositevalue+num

print(f"The digits reversed is {oppositevalue}")
