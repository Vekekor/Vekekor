import random



def gambling(balance,round_number):
    n = 1
    while True:
            WIN_CHANCE = random.choice(["WIN","LOSE"])


            if WIN_CHANCE == "WIN":
                balance = balance * 2

            if WIN_CHANCE == "LOSE":
                balance = 0
                return "You lost"
            
            if n == round_number:
                return f"After {round_number} rounds you have {balance} dollars gz"
            n = n + 1

print(gambling(40,3))