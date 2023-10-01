answer = input("Do you want to play this text adventure game? [yes/no] ")
if answer == "yes":
     print("That's great!")
     print()
     
     answer=input("Do you want to explore a cave or jungle? [cave/jungle] ")

     if answer=="cave":
         print("You go into the cave and see a sleeping bear")
         print() 

         answer = input("Do you want to fight or run? [fight/run] ")

         if answer == "fight":
          print("Bears are really strong! You lose!")

         elif answer == "run":
          print("You ran away! You win!")

         else:
          print("Invalid option, you lose!")

     elif answer == "jungle":
      print("you meet a tiger and get eatten! you lose!")
 
     else:
      print("Invalid option,You lose!")   
else:
  print("but this is really a awesome game!")
         
