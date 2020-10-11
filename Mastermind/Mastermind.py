import random
from constant import *

secretCode = [ 0 ] * CODE_SIZE

def chooseSecretCode() :
    for i in range( CODE_SIZE ) :
        secretCode[i] = random.randint( 0, NB_COLORS - 1 )

chooseSecretCode()
print(secretCode)