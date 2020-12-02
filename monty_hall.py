#monty hall problem
#https://en.wikipedia.org/wiki/Monty_Hall_problem

import random

boxes = [1,2,3]
no_change = 0
change = 0
attempt = 100000 #high enouch to satisfy law of large numbers

for i in range (0,attempt):
    #generate winning box and user choiche
    lucky_number = random.randint(1,3)
    user_choiche = random.randint(1,3)

    #remove one wrong answer 
    for item in boxes:
        if (item == lucky_number) or (item == user_choiche):
            continue
        boxes.remove(item)
        break

    #user do not change
    if user_choiche == lucky_number:
        no_change+=1
    else:
        change+=1


no_change_percent = (no_change*100)/attempt
change_percent = (change*100)/attempt
print ("Win %% without changing number %.2f" %no_change_percent)
print ("Win %% when changing number %.2f" %change_percent)
