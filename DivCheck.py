'''
Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

def divBySeven():
    """
    This Function will search through all numbers between 2000 to 3000 and divide 
    by 7 and if there is a remainder it is divisible by 7. Then I will do the same 
    for 5.
    This will be put in a list the printed at the end """
    n = []
    for i in  range(2000, 3001):
        if i % 7 == 0:
            if not i % 5 == 0:
                n.append(i)
    print(n)
        
divBySeven()