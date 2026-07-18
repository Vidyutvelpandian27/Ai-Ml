name = str(input("Enter names : "))
marks = list(map(int, input("Enter marks : ").split(" ")))
avg = sum(marks)/len(marks)
print("Total marks : ",sum(marks))
print("Average marks : ",avg)
if(avg >= 90):
    print("Grade A")
elif(avg >= 75):
    print("Grade B")
elif(avg >= 60):
    print("Grade C")
elif(avg >= 40):
    print("Grade D")
else:
    print("Fail!!!")
result = [f"Subject:{i+1}"  for i,score in enumerate(marks) if score<=40 ]
print("Subjects below 40:",end=" ")
print(result)
