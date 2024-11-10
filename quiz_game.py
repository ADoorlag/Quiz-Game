print("Welcome to the game!")
questions = 21

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's go!")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("What year was the declaration of independence signed? ")
if answer == "1776":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
    
answer = input("What planet is known as the Red Planet? ")
if answer.lower() == "mars":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("What is the smallest prime number? ")
if answer == "2":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
    
answer = input("What is the largest planet in our solar system? ")
if answer.lower() == "jupiter":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
    
answer = input("What is the largest mammal in the world? ")
if answer.lower() == "blue whale":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
    
answer = input("What is the largest ocean in the world? ")
if answer.lower() == "pacific ocean":
    print("Correct!")
    score+=1
else:
    print("Incorrect!") 
    
answer = input("What is the smallest country in the world? ")
if answer.lower() == "vatican city":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


answer = input("What does HTML stand for? ")
if answer.lower() == "hypertext markup language":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("What is the capital of France? ")
if answer.lower() == "paris":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("What element does 'O' represent on the periodic table? ")
if answer.lower() == "oxygen":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
    
answer = input("Who developed the theory of general relativity? ")
if answer.lower() == "albert einstein":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("What does DNS stand for in computer networking? ")
if answer.lower() == "domain name system":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("What programming language is known for its snake logo? ")
if answer.lower() == "python":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
    
answer = input("In what year did the Titanic sink? ")
if answer == "1912":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("What does SSD stand for in computer storage? ")
if answer.lower() == "solid state drive":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("What is the derivative of sin(x)? ")
if answer.lower() == "cos(x)":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

final_score = ((score/5)*100)
print("Your score is " + str(score) + " points out of " + str(questions) + " questions. Your final score is " + str(final_score)+"%")