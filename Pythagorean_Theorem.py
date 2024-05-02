# Print instructions.
print("How this program works:\n")
print("We use here the pythagorean theorem to find the sides of a RIGHT TRIANGLE")
print("Side A is the shortest side, side B is the second longest, and side C is the hypothenuse.")
print('''We will ask you to type the parameters and the unknown side MUST be typed as a "?".''')
print("Just press X to quit.(Top left)")

# Use this to find the square root in the functions
import math

run = True

# Put on loop
while run:
    # Ask for the parameters
    sa = input("\nSide A: ")
    sb = input("Side B: ")
    sc = input("Side C: ")

    # The boring math stuff

    # Math to find side A
    def findA():
        print("\nWe will find side A for you...\n")
        ss = int(sc)*int(sc) - int(sb)*int(sb)
        sa = math.sqrt(int(ss))
        print("Answer:")
        print(sa)
        print("\nFor certain purposes, you may not need to find the square root.")
        print("\nWe will give you a non-square rooted answer too:")
        print(sa*sa)
    # Math to find side B    
    def findB():
        print("\nWe will find side B for you...\n")
        ss = int(sc)*int(sc) - int(sa)*int(sa)
        sb = math.sqrt(int(ss))
        print("Answer:")
        print(sb)
        print("\nFor certain purposes, you may not need to find the square root.")
        print("\nWe will give you a non-square rooted answer too:")
        print(sb*sb)

    # Math to find side C    
    def findC():
        ss = int(sa)*int(sa) + int(sb)*int(sb)
        sc = math.sqrt(ss)
        print("\nAnswer:")
        print(sc)
        print("\nFor certain purposes, you may not need to find the square root.")
        print("\nWe will give you a non-square rooted answer too:")
        print(sc*sc)


    # Check if Side A is a "?", a number, or invalid
    if sa == "?":
        findA()
    elif sa == int:
        pass

    # Check if Side B is a "?", a number, or invalid
    elif sb == "?":
        findB()
    elif sb == int:
        pass
        
    # Check if Side C is a "?", a number, or invalid
    elif sc == "?":
        findC()
    elif sc == int:
        pass

    # If not all the parameters are valid, print this and repeat.
    else:
        print("\nSeems you are testing the program and accidentally typed all the parameters!")
        print('''Haha! Next time, you should leave one out and type "?" instead. ''')
        print("\nIf that is not the case, you were probably messing around and typing letters...")
    
        
    ask = True
    
    # Ask if user wants to repeat the program
    while ask:

        # Create "yn" as the user's answer
        yn = input("\nRepeat? (y/n)\n")

        # If user's answer is yes, repeat the prorgam
        if yn == "y" or yn == "Y" or yn == "Yes" or yn == "yes" or yn == "sure" or yn == "okay" or yn == "Ok" or yn == "Sure":
            ask = False
            run = True

        # If user's answer is no, exit the program.   
        elif yn == "n" or yn == "N" or yn == "No" or yn == "no" or yn == "Nope" or yn == "nope":
            ask = False
            run = False

        # If the user's answer is anything else, ask the question again.
        else:
            print('''Sorry that answer was invalid, Type "y" to repeat or "n" to exit''')
            ask = True
            run = True
        
        
