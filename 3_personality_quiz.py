score = 0
print ('What were you like when you were in kindergarten?\n')
print ('You will be asked a series of questions, answer by typing A, B, or C.\n')
input ('To begin press enter.\n')

outfit_ques = input('What was your favorite outfit? \nA. overalls \nB. clean and matching \nC. halloween costume \n')
if outfit_ques == 'A':
    score = 2
elif outfit_ques == "B" :
    score = 1
elif outfit_ques == "C":
    score = 0
class_ques = input('What was your favorite class? \nA. finger painting \nB. ABCs \nC. recess \n')
if class_ques == 'A':
    score = score + 0
elif class_ques == "B" :
    score = score + 1
elif class_ques == "C" :
    score = score + 2
activity_ques = input('What was your favorite activity? \nA. playing house \nB. make believe \nC. wrestling \n')
if activity_ques == 'A':
    score = score + 1
elif activity_ques == "B" :
    score = score + 0
elif activity_ques == "C" :
    score = score + 2
friend_ques = input('What was your friend group like? \nA. Attached to one best friend \nB. you were a loner \nC. you were friends with anything that moved \n')
if friend_ques == 'A':
    score = score + 1
elif friend_ques == "B" :
    score = score + 2
elif friend_ques == "C" :
    score = score + 0

if 6<= score <= 8:
    print ("\nYou were a school yard bully.")
    
elif 3<= score <= 5:
    print ("\nYou were dressed by your parents and took your homework seriously.")
    
elif 0<= score <= 2:
    print ("\nYou truely believed you were a unicorn.")
    

