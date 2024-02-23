print("Hello welcome to pizza world")
want_pizza = input("Do you want some pizza?")
if want_pizza == "yes": 
    print("Great! you can choose up to 3 toppings")

    topping1 = input("Whats the first topping you want? ")


    topping2 = input("Whats the second topping you want? ")


    topping3 = input("Whats the third topping you want? ")



    allToppings = [topping1, topping2, topping3]

    order = ", " .join(allToppings)

    print("Ok that will be a" + order + " Pizza coming right up")

else:
    print("No pizza for you")  
#%%