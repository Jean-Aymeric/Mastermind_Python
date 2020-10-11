import random
from constant import *

secretCode = [ 0 ] * CODE_SIZE

def chooseSecretCode() :
    for i in range( CODE_SIZE ) :
        secretCode[i] = random.randint( 0, NB_COLORS - 1 )

def analyseProposition( proposition ) :
    return True

def askProposition() :
    proposition = [0] * CODE_SIZE
    print("Entrez votre proposition de code : ")
    print("Appuyez sur ENTREE après chaque nombre.")
    for i in range( CODE_SIZE ) :
        proposition[i] = input ("Nombre " + str(i + 1) + " : ")

def gameLoop() :
    chooseSecretCode()
    codeFound = False
    while (not codeFound) :
        proposition = askProposition()
        if (analyseProposition( proposition ) == True) :
            codeFound = True

gameLoop()