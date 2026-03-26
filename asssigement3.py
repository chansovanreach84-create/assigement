distance_input = input("Enter the distance that they have to travel in kilometers :km ")
car_average_KPL_input = input("Car Average KPL :")
current_fuel_price_input = input("The current fuel price per liter : $")

distance = float(distance_input)
average_kpl = float(car_average_KPL_input)
fuel_price = float(current_fuel_price_input)
estimator_fuel_needed = distance / average_kpl
estimator_cost_thier_trip = estimator_fuel_needed * fuel_price

print(f"The estimator fuel needed for thier trip is : {estimator_fuel_needed:.2f}liters")
print(f"The estimator cost for thier trip is : ${estimator_cost_thier_trip:.2f}")
