def get_contact_info():
    
    #print("Contact Information")
    
    FName=input("Enter your FirstName: ")
    LastName=input("Enter your LastName: ")
    Address=input("Enter your Address: ")
    Phone=input("Phone Number: ")
    EmailAdd=input("Enter Your Email: ")

    return FName, LastName, Address, Phone, EmailAdd
    
def select_pizza():
   sizes = ("Small", "Medium", "Large")
   toppings = ("HamandCheese", "DoubleCheese", "Pepperoni")

   print("Pizza Sizes:")
   for i, size in enumerate(sizes):
       print(f"(i+1). (size)")

   size_choice = int(input("Enter the number of pizza size: "))
   selected_size = sizes[size_choice - 1]

   selected_toppings = ()
   print("Pizza Toppings:")
   for(toppings):
       print(f"(i+1). (topping)")
       choice = input("Do you want this topping? (yes/no): ")
       if choice() == "yes":
           selected_toppings(toppings)
    
    return selected_size, selected_toppings

def calculate_price(size, toppings):
   price = 0

   if size == "Small":
       price += 120
   elif size == "Medium":
       price += 150
   elif size == "Large":
       price += 200

price += (toppings) * 1.5

   return price