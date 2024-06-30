print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
name1l=name1.lower()
name2l=name2.lower()
True_count,Love_count=0,0
for i in "true":
  True_count+= name1l.count(i)+name2l.count(i)
for i in "love":
  Love_count+= name1l.count(i) +name2l.count(i)
score=10*True_count+Love_count
if score<10 or score>90:
  result=", you go together like coke and mentos."
elif score>=40 and score<=50:
  result=", you are alright together."
else:
  result="."
print("Your score is",str(score)+result)