import random
from constant import *

secretCode = [ 0 ] * CODE_SIZE

def chooseSecretCode() :
    for i in range( CODE_SIZE ) :
        secretCode[i] = random.randint( 0, NB_COLORS - 1 )
    print( secretCode )

def analyseProposition( proposition ) :
    analyseResult = [ 0, 0 ]
    secretCodeAnalyse = [ False ] * CODE_SIZE
    propositionAnalyse = [ False ] * CODE_SIZE
    for i in range( CODE_SIZE ) :
        if (proposition[i] == secretCode[i]) :
            analyseResult[0] += 1
            secretCodeAnalyse[i] = True
            propositionAnalyse[i] = True
    for i in range( CODE_SIZE ) :
        for j in range( CODE_SIZE ) :
             if ((proposition[i] == secretCode[j]) and not secretCodeAnalyse[j] and not propositionAnalyse[i]) :
                 analyseResult[1] += 1
                 secretCodeAnalyse[j] = True
                 propositionAnalyse[i] = True
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