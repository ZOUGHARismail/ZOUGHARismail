from sys import path
from os import system
#path.append("C:\\Users\\ACER\\Desktop\\Tsdi1\\ismail\\python\\modules")   
path.append(".\\modules")  #this is for all user
import pack.fonction as tl
choix =0
notes=[]
while choix !=13:
    system("cls") 
    choix=int(input("\n1. Saisir\n2. Afficher\n3. Somme\n"+
    "4. Tri Croissant\n5. Inverser\n6. Max\n7. Admis\n8. NonAdmis\n9. Max\n10. Min\n11. Enregistrer\n12. Charger\n13. Quitter\nTapez votre choix ? "))
    if choix==1:
        n=int(input("Combien de notes voulez vous saisir ? "))
        tl.saisir(notes,n)
        
    elif choix==2:
        tl.afficherVertical(notes)
        system("pause")
        
    elif choix==3:
        print("La somme est :",tl.somme(notes))
        system("pause")
        
    elif choix==4:
       tl.triCroissant(notes)
       #notes.sort()
       tl.afficherVertical(notes)
       system("pause")
       
    elif choix==5:
       #tl.inverser(notes)
       notes=notes[::-1]
       tl.afficherVertical(notes)
       system("pause")
          
    elif choix==6:
        print("La plus grande note de la liste est :",tl.getMax(notes))
        system("pause")
    elif choix==7:
        tl.afficherHoris(tl.getAdmis(notes))
        system("pause")
    elif choix==8:
        tl.afficherHoris(tl.getNonAdmis(notes))
        system("pause")
    elif choix==9:
        print("max=",tl.getMax(notes))
        system(("pause"))
    elif choix==10:
        print("min",tl.getMin(notes))
    elif choix==11:
        tl.enregistrer(notes)
    elif choix==12:
        notes=tl.charger()
        tl.afficherVertical(notes)
        system("pause")