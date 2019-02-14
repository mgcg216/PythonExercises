"""
Write a program to solve a classic ancient Chinese puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
How many rabbits and how many chickens do we have?
"""

def ChinPuz():
    """
    This function will check all posible combination of chickens and rabbits
    First it will 35 chickens the 34 chickens and 1 rabbit etc. At each iteration
    I will check if the legs match up """
    c = 2 # number of chicken legs
    r = 4 # number of rabbit legs
    headNum = 35
    legNum = 94
    for i in range(0, headNum + 1):
        rabbit = i 
        chicken = (headNum - i)
        legs = rabbit * r + chicken * c
        if legs == legNum:
            print("Rabbits: ", rabbit)
            print("Chickens: ", chicken)
        
ChinPuz()