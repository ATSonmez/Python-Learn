questions = ("How many elements are in the periodic table?", 
             "which animal lays the ;argest eggs", 
             "Abundat gas", 
             "Bones body", 
             "planet")


options = (("A", "B", "C",  "D"), 
           ("A", "B", "C",  "D"), 
           ("A", "B", "C1",  "D"), 
           ("A", "B", "C",  "D"), 
           ("A", "B", "C",  "D"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0 
question_num = 0

for question in questions:
    print("---------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect")
        print(f"{answers[question_num]} is the correct answer")
        
    question_num += 1