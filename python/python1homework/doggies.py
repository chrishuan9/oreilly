__author__ = 'chris'
"""
Objective 1:
This project tests more of your understanding of classes and objects.

1. Create a new Python source file named doggies.py.
2. Write a class named Dog. Dog's __init__() method should take two parameters, name and breed, in addition to the
implicit self.
3. Bind an empty list to a dogs global variable (dogs should not be an attribute of the Dog class).
4. Using a while loop, get user input for name and breed. The loop should terminate when the user enters a blank name.
5. For each name and breed entered, create an instance of the Dog class with name and breed as arguments. Append the
object to the dogs list.
6. Each time around the loop, print the current dogs list (the name and breed of each dog).

Below is an example of possible output from running the program.

Name: Snoopy
Breed: Beagle
DOGS
0. Snoopy:Beagle
****************************************
Name: Marmaduke
Breed: Great Dane
DOGS
0. Snoopy:Beagle
1. Marmaduke:Great Dane
****************************************
Name: Rover
Breed: Mutt
DOGS
0. Snoopy:Beagle
1. Marmaduke:Great Dane
2. Rover:Mutt
****************************************
Name:
"""


class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __str__(self):
        return "{0}:{1}".format(self.name, self.breed)


if __name__ == "__main__":
    dogs = []
    while True:
        inputName = input("Name: ")
        if not inputName:
            break
        inputBreed = input("Breed: ")
        dogs.append(Dog(inputName, inputBreed))
        print("DOGS")
        for i, dog in enumerate(dogs):
            print("{0}. {1}".format(i, dog))
        print("*" * 41)

