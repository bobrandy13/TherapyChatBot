import time
import random 
reason = input("what brings you here today? ")

# STARTING_MONEY = 1000

wallet = open("wallet.txt", 'r+')

# wallet.write(str(STARTING_MONEY))

money = int(wallet.readline())

allowed_commands = ["spine problems", "trauma", "some problms"]
solutions = [
    "skill issue",
    "wow im so happy for you, or dang sorry that happened",
    "mmm i see i see... ok, that will be $500",
    "im sorry you feelthat way",
    "let's unpack that",
    "have you considered going outside and touching grass???",
    "LMAO????", 
]

print(money)

def payment(response):
    global money
    wallet.truncate()
    if (response == "mmm i see i see... ok, that will be $500"):
        money -= 500
        wallet.write(str(money))
    else:
        money -= 100
        wallet.write(str(money))
 


def fix_problems(reason):
    global money
    time.sleep(2)
    # print(money)
    print("thnking....")
    time.sleep(5) 
    response = random.choice(solutions)
    payment(response)

    print("-------------------------")
    print(response)
    print("-------------------------")


while money > 0 or reason != "EXIT": 

    fix_problems(reason)
    print("you have", money, "left. Spend wisely.")
    reason = input("what brings you here today? ")



wallet.close()