cars = 100
space_in_car = 4.0

drivers = 30

passengers = 90

cars_not_driven = cars - drivers

cars_driven = drivers

carpool_capacity = cars_driven * space_in_car

average_passengers_per_car = passengers / cars_driven




print  "There are", cars, "cars avaliable"

print "There are only",drivers ,"drivers avaliable"

print "There will be", cars_not_driven,"empty cars today"

print "we can tarnsport",carpool_capacity,"pelple today."

print "we have ",passengers,"to carpool today"

print "we need to put about",average_passengers_per_car,"in each car"
