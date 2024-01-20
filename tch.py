import math
from collections import deque

# Discount is 20%
discount = 0.2

# This array will contain the public transports
transports = []

# This array will contain the walk paths from location to location (station to station)
walks = []

class Transport:
  def __init__(
    self,
    name,
    stations,
    distances,
    fare_matrix = None,
    fare_matrix_sv = None,
    fare_function = None,
    two_way = False,
    discountable = False
  ):
    self.name = name
    self.stations = stations
    self.distances = distances

    if fare_matrix:
      self.fare_matrix = fare_matrix

    if fare_matrix_sv:
      self.fare_matrix_sv = fare_matrix_sv

    if fare_function:
      self.fare_function = fare_function

    self.two_way = two_way
    self.discountable = discountable

    transports.append(self)

class Walk:
  def __init__(self, trails):
    self.trails = trails

    walks.append(self)

# EDSA Carousel North Bound

edsa_carousel_north_bound = Transport(
  name = "EDSA Carousel",
  stations = [
    "PITX",
    "City of Dreams",
    "DFA",
    "Roxas Boulevard",
    "Taft Avenue",
    "Ayala",
    "Buendia",
    "Guadalupe",
    "Ortigas",
    "Santolan Annapolis",
    "Main Avenue",
    "Q-Mart",
    "Quezon Avenue",
    "North Avenue",
    "Roosevelt",
    "Kaingin",
    "Balintawak",
    "Bagong Barrio",
    "Monumento"
  ],
  distances = [2.4, 2.9, 1.1, 0.8, 4.6, 1.0, 1.9, 2.4, 2.4, 0.9, 2.6, 2.6, 1.7, 1.2, 1.0, 0.9, 0.8, 1.2],
  fare_matrix = [
    [   -1, 15.00, 15.00, 15.00, 15.00, 24.00, 26.50, 31.50, 38.00, 44.75, 46.50, 51.25, 55.50, 59.00, 63.50, 65.75, 67.75, 69.50, 73.00],
    [   -1,    -1, 15.00, 15.00, 15.00, 17.75, 20.00, 25.00, 31.50, 38.25, 40.00, 44.75, 49.00, 52.50, 57.00, 59.25, 61.25, 63.25, 66.50],
    [   -1,    -1,    -1, 15.00, 15.00, 16.25, 18.50, 23.75, 30.25, 36.75, 38.75, 43.50, 47.75, 51.00, 55.50, 58.00, 60.00, 61.75, 65.25],
    [   -1,    -1,    -1,    -1, 15.00, 15.00, 15.75, 21.00, 27.50, 34.25, 36.00, 40.75, 45.00, 48.50, 53.00, 55.25, 57.25, 59.00, 62.50],
    [   -1,    -1,    -1,    -1,    -1, 15.00, 15.00, 18.75, 25.25, 31.75, 33.75, 38.50, 42.75, 46.00, 50.50, 53.00, 55.00, 56.75, 60.25],
    [   -1,    -1,    -1,    -1,    -1,    -1, 15.00, 15.00, 15.50, 22.25, 24.00, 29.00, 33.25, 36.50, 41.00, 43.50, 45.25, 47.25, 50.50],
    [   -1,    -1,    -1,    -1,    -1,    -1,    -1, 15.00, 15.00, 20.00, 21.75, 26.50, 30.75, 34.25, 38.75, 41.25, 43.00, 45.00, 48.25],
    [   -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1, 15.00, 15.00, 16.75, 21.50, 25.75, 29.00, 33.75, 36.00, 38.00, 39.75, 43.25],
    [   -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1, 15.00, 15.00, 15.00, 19.25, 22.75, 27.25, 29.50, 31.50, 33.25, 36.75],
    [   -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1, 15.00, 15.00, 15.00, 16.00, 20.50, 22.75, 24.75, 26.75, 30.00],
    [   -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1, 15.00, 15.00, 15.00, 18.75, 21.00, 23.00, 25.00, 28.25],
    [   -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1, 15.00, 15.00, 15.00, 16.25, 18.25, 20.00, 23.50],
    [   -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1, 15.00, 15.00, 15.00, 15.00, 15.75, 19.25],
    [   -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1, 15.00, 15.00, 15.00, 15.00, 15.75],
    [   -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1, 15.00, 15.00, 15.00, 15.00],
    [   -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1, 15.00, 15.00, 15.00],
    [   -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1, 15.00, 15.00],
    [   -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1, 15.00],
    [   -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1]
  ],
  discountable = True
)

# EDSA Carousel South Bound

edsa_carousel_south_bound = Transport(
  name = "EDSA Carousel",
  stations = [
    "Monumento",
    "Bagong Barrio",
    "Balintawak",
    "Kaingin",
    "Roosevelt",
    "North Avenue",
    "Quezon Avenue",
    "Q-Mart",
    "Main Avenue",
    "Santolan Annapolis",
    "Ortigas",
    "Guadalupe",
    "Buendia",
    "Ayala",
    "Tramo",
    "Taft Avenue",
    "Roxas Boulevard",
    "MoA",
    "DFA",
    "Ayala Malls Manila Bay",
    "PITX"
  ],
  distances = [1.2, 0.8, 0.9, 1.0, 1.2, 1.7, 2.6, 2.6, 0.9, 2.4, 2.4, 1.9, 1.0, 4.2, 0.45, 4.6, 1.3, 1.4, 0.7, 2.3],
  fare_matrix = [
    [   -1, 15.00, 15.00, 15.00, 15.00, 15.75, 19.25, 23.50, 28.00, 29.75, 36.50, 42.75, 48.00, 50.25, 58.75, 59.50, 62.00, 64.25, 68.00, 71.75, 75.50],
    [   -1,    -1, 15.00, 15.00, 15.00, 15.00, 15.75, 20.00, 24.50, 26.25, 33.00, 39.50, 44.75, 47.00, 55.25, 56.25, 58.50, 61.00, 64.75, 66.75, 70.50],
    [   -1,    -1,    -1, 15.00, 15.00, 15.00, 15.00, 18.25, 22.75, 24.50, 31.25, 37.50, 42.75, 45.00, 53.50, 54.25, 56.75, 59.00, 62.75, 65.00, 68.75],
    [   -1,    -1,    -1,    -1, 15.00, 15.00, 15.00, 16.25, 20.75, 22.50, 29.25, 35.75, 40.75, 43.25, 51.50, 52.50, 54.75, 57.25, 60.75, 63.00, 66.75],
    [   -1,    -1,    -1,    -1,    -1, 15.00, 15.00, 15.00, 18.50, 20.25, 27.00, 33.25, 38.50, 40.75, 49.25, 50.00, 52.50, 54.75, 58.50, 60.75, 64.50],
    [   -1,    -1,    -1,    -1,    -1,    -1, 15.00, 15.00, 15.00, 15.75, 22.50, 28.75, 34.00, 36.25, 44.75, 45.50, 48.00, 50.25, 54.00, 56.25, 60.00],
    [   -1,    -1,    -1,    -1,    -1,    -1,    -1, 15.00, 15.00, 15.00, 19.00, 25.50, 30.75, 33.00, 41.25, 42.25, 44.50, 47.00, 50.50, 52.75, 56.50],
    [   -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1, 15.00, 15.00, 15.00, 21.00, 26.25, 28.50, 37.00, 38.00, 40.25, 42.75, 46.25, 48.50, 52.25],
    [   -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1, 15.00, 15.00, 15.00, 20.00, 22.25, 30.75, 31.50, 34.00, 36.25, 40.00, 42.25, 46.00],
    [   -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1, 15.00, 15.00, 15.00, 15.75, 24.00, 25.00, 27.25, 29.75, 33.25, 35.50, 39.25],
    [   -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1, 15.00, 15.00, 15.00, 17.50, 18.50, 20.75, 23.25, 27.00, 29.00, 33.00],
    [   -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1, 15.00, 15.00, 15.00, 15.00, 15.50, 18.00, 21.75, 23.75, 27.75],
    [   -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1, 15.00, 15.00, 15.00, 15.00, 15.75, 19.50, 21.50, 25.50],
    [   -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1, 15.00, 15.00, 15.00, 15.00, 15.00, 15.00, 17.00],
    [   -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1, 15.00, 15.00, 15.00, 15.00, 15.00, 16.00],
    [   -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1, 15.00, 15.00, 15.00, 15.00, 15.00],
    [   -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1, 15.00, 15.00, 15.00, 15.00],
    [   -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1, 15.00, 15.00, 15.00],
    [   -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1, 15.00, 15.00],
    [   -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1, 15.00],
    [   -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1]
  ],
  discountable = True
)

# LRT-1

lrt1 = Transport(
  name = "LRT1",
  stations = [
    "Baclaran",
    "EDSA",
    "Libertad",
    "Gil Puyat",
    "Vito Cruz",
    "Quirino",
    "Pedro Gil",
    "UN Avenue",
    "Central",
    "Carriedo",
    "Doroteo Jose",
    "Bambang",
    "Tayuman",
    "Blumentritt",
    "Abad Santos",
    "R. Papa",
    "5th Avenue",
    "Monumento",
    "Balintawak",
    "Roosevelt"
  ],
  distances = [0.65, 1.0, 0.75, 1.0, 0.8, 0.75, 0.7, 1.2, 1.5, 0.65, 0.6, 0.6, 0.75, 1.1, 0.65, 0.9, 1.1, 2.3, 2.0],
  fare_matrix = [
    [-1, 15, 15, 20, 20, 20, 20, 20, 25, 25, 25, 25, 25, 30, 30, 30, 30, 30, 35, 35],
    [15, -1, 15, 15, 20, 20, 20, 20, 25, 25, 25, 25, 25, 25, 30, 30, 30, 30, 35, 35],
    [15, 15, -1, 15, 15, 20, 20, 20, 20, 25, 25, 25, 25, 25, 25, 30, 30, 30, 35, 35],
    [20, 15, 15, -1, 15, 20, 20, 20, 20, 20, 25, 25, 25, 25, 25, 25, 30, 30, 30, 35],
    [20, 20, 15, 15, -1, 15, 15, 20, 20, 20, 20, 20, 25, 25, 25, 25, 25, 30, 30, 35],
    [20, 20, 20, 20, 15, -1, 15, 15, 20, 20, 20, 20, 20, 25, 25, 25, 25, 25, 30, 30],
    [20, 20, 20, 20, 15, 15, -1, 15, 20, 20, 20, 20, 20, 20, 25, 25, 25, 25, 30, 30],
    [20, 20, 20, 20, 20, 15, 15, -1, 15, 20, 20, 20, 20, 20, 20, 25, 25, 25, 30, 30],
    [25, 25, 20, 20, 20, 20, 20, 15, -1, 15, 15, 20, 20, 20, 20, 20, 20, 25, 25, 30],
    [25, 25, 25, 20, 20, 20, 20, 20, 15, -1, 15, 15, 20, 20, 20, 20, 20, 25, 25, 30],
    [25, 25, 25, 25, 20, 20, 20, 20, 15, 15, -1, 15, 15, 20, 20, 20, 20, 20, 25, 25],
    [25, 25, 25, 25, 20, 20, 20, 20, 20, 15, 15, -1, 15, 15, 20, 20, 20, 20, 25, 25],
    [25, 25, 25, 25, 25, 20, 20, 20, 20, 20, 15, 15, -1, 15, 15, 20, 20, 20, 25, 25],
    [30, 25, 25, 25, 25, 25, 20, 20, 20, 20, 20, 15, 15, -1, 15, 15, 20, 20, 20, 25],
    [30, 30, 25, 25, 25, 25, 25, 20, 20, 20, 20, 20, 15, 15, -1, 15, 15, 20, 20, 25],
    [30, 30, 30, 25, 25, 25, 25, 25, 20, 20, 20, 20, 20, 15, 15, -1, 15, 20, 20, 25],
    [30, 30, 30, 30, 25, 25, 25, 25, 20, 20, 20, 20, 20, 20, 15, 15, -1, 15, 20, 20],
    [30, 30, 30, 30, 30, 25, 25, 25, 25, 25, 20, 20, 20, 20, 20, 20, 15, -1, 20, 20],
    [35, 35, 35, 30, 30, 30, 30, 30, 25, 25, 25, 25, 25, 20, 20, 20, 20, 20, -1, 20],
    [35, 35, 35, 35, 35, 30, 30, 30, 30, 30, 25, 25, 25, 25, 25, 25, 20, 20, 20, -1]
  ],
  fare_matrix_sv = [ # Fare matrix for stored value cards
    [13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 23, 24, 25, 26, 27, 28, 29, 30, 33, 35],
    [14, 13, 15, 15, 17, 18, 19, 20, 21, 22, 23, 24, 24, 25, 26, 27, 28, 29, 32, 34],
    [15, 15, 13, 14, 15, 16, 17, 18, 20, 21, 22, 22, 23, 24, 25, 26, 27, 28, 31, 33],
    [16, 15, 14, 13, 15, 16, 17, 17, 19, 20, 21, 21, 22, 23, 24, 25, 26, 27, 30, 32],
    [17, 17, 15, 15, 13, 14, 15, 16, 18, 19, 19, 20, 21, 22, 23, 24, 25, 26, 29, 31],
    [18, 18, 16, 16, 14, 13, 14, 15, 17, 18, 18, 19, 20, 21, 22, 23, 24, 25, 28, 30],
    [19, 19, 17, 17, 15, 14, 13, 14, 16, 17, 17, 18, 19, 20, 21, 22, 23, 24, 27, 29],
    [20, 20, 18, 17, 16, 15, 14, 13, 15, 16, 16, 17, 18, 19, 20, 21, 22, 23, 26, 28],
    [22, 21, 20, 19, 18, 17, 16, 15, 13, 14, 15, 16, 17, 17, 18, 19, 20, 22, 24, 27],
    [23, 22, 21, 20, 19, 18, 17, 16, 14, 13, 14, 15, 16, 16, 18, 18, 20, 21, 24, 26],
    [23, 23, 22, 21, 19, 18, 17, 16, 15, 14, 13, 14, 15, 16, 17, 18, 19, 20, 23, 25],
    [24, 24, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 14, 15, 16, 17, 18, 19, 22, 24],
    [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 14, 15, 16, 17, 18, 21, 23],
    [26, 25, 24, 23, 22, 21, 20, 19, 17, 16, 16, 15, 14, 13, 14, 15, 16, 18, 20, 23],
    [27, 26, 25, 24, 23, 22, 21, 20, 18, 18, 17, 16, 15, 14, 13, 14, 15, 17, 19, 22],
    [28, 27, 26, 25, 24, 23, 22, 21, 19, 18, 19, 17, 16, 15, 14, 13, 14, 16, 18, 21],
    [29, 28, 27, 26, 25, 24, 23, 22, 20, 20, 19, 18, 17, 16, 15, 14, 13, 15, 17, 20],
    [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 18, 17, 16, 15, 13, 16, 18],
    [33, 32, 31, 30, 29, 28, 27, 26, 24, 24, 23, 22, 21, 20, 19, 18, 17, 16, 13, 16],
    [35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 23, 22, 21, 20, 18, 16, 13]
  ]
)

# LRT-2

lrt2 = Transport(
  name = "LRT2",
  stations = [
    "Recto",
    "Legarda",
    "Pureza",
    "V. Mapa",
    "J. Ruiz",
    "Gilmore",
    "Betty Go-Belmonte",
    "Araneta Cubao",
    "Anonas",
    "Katipunan",
    "Santolan",
    "Marikina-Pasig",
    "Antipolo"
  ],
  distances = [1.1, 1.4, 1.4, 1.2, 0.9, 1.1, 1.2, 1.4, 1.0, 2.0, 1.8, 2.4],
  fare_matrix = [
    [-1, 15, 20, 20, 20, 25, 25, 25, 25, 30, 30, 35, 35],
    [15, -1, 15, 20, 20, 20, 25, 25, 25, 25, 30, 30, 35],
    [20, 15, -1, 15, 20, 20, 20, 20, 25, 25, 30, 30, 30],
    [20, 20, 15, -1, 15, 20, 20, 20, 20, 25, 25, 30, 30],
    [20, 20, 20, 15, -1, 15, 20, 20, 20, 20, 25, 25, 30],
    [25, 20, 20, 20, 15, -1, 15, 20, 20, 20, 25, 25, 30],
    [25, 25, 20, 20, 20, 15, -1, 15, 20, 20, 20, 25, 25],
    [25, 25, 20, 20, 20, 20, 15, -1, 15, 20, 20, 25, 25],
    [25, 25, 25, 20, 20, 20, 20, 15, -1, 15, 20, 20, 25],
    [30, 25, 25, 25, 20, 20, 20, 20, 15, -1, 20, 20, 25],
    [30, 30, 30, 25, 25, 25, 20, 20, 20, 20, -1, 15, 20],
    [35, 30, 30, 30, 25, 25, 25, 25, 20, 20, 15, -1, 20],
    [35, 35, 30, 30, 30, 30, 25, 25, 25 ,25 ,20, 20 ,-1]
  ],
  fare_matrix_sv = [ # Fare matrix for stored value cards
    [13, 15, 16, 18, 19, 21, 22, 23, 25, 26, 28, 31, 33],
    [15, 13, 15, 17, 18, 19, 21, 22, 24, 25, 27, 29, 32],
    [16, 15, 13, 15, 16, 18, 19, 20, 22, 23, 26, 28, 30],
    [18, 17, 15, 13, 15, 16, 17, 19, 20, 22, 24, 26, 29],
    [19, 18, 16, 15, 13, 14, 16, 17, 19, 20, 22, 24, 27],
    [21, 19, 18, 16, 14, 13, 15, 16, 18, 19, 21, 23, 26],
    [22, 21, 19, 17, 16, 15, 13, 15, 16, 18, 20, 22, 25],
    [23, 22, 20, 19, 17, 16, 15, 13, 15, 16, 19, 21, 23],
    [25, 24, 22, 20, 19, 18, 16, 15, 13, 14, 17, 19, 22],
    [26, 25, 23, 22, 20, 19, 18, 16, 14, 13, 16, 18, 21],
    [28, 27, 26, 24, 22, 21, 20, 19, 17, 16, 13, 15, 18],
    [31, 29, 28, 26, 24, 23, 22, 21, 19, 18, 15, 13, 16],
    [33, 32, 30, 29, 27, 26, 25, 23, 22, 21, 18, 16, 13]
  ]
)

# MRT-3

mrt3 = Transport(
  name = "MRT3",
  stations = [
    "North Avenue",
    "Quezon Avenue",
    "GMA Kamuning",
    "Araneta Cubao",
    "Santolan Annapolis",
    "Ortigas",
    "Shaw Boulevard",
    "Boni",
    "Guadalupe",
    "Buendia",
    "Ayala",
    "Magallanes",
    "Taft Avenue"
  ],
  distances = [1.2, 1.0, 2.4, 2.2, 2.4, 0.85, 1.0, 0.9, 1.9, 0.9, 3.0, 3.3],
  fare_matrix = [
    [-1, 13, 13, 16, 16, 20, 20, 20, 24, 24, 24, 28, 28],
    [13, -1, 13, 13, 16, 16, 20, 20, 20, 24, 24, 24, 28],
    [13, 13, -1, 13, 13, 16, 16, 20, 20, 20, 24, 24, 24],
    [16, 13, 13, -1, 13, 13, 16, 16, 20, 20, 20, 24, 24],
    [16, 16, 13, 13, -1, 13, 13, 16, 16, 20, 20, 20, 24],
    [20, 16, 16, 13, 13, -1, 13, 13, 16, 16, 20, 20, 20],
    [20, 20, 16, 16, 13, 13, -1, 13, 13, 16, 16, 20, 20],
    [20, 20, 20, 16, 16, 13, 13, -1, 13, 13, 16, 16, 20],
    [24, 20, 20, 20, 16, 16, 13, 13, -1, 13, 13, 16, 16],
    [24, 24, 20, 20, 20, 16, 16, 13, 13, -1, 13, 13, 16],
    [24, 24, 24, 20, 20, 20, 16, 16, 13, 13, -1, 13, 13],
    [28, 24, 24, 24, 20, 20, 20, 16, 16, 13, 13, -1, 13],
    [28, 28, 24, 24, 24, 20, 20, 20, 16, 16, 13, 13, -1]
  ]
)

# Function for calculating jeep fare
# P13 minimum
# + P1 for every kilometer after the first 4 kilometers

def jeep_fare_function(distance):
  if distance <= 4:
    return 13
  else:
    return 13 + (((distance)*1.8) - 4)

jeep_crame_qmart = Transport(
  name = "Jeep (Crame -> Q-Mart)",
  stations = [
    "1st West Crame Road / Road 6",
    "1st West Crame Road / Road 2",
    "1st West Crame Road / Col. Bonny Serrano Avenue",
    "EDSA / Col. Bonny Serrano Avenue",
    "13th Avenue / Col. Bonny Serrano Avenue",
    "13th Avenue / P. Tuazon Boulevard",
    "20th Avenue / P. Tuazon Boulevard",
    "20th Avenue / Aurora Boulevard",
    "Albany / Aurora Boulevard",
    "Albany / Ermin Garcia",
    "New York / Ermin Garcia",
    "Montreal / New York",
    "Montreal / Ermin Garcia"
  ],
  distances = [0.25, 0.27, 0.55, 0.7, 0.85, 0.6, 0.65, 0.27, 0.3, 0.35, 0.65, 0.2],
  fare_function = jeep_fare_function,
  two_way = False,
  discountable = True
)

jeep_qmart_crame = Transport(
  name = "Jeep (Q-Mart -> Crame)",
  stations = [
    "Montreal / Ermin Garcia",
    "Yale / Ermin Garcia",
    "Yale / New York",
    "New York / Ermin Garcia",
    "15th Avenue / Ermin Garcia",
    "15th Avenue / Aurora Boulevard",
		"15th Avenue / P. Tuazon Boulevard",
    "15th Avenue / Col. Bonny Serrano Avenue",
    "EDSA / Col. Bonny Serrano Avenue",
    "1st West Crame Road / Col. Bonny Serrano Avenue",
    "1st West Crame Road / Road 2",
    "Road 7 / Road 2",
    "Road 7 / Road 6",
    "1st West Crame Road / Road 6"
  ],
  distances = [0.55, 0.18, 0.14, 0.096, 0.45, 0.6, 0.9, 0.85, 0.55, 0.27, 0.11, 0.26, 0.12],
  fare_function = jeep_fare_function,
  two_way = False,
  discountable = True
)

jeep_farmers_crame = Transport(
  name = "Jeep (Farmers -> Crame)",
  stations = [
    "Araneta Center Jeepney Terminal",
    "8th Avenue / P. Tuazon Boulevard",
    "9th Avenue / P. Tuazon Boulevard",
    "13th Avenue / P. Tuazon Boulevard",
    "15th Avenue / P. Tuazon Boulevard",
    "15th Avenue / Main Avenue",
    "15th Avenue / Col. Bonny Serrano Avenue",
    "EDSA / Col. Bonny Serrano Avenue",
    "1st West Crame Road / Col. Bonny Serrano Avenue",
    "1st West Crame Road / Road 2",
    "Road 7 / Road 2",
    "Road 7 / Road 6",
    "1st West Crame Road / Road 6"
  ],
  distances = [0.11, 0.08, 0.28, 0.21, 0.4, 0.5, 0.85, 0.55, 0.27, 0.11, 0.26, 0.12],
  fare_function = jeep_fare_function,
  two_way = False,
  discountable = True
)

jeep_recto_malinta = Transport(
  name = "Jeep (Recto <-> Monumento)",
  stations = [
    "Recto",
    "Quezon Boulevard / Fugoso Street",
    "Felix Huertas Road / Fugoso Street",
    "Felix Huertas Road / Lacson Avenue",
    "Yuseco Street / Lacson Avenue",
    "Yuseco Street / Rizal Avenue",
    "Yuseco Street / Tomas Mapua Street",
    "Cavite Street / Tomas Mapua Street",
    "Cavite Street / Bugallon Street",
    "Tecson Street / Bugallon Street",
    "Tecson Street / Abad Santos Avenue",
    "Rizal Avenue / Abad Santos Avenue",
    "R. Papa",
    "5th Avenue",
    "Monumento"
  ],
  distances = [0.65, 0.19, 1.2, 0.15, 0.11, 0.1, 0.55, 0.11, 0.17, 0.18, 0.7, 0.6, 0.95, 1.1],
  fare_function = jeep_fare_function,
  two_way = True,
  discountable = True
)





jeep_cubao = Transport(
  name = "Jeep (Cubao)",
  stations = [
    # ...
    "Anonas",
    "Potsdam / Aurora Boulevard",
    "20th Avenue / Aurora Boulevard",
    "15th Avenue / Aurora Boulevard",
    "Gateway"
  ],
  distances = [0.4, 0.11, 0.4, 0.6],
  fare_function = jeep_fare_function,
  two_way = False,
  discountable = True
)

jeep_cubao = Transport(
  name = "Jeep (Cubao)",
  stations = [
    "Cubao",
    "15th Avenue / Aurora Boulevard",
    "20th Avenue / Aurora Boulevard",
    "T.I.P.",
    "Anonas"
    # ...
  ],
  distances = [0.65, 0.4, 0.11, 0.4],
  fare_function = jeep_fare_function,
  two_way = False,
  discountable = True
)

jeep_taytay_cubao = Transport(
  name = "Jeep (Taytay -> Cubao)",
  stations = [
    "Taytay Bayan",
		"Felix Avenue / Bonifacio Avenue",
		"Rizal Avenue / Bonifacio Avenue",
		"Tropical Hut",
		"Marikina-Pasig",
		"Santolan",
		"Katipunan",
		"Anonas",
		"Ermin Garcia / Aurora Boulevard",
		"Potsdam / Ermin Garcia",
		"Albany / Ermin Garcia",
		"15th Avenue / Ermin Garcia",
		"15th Avenue / Aurora Boulevard",
		"15th Avenue / P. Tuazon Boulevard",
		"13th Avenue / P. Tuazon Boulevard",
		"9th Avenue / P. Tuazon Boulevard",
		"8th Avenue / P. Tuazon Boulevard",
		"8th Avenue / Main Avenue",
		"9th Avenue / Main Avenue",
		"9th Avenue / P. Tuazon Boulevard",
  ],
  distances = [0.85, 2.1, 4.1, 0.16, 1.8, 2.0, 1.0, 0.28, 0.28, 0.35, 0.26, 0.45, 0.6, 0.21, 0.27, 0.073, 0.35, 0.075, 0.3],
  fare_function = jeep_fare_function,
  two_way = False,
  discountable = True
)

jeep_cubao_taytay = Transport(
  name = "Jeep (Cubao -> Taytay)",
  stations = [
		"8th Avenue",
		"8th Avenue / Main Avenue",
		"9th Avenue / Main Avenue",
		"9th Avenue / P. Tuazon Boulevard",
		"13th Avenue / P. Tuazon Boulevard",
		"15th Avenue / P. Tuazon Boulevard",
		"20th Avenue / P. Tuazon Boulevard",
		"20th Avenue / Aurora Boulevard",
		"T.I.P.",
		"Ermin Garcia / Aurora Boulevard",
		"Anonas",
		"Katipunan",
		"Santolan",
		"Marikina-Pasig",
		"Tropical Hut",
		"Rizal Avenue / Bonifacio Avenue",
		"Felix Avenue / Bonifacio Avenue",
    "Taytay Bayan",
  ],
  distances = [0.16, 0.075, 0.35, 0.27, 0.21, 0.4, 0.65, 0.084, 0.12, 0.28, 1.0, 2.0, 1.8, 0.16, 4.1, 2.1, 0.85],
  fare_function = jeep_fare_function,
  two_way = False,
  discountable = True
)


jeep_antipolo_cubao = Transport(
	name = "Jeep (Cubao <-> Antipolo)",
	stations = [
    "Shopwise Antipolo",
    "Robinsons Antipolo",
    "Antipolo",
    "Marikina-Pasig",
    "Santolan",
    "Katipunan",
    "Anonas",
		"Ermin Garcia / Aurora Boulevard",
    "Potsdam / Aurora Boulevard",
    "T.I.P.",
    "20th Avenue / Aurora Boulevard",
    "15th Avenue / Aurora Boulevard",
    "Gateway"
	 ],
	 distances = [1.9, 8.9, 2.4, 1.8, 2.0, 1.0, 0.28, 0.049, 0.084, 0.11, 0.4, 0.6],
	 fare_function = jeep_fare_function,
	 two_way= True,
	 discountable= True
)

jeep_baras_antipolo = Transport(
    name = "Jeep(Baras -> Antipolo)",
    stations = [
        "Baras",
        "Robinsons Antipolo"
        ],
    distances = [18],
    fare_function = jeep_fare_function,
    two_way=  False,
    discountable = True
)

jeep_antipolo_baras = Transport(
    name = "Jeep(Antipolo -> Baras)",
    stations = [
        "Shopwise Antipolo",
        "Baras"
        ],
    distances = [16.3],
    fare_function = jeep_fare_function,
    two_way= False,
    discountable = True
)


# Function for calculating modern jeep fare
# P15 minimum
# + P1 for every kilometer after the first 4 kilometers

def modern_jeep_fare_function(distance):
  if distance <= 4:
    return 15
  else:
    return 15 + (distance - 4)

modern_jeep_alimall = Transport(
  name = "Mordern Jeep (Ali Mall)",
  stations = [
    "Potsdam / Aurora Boulevard",
    "20th Avenue / Aurora Boulevard",
    "20th Avenue / P. Tuazon Boulevard",
    "Ali Mall",
    "Shopwise"
  ],
  distances = [0.13, 0.65, 0.6, 0.45],
  fare_function = jeep_fare_function,
  two_way = False,
  discountable = True
)


tricycle_qmart = Transport(
  name = "Tricycle (Q-Mart)",
  stations = [
    "Q-Mart",
    "Potsdam / Aurora Boulevard"
  ],
  distances = [1.8],
  fare_matrix = [
    [-1, 45],
    [-1, -1]
  ]
)


jeep_bulacan = Transport(
    name = "Jeep (Bulacan)",
    stations = [
        "SM San Jose Del Monte",
        "15th Avenue / Aurora Boulevard",
    ],
    distances = [26.8],
    fare_matrix = [
        [-1, 56],
        [56,-1]
    ]
)




# Walks between points and stations
# trail: [ point1, point2, distance]

walk_cubao = Walk(
  trails = [
    ["LRT2 - Araneta Cubao", "MRT3 - Araneta Cubao", 0.55],
    ["LRT2 - Araneta Cubao", "Jeep (Cubao) - Cubao", 0.02],
    ["Jeep (Cubao) - Gateway", "Jeep (Cubao) - Cubao", 0.066],
    ["EDSA Carousel - Main Avenue", "EDSA / Main Avenue", 0.07],
    ["EDSA Carousel - Main Avenue", "EDSA / P. Tuazon Boulevard", 0.24],
    ["MRT3 - Araneta Cubao", "EDSA / P. Tuazon Boulevard", 0.4],
    ["MRT3 - Araneta Cubao", "EDSA / Aurora Boulevard", 0.25],
    ["EDSA / Aurora Boulevard", "EDSA Carousel - Q-Mart", 1],
    ["Jeep (Crame -> Q-Mart) - 20th Avenue / Aurora Boulevard", "T.I.P.", 0.083],
    ["Jeep (Crame -> Q-Mart) - EDSA / Col. Bonny Serrano Avenue", "EDSA / Main Avenue", 0.35],
    ["Jeep (Crame -> Q-Mart) - Montreal / Ermin Garcia", "EDSA / Aurora Boulevard", 0.95],
    ["Jeep (Crame -> Q-Mart) - Montreal / Ermin Garcia", "EDSA Carousel - Q-Mart", 0.18],
    ["Jeep (Crame -> Q-Mart) - Montreal / Ermin Garcia", "Tricycle (Q-Mart) - Q-Mart", 0.001],
    ["Jeep (Crame -> Q-Mart) - Montreal / Ermin Garcia", "Jeep (Q-Mart -> Crame) - Montreal / Ermin Garcia", 0.001],
    ["Mordern Jeep (Ali Mall) - Ali Mall", "13th Avenue / P. Tuazon Boulevard", 0.001],
    ["Mordern Jeep (Ali Mall) - Shopwise", "13th Avenue / P. Tuazon Boulevard", 0.5],
    ["Mordern Jeep (Ali Mall) - Shopwise", "LRT2 - Araneta Cubao", 0.45],
    ["8th Avenue / P. Tuazon Boulevard", "EDSA / P. Tuazon Boulevard", 0.3],
    ["8th Avenue / P. Tuazon Boulevard", "13th Avenue / P. Tuazon Boulevard", 0.35],
    ["T.I.P.", "15th Avenue", .45]
  ]
)

walk_recto = Walk(
  trails = [
    ["LRT1 - Doroteo Jose", "LRT2 - Recto", 0.35],
    ["Jeep (Recto <-> Monumento) - Recto", "LRT2 - Recto", 0.22]
  ]
)

walk_monumento = Walk(
  trails = [
    ["Jeep (Recto <-> Monumento) - Monumento", "EDSA Carousel - Monumento", 0.6],
    ["Jeep (Recto <-> Monumento) - Monumento", "LRT1 - Monumento", 0.01]
  ]
)

walk_edsa = Walk(
  trails = [
    ["EDSA Carousel - Balintawak", "LRT1 - Balintawak", 0.15],
    ["EDSA Carousel - Roosevelt", "LRT1 - Roosevelt", 0.16],
    ["EDSA Carousel - North Avenue", "MRT3 - North Avenue", 0.11],
    ["EDSA Carousel - Quezon Avenue", "MRT3 - Quezon Avenue", 0.18],
    ["EDSA Carousel - Santolan Annapolis", "MRT3 - Santolan Annapolis", 0.17],
    ["EDSA Carousel - Ortigas", "MRT3 - Ortigas", 0.28],
    ["EDSA Carousel - Guadalupe", "MRT3 - Guadalupe", 0.15],
    ["EDSA Carousel - Buendia", "MRT3 - Buendia", 0.13],
    ["EDSA Carousel - Ayala", "MRT3 - Ayala", 0.089],
    ["EDSA Carousel - Taft Avenue", "MRT3 - Taft Avenue", 0.27],
    ["LRT1 - EDSA", "MRT3 - Taft Avenue", 0.35],
    ["LRT1 - EDSA", "EDSA Carousel - Taft Avenue", 0.26]
  ]
)

walk_tip = Walk(
    trails = [
        ["T.I.P.", "Potsdam / Aurora Boulevard", 0.02],
        ["T.I.P.", "LRT2 - Anonas", .45],
    ]
)



# Initialize graph dict
graph = {}



# Function for setting cost between two nodes
def setCost(cost_name, src, dest, cost, discountable = None, transport = None):
  # Initialize the source dict if non-existent
  if src in graph:
    src_dict = graph[src]
  else:
    src_dict = {}
    graph[src] = src_dict

  # Initialize the destination dict if non-existent
  if dest in src_dict:
    dest_dict = src_dict[dest]
  else:
    dest_dict = {}
    src_dict[dest] = dest_dict

  # Set cost
  # Only change if newer is lower
  if cost_name not in dest_dict or dest_dict[cost_name] > cost:
    dest_dict[cost_name] = cost

    # Set transport property
    if transport is not None:
      dest_dict["transport"] = transport

  # Set discountable property
  if discountable is not None and "discountable" not in dest_dict:
    dest_dict["discountable"] = discountable



def setTwoWayCost(cost_name, node1, node2, cost, discountable = None):
  # Set cost node1 to node2
  setCost(cost_name, node1, node2, cost, discountable)
  # Set cost node2 to node1
  setCost(cost_name, node2, node1, cost, discountable)



def getCost(cost_name, src, dest, discounted = False):
  # Check if source node is in graph
  if src in graph:
    src_dict = graph[src]
    # Check if destination node is connected from source node
    if dest in src_dict:
      dest_dict = src_dict[dest]
      # Check if the cost exist
      if cost_name in dest_dict:
        # Apply discount if needed
        if discounted:
          return dest_dict[cost_name] * (1 - discount)

        return dest_dict[cost_name]

  # If any check fail, return -1 (meaning no connection)
  return -1



# This dict will contain all station names as keys
# The value is the location name of the station
stations = {}

# Locations are places from walking trails, and station names (without the transport name)
# This dict will contain location names as keys
# The values are arrays of stations with the same location name
locations = {}



# Add the public transports in the graph
for transport in transports:

  transport_name = transport.name
  distances = transport.distances
  two_way = transport.two_way
  discountable = transport.discountable

  # Array for storing station nodes
  station_nodes = []



  # Generate names for station nodes
  for location_name in transport.stations:

    station_name = transport_name + " - " + location_name
    station_nodes.append(station_name)

    # Add the location name (without transport name) to locations
    # Add the station in the location group
    if location_name in locations:
      locations[location_name].append(station_name)
    else:
      locations[location_name] = [station_name]

    # Add the station name to stations
    stations[station_name] = location_name



  # Adding distances in the graph
  # Loop through possible first station
  for index1, station1 in enumerate(station_nodes):

    distance = 0 # variable for distance

    # Loop through possible second station
    for index2, station2 in enumerate(station_nodes[index1+1:]):

      # Add the distance for the next station
      distance += distances[index1 + index2]

      # Set the covered distance for the two stations
      setTwoWayCost("distance", station1, station2, distance)


  # for index, distance in enumerate(distances):
    # station1 = station_nodes[index] # station1 name
    # station2 = station_nodes[index + 1] # station2 name

    # setTwoWayCost("distance", station1, station2, distance)



  # Adding fare when matrix is specified
  if hasattr(transport, "fare_matrix"):

    # Loop through the rows
    for src_index, row in enumerate(transport.fare_matrix):

      src = station_nodes[src_index] # source station name

      # Loop through the fare costs
      for dest_index, fare in enumerate(row):

        # Negative fare means there's no route to that station
        # Only include 0 or positive prices
        if fare >= 0:
          dest = station_nodes[dest_index] # destination station name

          setCost("fare", src, dest, fare, discountable, transport_name)



  # Adding fare when function is specified
  if hasattr(transport, "fare_function"):

    # Loop through possible source nodes
    for src_index, src in enumerate(station_nodes):

      distance = 0 # variable for distance

      # Loop through possible destination nodes
      for dest_index, dest in enumerate(station_nodes[src_index+1:]):

        # Add the distance for the next station
        distance += distances[src_index + dest_index]

        fare = transport.fare_function(distance) # Calculate the fare

        setCost("fare", src, dest, fare, discountable, transport_name) # Set the fare

        # If the transport is two-way, also set the fare for reverse
        if two_way:
          setCost("fare", dest, src, fare, discountable, transport_name)



# List of station names
station_names = list(stations.keys())

# Add walking distance between nodes in the graph
for walk in walks:
  for trail in walk.trails:
    node1 = trail[0]
    node2 = trail[1]
    distance = trail[2]

    setTwoWayCost("distance", node1, node2, distance)

    # If a node is not a station, then it is a location
    if node1 not in station_names and node1 not in locations:
      locations[node1] = []
    if node2 not in station_names and node2 not in locations:
      locations[node2] = []



# Add distance between locations and stations with the same names
for location, grouped_stations in locations.items():

  # Distance of the location from all the same name stations
  distance = 0.01 # assume 50 meter walk minimum walk

  # Loop for each pair station (including the location itself)
  for index, station1 in enumerate([location] + grouped_stations):
    for index, station2 in enumerate(grouped_stations[index:]):
      temp_distance = getCost("distance", station1, station2)

      if temp_distance > 0:
        # sum up the squares of distances between stations
        distance += temp_distance*temp_distance

  # The square root of the sum of the squares of the distances is guaranteed to be greater than any one of the distances
  # It can be halved because a path through a location between two stations would go through 2 distances

  # This makes it so that any new path through a location will not become a shortcut between stations

  distance = math.sqrt(distance)/2

  # Set the distances
  for station in grouped_stations:
    setTwoWayCost("distance", location, station, distance)






# List of location names
location_names = list(locations.keys())

# List of uppercase location names
location_names_upper = [location_name.upper() for location_name in location_names]

# Function for searching a location
def find_location(search_location):

  # Convert to uppercase for case-insensitive search
  search_location_upper = search_location.upper()

  # Check if uppercase location is in uppsercase location list
  if search_location_upper in location_names_upper:

    # Get the index in the uppercase location list
    index = location_names_upper.index(search_location_upper)

    # Return the location name from the normal location list
    return location_names[index]

  else:

    # If no exact match is found, try to get incomplete matches

    # This array will contain incomplete matches
    matches = []

    for index, location_name_upper in enumerate(location_names_upper):
      # Find the input in the string
      # If the found index is not -1, then it is found
      if location_name_upper.find(search_location_upper) >= 0:
        matches.append(location_names[index])

    # Return incomplete matches if found
    if matches:
      return matches

    # Return None if location is not found
    return None





# Function for getting location input
def input_location(prompt):

  # Keep asking for input until an exact match is found
  while True:

    # Print the prompt and take input
    print(prompt)
    user_input = input("Enter location name: ")

    # Use the find_function to get the location
    match = find_location(user_input)

    if isinstance(match, str):

      # If exact match is found, return it
      return match

    if match is None:

      # If no match is found, print it
      print("\nLocation not found\n")

    elif isinstance(match, list):

      # If incomplete matches are found, print it
      print("\n\nMatches found:")
      print(" - " + "\n - ".join(match))



# Function for getting number input
def input_number(prompt):

  # Keep asking until a valid number is entered
  while True:

    # Print the prompt and take input
    print(prompt)
    user_input = input("Enter number: ")

    try:
      # Parse and return if input could be parsed as float
      return float(user_input)
    except ValueError:
      # Print invalid if parsing fails
      print("\nInvalid number\n")



# Function for getting yes or no input
def input_yes_or_no(prompt):

  # Loop until valid input is entered
  while True:

    # Print the prompt and take input
    print(prompt)
    user_input = input("Enter yes or no: ")

    yes_choices = ['yes', 'y', 'true', 't']
    no_choices = ['no', 'n', 'false', 'f']

    if user_input.lower() in yes_choices:
      # Return true for yes
      return True
    elif user_input.lower() in no_choices:
      # Return false for no
      return False
    else:
      # Print invalid if neither
      print("\nInvalid input\n")



# Function for getting input from choices
def input_choice(prompt, choices, choice_name = "Options"):

  # Loop until valid input is entered
  while True:

    # Print the prompt
    print(prompt)

    # Print the choices
    print("\n" + choice_name + ":")
    for (index, choice) in enumerate(choices, start=1):
      print("", index, "-", choice)

    # Take input
    user_input = input("\nEnter option index: ")

    try:
      # Parse to integer index
      index = int(user_input) - 1

      if 0 <= index < len(choices) :
        # Return the choice
        return choices[index]
      else:
        # Print invalid if neither
        print("\nInvalid index\n")

    except ValueError:
      # Print invalid if parsing fails
      print("\nInvalid index\n")



# Input for source location
source = input_location("\nWhere are you commuting from?")
print("\nSource location set to:", source, "\n")

# Input for maximum walking distance
max_walking_distance = input_number("\nHow far are you willing to walk? (km)")
print("\nMaximum walking distance set to:", str(max_walking_distance) + "km\n")

# Input for maximum walking distance
max_fare = input_number("\nHow much can you spend in commuting? (P)")
print("\nMaximum fare set to:", "P" + str(max_fare), "\n")

# Input for discount
discounted = input_yes_or_no("\nAre you given discount (Student/Senior/PWD)?")
print("\nDiscount will" + (" not " if not discounted else " ") + "be applied.\n")

# Input for sorting target
optimization_choices = ["fare", "walking distance", "fare efficiency"]
optimization_target = input_choice("\nWhat would you like to optimize for?", optimization_choices)
print("\nOptimizing answers by:", optimization_target + "\n")




# Function for getting optimized path
# This is a Modified Dijkstra's Algorithm
# It factors in both fare and distance

optimization_costs = [
  "fare",
  "walking distance",
  "fare efficiency",
  "total distance",
  "hops"
]

def get_optimized_path(start_node, end_node):

  # Dict for containing visited nodes and their properties
  visited = {}
  # Queue for nodes to visit
  to_visit = deque()

  # Set the property for the source node
  start_path_details = {
    "fare": 0,
    "walking distance": 0,
    "fare efficiency": 0,
    "total distance": 0,
    "hops": 0,
    "path": [{
      "node": start_node,
      "walked_to": False
    }]
  }

  # Optimized path for each cost will be kept in track
  optimization_dict = {}
  visited[start_node] = optimization_dict
  for cost in optimization_costs:
    optimization_dict[cost] = start_path_details

  # Set the source node to be visited first
  to_visit.append(start_node)

  # Function for visiting a node
  def visit(current_node):

    optimization_dict = visited[current_node]

    for cost in optimization_costs:

      # Get the path details for all costs
      current_path_details = optimization_dict[cost]

      # Get the path details
      current_path = current_path_details["path"]
      current_fare = current_path_details["fare"]
      current_walk = current_path_details["walking distance"] # walking distance
      current_dist = current_path_details["total distance"] # total distance
      current_hops = current_path_details["hops"]

      # Loop for all connected nodes
      for next_node in graph[current_node].keys():

        # Get the costs for jumping to the next node
        next_distance = getCost("distance", current_node, next_node)
        next_fare = getCost("fare", current_node, next_node, discounted)

        # This function is for checking the next node
        def check_next_node(will_walk): # will_walk determines if the next node will be walked to

          # Create local variables for walking distance and fare
          new_walk = current_walk # walking distance
          new_fare = current_fare
          new_dist = current_dist

          if will_walk:
            # If walking to the next node, the walking distance will increase
            new_walk += next_distance # walking distance
          else:
            # If riding to the next node, the fare will increase
            new_fare += next_fare

          # If new walking distance or fare passes the limit, cancel operation and return
          if new_walk > max_walking_distance:
            return
          if new_fare > max_fare:
            return

          new_dist += next_distance

          new_rode = new_dist - new_walk # rode distance

          # Update fare efficiency
          if new_rode == 0:
            new_ratio = 0
          else:
            # Efficiency is reciprocated for comparison
            # It is also multiplied to total distance to remove incentive for riding back and forth
            new_ratio = new_dist * new_fare/new_rode

          # Create local variable for the hop counter
          new_hops = current_hops

          previously_walked = current_path[-1]["walked_to"]
          if not previously_walked or not will_walk:
            # If either the current node or the next node will not be walked to, add to hop counter
            new_hops += 1

          # Create a copy of the current path
          new_path = current_path.copy()
          # Add current node to new path
          new_path.append({
            "node": next_node,
            "walked_to": will_walk
          })

          # Create a new node dict
          new_path_details = {
            "fare": new_fare,
            "walking distance": new_walk,
            "fare efficiency": new_ratio,
            "total distance": new_dist,
            "hops": new_hops,
            "path": new_path
          }

          if next_node in visited:
            optimization_dict = visited[next_node]

            # Loop for all optimization costs
            for cost2 in optimization_costs:

              old_path_details = optimization_dict[cost2]

              if new_path_details[cost2] < old_path_details[cost2]:
                # If new path is better in a cost, update to new path in that cost
                optimization_dict[cost2] = new_path_details

                # Add next node to visit queue
                if next_node not in to_visit:
                  to_visit.append(next_node)

          else:

            # Create new optimization dict if needed
            optimization_dict = {}
            visited[next_node] = optimization_dict

            # Set new path for all costs
            for cost2 in optimization_costs:
              optimization_dict[cost2] = new_path_details

            # Add next node to visit queue
            if next_node not in to_visit:
              to_visit.append(next_node)


        # If possible, try walking to the next station
        if (next_distance >= 0):
          check_next_node(True)

        # If possible, also try riding to the next station
        if (next_fare >= 0):
          check_next_node(False)

  # Visit nodes in the queue until all are explored
  while to_visit:
    visit(to_visit.popleft())


  if end_node in visited:
    # If end node is visited, return its optimized path for the specific property
    return visited[end_node][optimization_target]
  else:
    # If end node was not visited, return None
    return None



def path_details_to_steps(path_details):
  path = path_details["path"]


  steps = []

  step_start = path[0]["node"]
  step_count = 1

  is_walking = path[0]["walked_to"]

  # Distance accumulator
  step_distance = 0

  def append_walk(step_end):
    nonlocal step_start
    nonlocal step_distance
    nonlocal step_count
    steps.append(
      "({count}) Walk (Distance: {distance:.2f}km)\n     from [{start}]\n     to [{end}] ".format(
        count = step_count,
        start = step_start,
        end = step_end,
        distance = step_distance
      )
    )
    step_distance = 0 # Reset distance
    step_start = step_end
    step_count += 1

  def append_ride(step_end):
    nonlocal step_start
    nonlocal step_count
    steps.append(
      "({count}) Ride {transport} (Fare: P{fare:.2f})\n     from [{start}]\n     to [{end}] ".format(
        count = step_count,
        transport = graph[step_start][step_end]["transport"], # Get the transport name
        start = stations[step_start], # Get the location name
        end = stations[step_end],
        fare = getCost("fare", step_start, step_end, discounted)
      )
    )
    step_start = step_end
    step_count += 1

  prev_node = path[0]["node"]

  for jump in path[1:]:
    next_node = jump["node"]
    walk_to_next_node = jump["walked_to"]

    # Walking after walking is considered one walk
    if not walk_to_next_node:
      # Only add step if not walking to next node
      if is_walking:
        # If walking before, append the walk until previous node
        append_walk(prev_node)

      append_ride(next_node)
    else:
      # If walking to next node, add new distance to step distance
      step_distance += getCost("distance", prev_node, next_node)

    is_walking = walk_to_next_node
    prev_node = next_node

  # If last node was walked to, it would not be appended in the loop
  if is_walking:
    append_walk(next_node)

  return steps



def print_path_details(path_details):
  print("\n" + "=" * 50 + "\n")

  path = path_details["path"]
  start_node = path[0]["node"]
  end_node = path[-1]["node"]

  print("Result path from [{start}] to [{end}]".format(
    start = start_node,
    end = end_node
  ))

  actual_efficiency = 0 if path_details["fare efficiency"] == 0 else 1 / path_details["fare efficiency"] * path_details["total distance"]

  print("\nTotal fare: P{0:.2f}".format(path_details["fare"]))
  print("Total walking distance: {0:.2f}km".format(path_details["walking distance"]))
  print("Fare efficiency: {0:.2f}km in transit/P1".format(actual_efficiency))

  steps = path_details_to_steps(path_details)

  print("\nCommute steps: ")
  print("\n" + "\n\n".join(steps))
  print("\n" + "=" * 50 + "\n")



def find_path(source, destination):
  path_details = get_optimized_path(source, destination)

  if path_details is None:
    print("\nNo suitable path was found from [{start}] to [{end}]\n".format(
      start = source,
      end = destination
    ))
  else:
    print_path_details(path_details)


find_path(source, "T.I.P.")
find_path("T.I.P.", source)

