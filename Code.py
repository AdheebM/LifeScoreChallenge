import random
import datetime

fo=0
count=1
history = []

def status(name, count, life_score):
    print("\n*Game status*")
    print("Player Name:", name)
    print("Total attempts:", count)
    print("Final score:", life_score)
    if count > 20:
        print("YAY you saved the world")
    else:
        print("Oh no you were defeated")
        
    return
name = input("Enter your name (as DON): ")
life_score = random.randint(1, 50)
while count <= 20:
        
        print("\nAttempt:", count)
        print(name + "'s life score is:", life_score)

        if count >= 16:
            rand1 = random.sample(range(20000, 100000), 5)
        elif count >= 11:
            rand1 = random.sample(range(3000, 10000), 5)
        elif count >= 6:
            rand1 = random.sample(range(250, 2000), 5)
        else:
            rand1 = random.sample(range(15, 100), 5)

        print("Numbers to fight with:", rand1)
        
        random_num = int(input("Select a number to fight: "))

        if random_num not in rand1:
            print("You have input a number that is not within range given")
            status(name, count, life_score)
            break
        
        elif random_num <= life_score:
            print("You fought the number", random_num, "successfully!")
            life_score += random_num
            print("Your updated Life Score is:", life_score)
            history.append([count, life_score, rand1, random_num])

        else:
            print("The number", random_num, "killed you!! RIP")
            print()
            status(name, count, life_score)
            history.append([count, life_score, rand1, random_num])
            break
        
        
        count += 1
        
        if count > 20:
            print("\nCongratulations! You have completed all 20 attempts successfully.")
            print("Game Over")
            status(name, count, life_score)


current_datetime = datetime.datetime.now()

formatted_datetime = current_datetime.strftime("%Y_%m_%d_%H_%M_%S_%f")

filename = f"{formatted_datetime}.txt"

with open(filename, "w") as fo:
    fo.write(f"Player name: {name}\n")

    for attempt in history:
        count, life_score, rand1, random_num = attempt
        
        fo.write(f"Attempt: {count}\n")
        fo.write(f"{name}'s life score is: {life_score}\n")
        fo.write("Numbers to fight with: " + " ".join(map(str, rand1)) + "\n")
        fo.write(f"Select a number to fight: {random_num}\n")
        fo.write(f"{random_num} killed {name}\n")
        fo.write("\n")

    fo.write("*** Game Information ***\n")
    fo.write(f"Player Name: {name}\n")
    fo.write(f"Final score: {life_score}\n")
    fo.write(f"Game played at: {datetime.datetime.now()}\n")
    
