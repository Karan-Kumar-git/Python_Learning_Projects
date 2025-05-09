questions = ["what is the largest country in the world?\n 1. Russia\n 2. China\n 3. USA\n 4. Canada",
             "what is the largest planet in the solar system?\n 1. Jupiter\n 2. Saturn\n 3. Earth\n 4. Mars",
             "what is the capital of France?\n 1. Paris\n 2. London\n 3. Berlin\n 4. Madrid",
             "what is the namme of the largest ocean?\n 1. Atlantic Ocean\n 2. Indian Ocean\n 3. Arctic Ocean\n 4. Pacific Ocean",
             "what is the largest desert in the world?\n 1. Sahara\n 2. Thar\n 3. Atacma\n 4. Antarctica",]

answers = ["Russia",
          "Jupiter",
          "Paris",
          "Pacific Ocean",
          "Antarctica",]
round = 0
money = 0

print("Welcome to the quiz game!\n")

for question in questions:
    if round != 0:
        print("Next question:\n")
    print(question)
    User_input = input("Answer: ").title()
    if User_input == answers[questions.index(question)]:
        print("Correct!")
        money += 1000
        print(f"You have won {money} dollars!\n")
        print("-----------------------------------------------------------------------------\n")
        round += 1
    else:
        print("Incorrect!")
        break

print(f"You have won {money} dollars!")
print("Thank you for playing the quiz game!")
