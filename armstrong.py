num = int(input("enter value:"))
for i in range(2,num+1):
    num_str = str(i)
    length = len(num_str)
    sum = 0 
    for item in num_str:
        sum += int(item) ** length 
    if sum == i:
        print(sum)