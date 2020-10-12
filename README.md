# Mastermind_Python

## Step 1
+ Faire un programme qui choisi un code secret
+ Le code secret est constitué d’une suite de nombres
+ Le nombre de nombres constituant le code secret doit être paramétrable dans le programme
+ L’amplitude des nombres constituant le code secret doit être paramétrable

## Step 2
+ Ajouter une fonction de GameLoop au programme
  - Une fonction GameLoop est une boucle qui lance la mécanique du jeu
  - La boucle ne s’arrête que lorsque le jeu est terminé
+ Ajouter une fonction de demande de proposition
  - La fonction doit demander à l’utilisateur le bon nombre de nombres
  - La fonction doit vérifier que les nombres sont dans la bonne amplitude
+ Ajouter une fonction d’analyse de la proposition
  - La fonction renvoie pour le moment toujours Vrai

## Step 3
+ Implémenter la fonction d’analyse
  - Pour le moment seule l’égalité est testée
+ Ajouter une fonction d’affichage lorsque le joueur gagne

## Step 4
+ Implémenter la fonction d’analyse
  - La fonction compte le nombre de nombres bien placés
+ Ajouter une fonction affichant le résultat de l’analyse

## Step 5
+ Implémenter la fonction d’analyse
  - La fonction compte le nombre de nombres corrects mais mal placés
  - Si un nombre est proposé plusieurs fois, la fonction compte juste chacune des proposition
  - Si un nombre est présent plusieurs fois dans le code, la proposition n’est comptée bonne qu’une seule fois
  - Si un nombre est bien placé, il n’est pas compté comme mal placé
+ Modifier la fonction d’affichage des résultats d’analyse

## Step 6
+ Implémenter la fonction d’analyse
  - Si un nombre est présent plusieurs fois dans le code, la proposition mal placée n’est comptée qu’une seule fois, sauf si le nombre est proposé plusieurs fois.

