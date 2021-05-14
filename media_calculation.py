def inform_user():
  print('\nPlease select a number between 0 and 10 (inclusive)\n')
  # print("\n")

#  CALCULATE THE MEDIA
def media_calculation(grades):
  grade1 = grades[0]
  grade2 = grades[1]

  division = len(grades)

  sum = 0

  for grade in grades:
    sum+=grade
    b = sum/division
  
  return b

# VERIFY IF THE STUDENT WAS APRROVED OR REPROVED
def verify_situation(nome,grade1, grade2):
  if grade1 < 0 or grade1 > 10 or grade2 < 0 or grade2 > 10:
    inform_user()
    student_situation()
  else:
    b = calculate_media([grade1, grade2])

    if b >= 6:
      print(f'\nThe student: {nome} was approved ({b})')
    else:
      print(f'\nThe student: {nome} was reproved ({b})')

# VERIFY WHO NEEDS TO VERIFY THE MEDIA      
def student_situation():
  inform_user()

  nome = input("Inform the student's name please: ")
  g1 = float(input('Inform a number from 0 to 10: '))
  g2 = float(input('Inform other number from 0 to 10: '))

  verify_situation(nome, g1, g2)
  
#   CALL THE FUNCTION TO INITIALIZE THE PROGRAM
  student_situation()
