# Even if you haven’t studied physics (recently or ever!), you might have heard that E = m*c*c
#, wherein 
#  E represents energy (measured in Joules), 
#  m represents mass (measured in kilograms), and 
#  c represents the speed of light (measured approximately as 300000000 meters per second), per Albert Einstein et al. Essentially, the formula means that mass and energy are equivalent.

# In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

# Function Brain for Calculation of E = m * c * c
def brain(m):
    c = 300000000
    # e = m * c * c
    e = int(m * pow(c, 2))
    return e

# Main Function
def main():
    mass = int(input("m: "))
    einstein = brain(mass)
    print("E:", einstein)

# Function Call
main()
