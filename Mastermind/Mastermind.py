import random
from constant import *

secretCode = [ 0 ] * CODE_SIZE

def chooseSecretCode() :
    for i in range( CODE_SIZE ) :
        secretCode[i] = random.randint( 0, NB_COLORS - 1 )
    print( secretCode )

def analyseProposition( proposition ) :
    analyseResult = [ 0, 0 ]
    for i in range( CODE_SIZE ) :
        if (proposition[i] == secretCode[i]) :
            analyseResult[0] += 1
    for i in range( CODE_SIZE ) :
        alreadyFound = False
        for j in range( CODE_SIZE ) :
             if ((proposition[i] == secretCode[j]) and not alreadyFound) :
                 analyseResult[1] += 1
                 alreadyFound = True
    analyseResult[1] -= analyseResult[0]
    return analyseResult

def showAnalyseResult( analyseResult ) :
    print( "Nombres bien placés : " + str( analyseResult[0] ) )
    print( "Nombres mal placés  : " + str( analyseResult[1] ) )

def askProposition() :
    proposition = [ -1 ] * CODE_SIZE
    print( "\nEntrez votre proposition de code : " )
    print( "Appuyez sur ENTREE après chaque nombre." )
    print( "Chaque nombre doit être inférieur à " + str( NB_COLORS ) )
    for i in range( CODE_SIZE ) :
       while ((proposition[i] >= NB_COLORS) or (proposition[i] < 0)) :
           proposition[i] = int( input( "Nombre " + str( i + 1 ) + " : " ) )
 
    return proposition

def gameLoop() :
    chooseSecretCode()
    codeFound = False
    while (not codeFound) :
        proposition = askProposition()
        analyseResult = analyseProposition( proposition )
        showAnalyseResult( analyseResult )
        if (analyseResult[0] == CODE_SIZE) :
            codeFound = True

def showGameWin() :
    print( "-----------------------------" )
    print( "| Vous avez gagné ! Bravo ! |" )
    print( "-----------------------------" )
gameLoop()
showGameWin()