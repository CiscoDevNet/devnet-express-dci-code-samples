food={"vegetables":["carrots","kale","cucumber","tomato"],"desserts":["cake","ice cream", "donut"]}
for hungry in food["vegetables"]:
	print("My favorite vegetable is " + hungry)
for hungry in food["desserts"]:
	print("My favorite dessert is " + hungry)

cars={"sports":{"Volkswagen":"Porsche","Dodge":"Viper","Chevy":"Corvette"},"classic":{"Mercedes-Benz":"300SL","Toyota":"2000GT","Lincoln":"Continental"}}
for auto in cars["sports"]:
	print("My favorite sports car make and model is the " + auto + " " + cars["sports"][auto])
for auto in cars["classic"]:
	print("My favorite classic car make and model is the " + auto + " " + cars["classic"][auto])

dessert={"iceCream":["Rocky Road","strawberry","Pistachio Cashew","Pecan Praline"]}
for yummy in dessert["iceCream"]:
	print("My favorite dessert is " + yummy)

soup={"soup":{"tomato":"healthy","onion":"bleh!","vegetable":"good for you"}}
for tastey in soup["soup"]:
	print("This " + tastey + " soup is " + soup["soup"][tastey])
