premium_charge = 125
flat_charge = 20
def g_shipping_flat_c(weight):
	if (weight<=2):
		cost = weight * 1.50 + flat_charge
	elif (weight>2) and (weight<=6):
		cost = weight * 3.0 + flat_charge
	elif (weight>6) and (weight<=10):
		cost = weight * 4.0 + flat_charge	
	elif (weight>10):
		cost = weight * 4.75 + flat_charge
	return cost

print(g_shipping_flat_c(8.4))

def drone_shipping(weight):
	flat_charge = 20
	if (weight<=2):
		cost = weight * 4.50
	elif (weight>2) and (weight<=6):
		cost = weight * 9.0 
	elif (weight>6) and (weight<=10):
		cost = weight * 12.0 
	elif (weight>10):
		cost = weight * 14.25
	return cost

print(drone_shipping(1.5))

def best_price(weigth):
  costa = g_shipping_flat_c(weigth)
  print("Ground Shipping Plus:\t\t" + str(costa))
  costb = g_shipping_flat_c(weigth) + premium_charge - flat_charge
  print("Ground Shipping Premium:\t" + str(costb))
  costc = drone_shipping(weigth) 
  print("Drone Shipping:\t\t\t" + str(costc))
  if (costa<costb) and (costa<costc):
    print("You're best price is:")
    print("Ground Shipping Plus:\t\t" + str(costa))
	elif (costb<costa) and (costb<costc):
    print("jajajaja")


best_price(4.8)
#best_price(41.5)
  
  
  
  
  
  