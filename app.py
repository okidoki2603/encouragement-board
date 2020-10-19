print("Title of program: Encouragement bot")
print()
while True:
  description = input("how do you feel today?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("tomorrow will be better")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("to continue smiling")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("you are stronger than you believe")
      counter += 1

  if counter == 0:
    
      output = "Sorry, could you use different words and try again ?"

  elif counter == 1:
    
      output = "It seems that you are feeling really " + feelings_list[0] + ". However, please remember that "+ encouragement_list[0] + "! Hope you feel better soon! :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling really " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better soon!:)"

  print()
  print(output)
  print()
