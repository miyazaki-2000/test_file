def make_pizza(size,*toppings):
	print(f"\nMaking a {size}-inch pizza with the following toppings")
	for topping in toppings:
		print(f"-{topping}")

from test_9 import car

my_car=car('audi','a4',2019)
print(my_car.get_descriptive_name())
