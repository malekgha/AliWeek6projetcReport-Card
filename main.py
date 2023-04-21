################ Function Definitions ################

# Shows the user what options they have
def displayMenu():

  # This option will involve you adding a student and a collection for their grades to a dictionary!
  print("1. Add a Student")

  # This option will involve you removing a pair from a dictionary!
  print("2. Remove a Student")

  # This option will require you to grab a student from a dictionary and add a quiz grade to it's corresponding collection of grades!
  # You'll also need to use a pre-written function that ensures the user is entering a valid grade (a decimal number)
  print("3. Add Quiz Grade for Student")

  # This option will require you to use a loop to list all of the grades for an INDIVIDUAL student!
  print("4. List a Student's Quiz Grades")

  # This option will have you write a function that takes in a student's grade as a number and return the letter grade equivalent!
  print("5. Get Student's Letter Grade")

  print("6. Quit")

# Prompts the user to enter a numeric grade
# This function works, and ensures the user entered a valid float for the grade
# It's not important HOW this function works, but how to USE this function
def getNumberGradeFromUser():

  val = None

  while(val == None):
    try:
      test = float(input("Enter a Grade: "))
      val = test
    except:
      val = None
  
  return val

######################################## Main Program ########################################

# Application Loop
displayMenu()
  
# create a varibale to hold the user's option, an set it to a default value
choice = ""
# continue to loop the following code as long as the choice is not equal "Quit"
while choice != "Quit":
    
  # prompt the user to select an option
  choice = input("Select an ption: ")
 #print(choice)
  

##########################1_ Adding a Student###########################################
  if choice == "1":
    choice = input("Enter student name: ")
    print(f"{choice} added!")

#create a dictionary
students = {}

for key, value in students.items():
 #adding a new student with a new empty list
  students["choice"] = []
   

# user = ""
# while user != "Quit":

#   # Prompt the user to select an option
#   user = input("Select an option: ")

#   if user == "1":
#     option1 = input("Enter student name: ")
#     for key, value in student.items():
#       student[key] = [value]
    
#       print(f"{option1} added!")

#   if user == "2":
#     option2 = input("Enter student name: ")
#     print(f"{option2} removed!")
#   if user == "3":
#     option3 = input("Enter a grade: ")
#     print(f"Added {option3} to {option1} quizzes")
    







#######################################2_Removing a Student###################################











#######################################3_Adding Quiz grades###################################









########################################4_List a Student's Quiz grades########################










########################################5_Get student's Letter Grade#########################







#########################################6_Quit############################################