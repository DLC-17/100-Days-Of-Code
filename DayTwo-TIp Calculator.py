cost = float(input("What was the cost of your meal? $"))
tip = int(input("How much would you like to tip? %"))/100
print(round((cost + cost*tip),2) ,"is the total" )
people=int(input("Split amongst how many people? "))
print("$",round((cost+ cost*tip)/people,2), "is the amount split amongst", people,"people")