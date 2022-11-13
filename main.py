print("Replit Login System.")
print()
print("Do not try solve this one unless you are a hacker!😁😁")


def showWinMessage():
  print("Welcome to Replit!")
  print() 


def userInput():  
  while True:
    print()
    username = input("What is your username?: ")
    password = input("What is your password?: ")
    
    if username.lower() != "peter" or password.lower() != "peter@193":
      print()
      print("""Whoops! I don't recognize that username or password.
Try again!""")
      continue
    elif username.lower() == "peter" and password.lower() == "sequoia@193":
      print()
      print("You a phenomenal hacker!")
      print()
      showWinMessage()
      break
      

def endGame():
  while True:
    print()
    input("""Thank you for logging in!
Click Stop on top right page and click Run to try again.""")
    print()
    continue


if __name__=="__main__":
  userInput()
  endGame()