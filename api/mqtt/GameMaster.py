from reset_agent import reset_agent
from teleport_agent import teleport_agent
from weather import change_weather
from polution import change_polution
from road import *
from subway_lines import subway_lines

from time import sleep


def close_some_road(close : str):
    car_a = Road("edge_54", close)
    car_b = Road("edge_56", close)
    list_car = [car_a,car_b]
    bike_a = Road("edge_12", close)
    bike_b = Road("edge_14", close)
    list_bike = [bike_a,bike_b]
    walk_a = Road("edge_32", close)
    walk_b = Road("edge_34", close)
    list_walk = [walk_a, walk_b]
    change_road(list_car, list_bike, list_walk)


def close_some_subway(close : str):
    list_line = ["edge_6","edge_7","edge_12"]
    list_status = [close, close, close]
    subway_lines(list_line, list_status)


def interact_all_subway(status : str):
    list_line = []
    list_status = []
    for i in range(30):
        line = "edge_" + str(i)
        list_line.append(line)
        list_status.append(status)
    subway_lines(list_line, list_status)


def reset():
    reset_agent()


def snow():
    change_weather("snow")


def rain():
    change_weather("rain")


def heat():
    change_weather("heat wave")


def pollution_normal():
    change_polution("normal")


def polution_eleve():
    change_polution("pollution peak")


def start_airport():
    reset_agent()
    teleport_agent("walk", (20, 2))


def little_snow_storm():
    reset_agent()
    change_weather("snow")
    sleep(7)
    change_weather("normal")


def hard_test1():
    rain()
    close_some_road("close")
    close_some_subway("close")


def hard_test2():
    polution_eleve()
    close_some_road()
    close_some_subway()


def hard_test3():
    rain()
    close_some_road("close")
    close_some_subway("close")
    sleep(3)
    change_weather("normal")
    sleep(2)
    close_some_road("open")
    close_some_subway("open")


def hard_test4():
    start_airport()
    polution_eleve()
    # fermer la route de l'aeroport.
    rain()


def open_all():
    close_some_road("open")
    close_some_subway("open")




