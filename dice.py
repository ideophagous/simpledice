"""
A simple dice roll simulator
"""

from random import randint

DICE_MIN = 1
DICE_MAX = 6
N_TRIALS = 100000

def get_random():
    """
    Returns a random integer n where DICE_MIN <= n <= DICE_MAX
    """
    return randint(DICE_MIN,DICE_MAX)
    
def check_uniformity():
    """
    Checks if our dice follows a uniform probability distribution
    The list of values should be close enough to each other
    """
    size = DICE_MAX-DICE_MIN+1
    values = [0]*size
    for i in range(N_TRIALS):
        values[get_random()-1]+=1
    for x in range(size):
        values[x] = values[x]/(N_TRIALS+0.0)
    print(values)



if __name__=='__main__':
    #check_uniformity()
    confirm = 'Y'
    counter = 1
    while confirm=="Y":
        confirm = ""
        print("Dice roll "+str(counter)+': '+str(get_random()))
        while confirm not in ["Y","N"]:
            confirm = input("Roll dice once more? Y/N ")
        counter+=1
