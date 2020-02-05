from mqtt_base import *
from reset_agent import reset_agent
from teleport_agent import teleport_agent
from weather import change_weather
from polution import change_polution
from road import *

from time import sleep

def snow():
    change_weather("snow")

def rain():
    change_weather("rain")

def heat():
    change_weather("heat wave")

def polution_normal():
    change_polution("normal")

def polution_normal():
    change_polution("pollution peak")


def start_aeroport():
    reset_agent()
    teleport_agent("walk", (20,2))


def little_smow_storm():
    reset_agent()
    change_weather("snow")
    sleep(7)
    change_weather("normal")


def close_some_road():


    car_a = Road("edge_54", "close")
    car_b = Road("edge_56", "close")
    list_car = [car_a,car_b]

    bike_a = Road("edge_12", "close")
    bike_b = Road("edge_14", "close")
    list_bike = [bike_a,bike_b]


    walk_a = Road("edge_32", "close")
    walk_b = Road("edge_34", "close")
    list_walk = [walk_a, walk_b]

    change_road(list_car, list_bike, list_walk)




