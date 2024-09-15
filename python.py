class Person:
    def __init__(self,name,age,gender):
        self.name=name  # Attribute for person's name
        self.age=age    # Attribute for person's age
        self.gender=gender  # Attribute for person's gender

    def introduce(self):
        # Method to introduce the person
        print(f'Hello, my name is {self.name}. I am {self.age} years old and I identify as {self.gender}.')


# Create an instance of the Person class
Person1=Person('Jonathan',25,'Male')
# addition 
Person2=Person('Alice',20,'Female')

# Call the introduce method to display the person's information
Person1.introduce()
Person2.introduce()