from GameMaster import *

def help():
    print("List des Commandes \n\
          hard1 = Lance le test hard1 \n\
          hard2 = Lance le test hard2 \n\
          hard3 = Lance le test hard3 \n\
          hard4 = Lance le test hard4 \n\
          help = Affiche la liste des commande \n\
          snow = Change le climat en neige \n\
          rain = Change le climat en pluit \n\
          polution = Change la polution en pic éleve \n\
          aer = Téléporte à l'aéroport \n\
          sworm = Provoque une tempête \n\
          open_all_car = ouvre toutes les route au car\n\
          close_all_car = ferme toutes les route au car\n\
          open_all = ouvre les route fermee\n\
          open_all_sub = ouvre les metros\n\
          close_all_sub = ferme les metros\n\
          reset = Téléporte l'Agent en {0,0}")

def parse_command(command : str):
    if (command == "hard1"):
        hard_test1()
    elif (command == "hard2"):
        hard_test2()
    elif (command == "hard3"):
        hard_test3()
    elif (command == "hard4"):
        hard_test4()
    elif (command == "help"):
        help()
    elif (command == "snow"):
        snow()
    elif (command == "rain"):
        rain()
    elif (command == "polution"):
        polution_eleve()
    elif (command == "aer"):
        start_airport()
    elif (command == "sworm"):
        little_snow_storm()
    elif (command == "open_all"):
        open_all()
    elif command == 'open_all_sub':
        interact_all_subway("open")

    elif command == 'close_all_sub':
        interact_all_subway("close")

    elif command == 'open_all_car':
        interact_all_road_car("open")

    elif command == 'close_all_car':
        interact_all_road_car("close")

    elif (command == "reset"):
        reset()
    else:
      print("Commande not Found: please enter \"help\" for see commande")

def shell():
  a = input(">")
  while a != "exit":
    parse_command(a)
    a = input(">")

shell()
