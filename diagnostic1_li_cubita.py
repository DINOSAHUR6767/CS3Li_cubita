shipping_speed = input("Enter shipping speed (express, overnight, standard): ")
cart_total = float(input("Enter cart total: "))



def calculate_checkout(cart_total, shipping_speed):
   
   if shipping_speed == "express":
      shipping_cost = 15.00
   elif shipping_speed == "overnight":
      shipping_cost = 25.00
   elif shipping_speed == "standard" and cart_total >= 100:
            shipping_cost = 0.00
   elif shipping_speed == "standard" and cart_total < 100:
            shipping_cost = 10.00        
   else:
        print("error")
        shipping_cost = 0.00

   total= cart_total + shipping_cost
    
   return total
print("Total checkout amount: $", calculate_checkout(cart_total, shipping_speed))
 #Example 
 #print(calculate_checkout(10000,"express"))
#print(calculate_checkout(10000,"overnight"))
#print(calculate_checkout(50,"standard"))
