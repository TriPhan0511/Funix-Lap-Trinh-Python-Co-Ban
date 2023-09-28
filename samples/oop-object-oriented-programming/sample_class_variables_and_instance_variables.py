class Shark:
    # Class variables
    animal_type = 'fish'
    location = 'ocean'

    # Constructor method with instance variables name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method with instance variable followers
    def set_followers(self, followers):
        print(f'This use has {followers} followers.')


def main():
    # First object, set up instance variables of constructor method
    sammy = Shark('Sammy', 5)

    # Print out instance variable "name"
    print(sammy.name)  # Sammy

    # Print out class variable "location"
    print(sammy.location)  # ocean

    # Second object
    stevie = Shark('Stevie', 8)

    # Print out instance variable "name"
    print(stevie.name)  # Stevie

    # Use set_followers method and pass "followers" instance variable
    stevie.set_followers(77)#This use has 77 followers.



if __name__ == '__main__':
    main()
