name = input("Enter your name = ")
print("Hello Welcome ", name)

height = int(input("Enter your height = "))

if height > 120:
 print("Congratulations, You are eligible with your height")



 age = int(input("Enter Your Age = "))

 if age <12:
  price = 10
  print("Your ticket price is ", price )

 elif age  >18:
  price =30
  print("Your ticet price = " , price )
  
 else:
  price = 20
  print("Your Ticket Price is = ", price)

 photo = input("Do you need to take a photo while the ride? ")

 if photo == "yes":
  pri = price + 50
  print("Your tital ticket prie is ", pri )
 else:
  print("Okey, Your Total Ticket Price is , ", price) 

  
else:
 print("Sorry !! You are not eligible to ride roller - coaster")



