from typing import Any
# Program #1: Kilometer Converter
# Write a program that asks the user to enter a distance in kilometers, 
# then converts that distance to miles.  The conversion formula is as follows:  
# Miles = kilometers x 0.6214.   
# The conversion must be done as a function with input and output.

def float_input(text: str) -> float:
    """
    Get console input with type of float, asks again if not correct type
    """
    while True:
        try:
            out: float = float(input(text))
            return out
        except ValueError:
            print("Incorrect type inputted, please input type: Float")


def kilometer_conversion(kilometers: float):    
    miles: float = 0.0
    ######################
    # WRITE YOUR CODE HERE
    ######################    
    miles = kilometers * 0.6214

    # Return the variable to the calling function
    return miles

#### This piece of the code has been done for you,
#### you only need to worry about the actual temp 
#### conversion logic in the temp_conversion function
if __name__ == '__main__':
    # Get User Input
    kilometers: float = float_input("Number of kilometers: ")
    # Call kilometer_conversion
    miles: float = kilometer_conversion(kilometers)
    print(f"Miles: {miles:.3f}")
    # Display the miles
