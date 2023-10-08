# Static methods are similar to class methods,
# except they don't receive any additional arguments;
# they are identical to normal functions that belong to a class.

# They are marked with the staticmethod decorator.

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == 'pineapple':
            raise ValueError('No pineapples!')
        else:
            return True

    def __str__(self) -> str:
        return f'Ingredients in this pizza: {", ". join(self.toppings)}'


ingredients = ['cheese', 'onions', 'spam']
# ingredients = ['cheese', 'onions', 'pineapple', 'spam']
pizza = None
try:
    if all(Pizza.validate_topping(i) for i in ingredients):
        pizza = Pizza(ingredients)
except ValueError as e:
    print(e)

if pizza is not None:
    print(pizza)
