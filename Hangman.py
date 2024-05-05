import random 

#Source: GitHub Gist 

#Link: https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c 

HANGMANPICS = [''' 

  +---+ 
  |   | 
      | 
      | 
      | 
      | 
=========''', ''' 

  +---+ 
  |   | 
  O   | 
      | 
      | 
      | 
=========''', ''' 

  +---+ 
  |   | 
  O   | 
  |   | 
      | 
      | 
=========''', ''' 

  +---+ 
  |   | 
  O   | 
 /|   | 
      | 
      | 
=========''', ''' 

  +---+ 
  |   | 
  O   | 
 /|\  | 
      | 
      | 
=========''', ''' 

  +---+ 
  |   | 
  O   | 
 /|\  | 
 /    | 
      | 
=========''', ''' 

  +---+ 
  |   | 
  O   | 
 /|\  | 
 / \  | 
      | 
========='''] 

 
#Making a list of puzzles 

movies = ["Beauty and the Beast", "Spider Man: No way home", "Encanto", "Divergent", "Moana"] 

food = ["Pizza", "Ravioli", "Lasagna", "Chicken Noodle Soup", "Shawarma Poutine"] 

phrases = ["Happy Birthday!", "You're amazing!", "Never say never!", "Be kind!", "Never give up!"] 

sports = ["Basketball", "Soccer", "Badminton", "Volleyball", "Tennis"] 

 

#Display the title and intro 

print("{:^80}".format("WELCOME TO HANGMAN!")) 

print() 

name = input("Enter name: ").title() 

print() 

print("Hi {}!".format(name)) 

print("I'm sure you know how to play this classic game of hangman.") 

print("However, if you don't (which is very unlikely :D),") 

print("Here are the INSTRUCTIONS:") 

print("You can choose a category to solve the puzzles.") 

print("This game will pick a random puzzle in the category of your choice and allow") 

print("you to guess it.") 

print("You can only make 6 wrong guesses.") 

print("GOOD LUCK and HAVE FUN! :D") 

input("Press [ENTER] to continue... ") 

 

#Put the program in a loop 

while True: 

 

  #Picks a random number for random puzzles 

  picker = random.randint(0,4) 


  #Display all the categories to the screen 

  print() 

  print("CHOOSE A CATEGORY: ") 

  print("{:^80}".format("-"*80)) 

  print("{:>10}{:10}".format("Quit",0)) 

  print("{:>10}{:10}".format("Movies",1)) 

  print("{:>10}{:10}".format("Food",2)) 

  print("{:>10}{:10}".format("Phrases",3)) 

  print("{:>10}{:10}".format("Sports",4)) 

  print("{:^80}".format("-"*80)) 

  print() 
 

  #Error trap so the that user enters a valid option 

  while True: 

      option = int(input("Enter option: (0 to exit) ")) 

      if (option >=0 and option <=4): 

          break 

      print("Please choose a valid category from 1 to 4 or (0 to exit).") 

      print()          

  #If user enters 0, exit the program 

  if option == 0: 

    print() 

    print("Hope you had lots of fun!") 

    break 

 
  #Select a random puzzle based on what category the user enters, define the category 

  elif option == 1: 

    category = "Movies" 

    puzzle = movies[picker].upper() 

     

  elif option == 2: 

    category = "Food" 

    puzzle = food[picker].upper() 

     

  elif option == 3: 

    category = "Phrases" 

    puzzle = phrases[picker].upper() 

     

  elif option == 4: 

    category = "Sports" 

    puzzle = sports[picker].upper() 

       

 

  #Set the wrong guesses counter to 0 

  wrong = 0 

 

  #Make a blank string for hidden word and guessed letters 

  hidden = "" 

  guessed = "" 

 
  #Add underscore to hidden for each uppercase character in puzzle 

  for i in range(len(puzzle)): 

      if(puzzle[i].isupper()): 

          hidden += "_" 

      else: 

          hidden = hidden + puzzle[i] 

 

  #Loop the actual playing part 

  while True: 

     

    print("{:^80}".format("-"*80)) 

    print() 

     

    #Print the hangman pic that is at the position of the number of wrong guesses 

    print(HANGMANPICS[wrong]) 

    print() 

 

    #Display the hidden word spaced out 

    for i in hidden: 

      print(i,end=" ") 

 

    #If user guesses the puzzle one letter at a time, break the loop 

    if(hidden == puzzle): 

      break 

 

    #Allow user to enter guess and error trap  

    while True: 

        print() 

        print() 

        print("The category is {}.".format(category)) 

        
        #Change the guess to uppercase 

        print("Guessed: {}".format(guessed.split())) 

        print() 

        guess = input("Enter guess: ").upper() 

        print() 

               

        #Make sure user enters one letter from A-Z or the whole puzzle 

        #Make sure the user does not enter the same letter more than once 

        if ((guess >= "A" and guess <= "Z") and (len(guess) ==1 or guess == puzzle) and guessed.find(guess)==-1 and guess!= ""): 

            break 


       

        print("Please enter a valid guess.") 

        print() 

         

        #If they guess a letter more than once, let them know 

        if (guessed.find(guess) >-1 and guess != ""): 

          print("You have already guessed {}.".format(guess)) 

          print() 

          print("Guess a different letter.") 

  
     

    #Store the users guesses in a string 

    guessed = guessed + guess + " " 

 

    #If user enters the whole puzzle correctly, get out of the guessing loop 

    if (guess == puzzle): 

      break 


    #If user's guess in found in puzzle 

    if(puzzle.find(guess) > -1): 

 

        #Loop through the length of puzzle and replace that character with guess 

        for i in range(len(puzzle)): 

            if (puzzle[i] == guess): 

              hidden = hidden[:i] + guess + hidden[i+1:] 

               

    #If user enters the wrong guess, add 1 to counter and let them know 

    else: 

      wrong+=1 

      print("Sorry '{}' is not in the puzzle.".format(guess)) 

      print() 

      print("This is wrong guess #{}.".format(wrong)) 

 


      #If the number of wrong guesses is 6, get out of the loop 

      if (wrong == 6): 

         

        #Display the last hangman pic before breaking loop 

        print(HANGMANPICS[wrong]) 

        break 

           

     

    print() 

    input("Press [ENTER] to continue ") 

 

  #If user has used up all their guesses, let them know 

  if (wrong == 6): 

      print() 

      print("Sorry {} you ran out of guesses.".format(name)) 

 

  #Else, tell them they got it 

  else: 

      print() 

      print() 

      print("YOU DID IT {}!! Good job!".format(name)) 

 

  #Allow them to play again   

  print() 

  again = input("Press [ENTER] to play again. ") 

  print() 

  print("{:^80}".format("-"*80)) 
