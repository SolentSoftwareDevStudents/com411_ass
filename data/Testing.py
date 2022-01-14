from datetime import *
from tui import observation_dates


for count, date in enumerate(observation_dates()):
    d1, m1, y1 = [int(x) for x in date.split('/')]

    date1 = (d1, m1, y1)

    d2, m2, y2 = [int[x] for x in co]

    print(date1)
