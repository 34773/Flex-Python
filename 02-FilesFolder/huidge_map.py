import os

Creatie = True

while Creatie:
 mapnaam = input("Voer in:")
 lengte_mapnaam = len(mapnaam)

 if lengte_mapnaam >0:
    os.mkdir(mapnaam)
    print("Map genaamd " + mapnaam + " is aangemaakt")

    Creatie = False 
    
 else:
    print("Voer een mapnaam in.")