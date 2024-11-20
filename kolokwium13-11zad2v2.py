import random


healthpoints = int("100")
experience = int("0")
healthpoints <=100
experience > 0 
potion = 0

while 1>0:
    print(f"\nYou have {experience} EXP and {healthpoints} HP. What do you want to do?")
    print(f"a) Attack")
    print(f"h) Hide")
    print(f"p) Use potion")
    print(f"e) Exit")
    choice = (input("Your choice: "))

    if choice == "a":
        experiencelog = random.randint(1,10)
        healthpointslog =  random.randint(10,50)
        healthpoints = healthpoints - healthpointslog
        if healthpoints >0:
            experience = experience + experiencelog
            
            print(f" Your choice: a \nAttack! You have gined {experiencelog} EXP, but at a cost of {healthpointslog} HP. \n You have {experience} EXP and {healthpoints} HP. What do you want to do?")
        elif healthpoints <0:
            print(f"Game over! Your final score is {experience} EXP.")
            break


    elif choice == "h":
        healthpointsgain = random.randint(0,5)
        experienceloss = random.randint(0,10)
        if healthpoints >0 and healthpoints + healthpointsgain <= 100: 
            healthpoints = healthpoints + healthpointsgain
        if experience > 0:
            experience = experience - experienceloss
        if experience < 0: 
            experience = 0
        print(f" Your choice: h \n Hide! You have gained {healthpointsgain} HP, but at a cost of {experienceloss} EXP. \n You have {experience} EXP and {healthpoints} HP. What do you want to do?")


    elif choice == "p":
        if potion == 0 and healthpoints >= 0 and healthpoints<=50:
            healthpoints = healthpoints + 50
            potion += 1
            print(f"Your choice: p \n Recovery! +50 HP for you. \n You have {experience} EXP and {healthpoints} HP. What do you want to do? ")
        elif potion == 0 and healthpoints>=50 and healthpoints<=100:
            potion = 100 - healthpoints
            healthpoints = healthpoints + potion
            potion += 1
            print(f"Your choice: p \n Recovery! +{potion} HP for you. \n You have {experience} EXP and {healthpoints} HP. What do you want to do? ")
        elif potion == 1:
            print(f"No potion left, no recovery for you. Sorry! \n You have {experience} EXP and {healthpoints} HP. What do you want to do? ")


    elif choice == "e":
        print(f"Game over! Your final score is {experience} EXP.")
        break
   
