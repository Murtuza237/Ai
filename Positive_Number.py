j=int(input("How Many numbers do you want: "))
i=1
input_list1=[]
output_list=[]

while i<=j:
    n=int(input("Enter a some number for list 1: "))
    input_list1.append(n)
    i+=1
for i in input_list1:
    if i>0:
        output_list.append(i)
        
print("Positive Numbers are: ")
for i in output_list:
    print(i, end=",")