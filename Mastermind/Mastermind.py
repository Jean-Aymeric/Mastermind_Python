import random
from constant import *

secretCode = [ 0 ] * CODE_SIZE

def chooseSecretCode() :
    for i in range( CODE_SIZE ) :
        secretCode[i] = random.randint( 0, NB_COLORS - 1 )

def analyseProposition( proposition ) :
    return True

def askProposition() :
    proposition = [-1] * CODE_SIZE
    print("Entrez votre proposition de code : ")
    print("Appuyez sur ENTREE après chaque nombre.")
    print ("Chaque nombre doit être inférieur à " + str(NB_COLORS))
    for i in range( CODE_SIZE ) :
       while ((proposition[i] >= NB_COLORS) or (proposition[i] < 0)) :
           proposition[i] = int(input ("Nombre " + str(i + 1) + " : "))
 
    return proposition

def gameLoop() :
    chooseSecretCode()
    codeFound = False
    while (not codeFound) :
        proposition = askProposition()
        if (analyseProposition( proposition ) == True) :
            codeFound = True

gameLoop()