# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import requests

def plot_xy(x, y, fname=""):
    # Take in a list of arrays, x and y data, and an optional title

    fig, ax = plt.subplots(1, 1)
    fig.subplots_adjust(hspace=0.5)
    ax.plot(x, y)
    ax.set_xlabel('Year')
    ax.set_ylabel('Temp.')
    ax.grid(True)
    startx, endx = ax.get_xlim()
    ax.xaxis.set_ticks(np.arange(startx, endx, 5))
    if fname != "":
        ax.set_title(fname)
        fig.savefig(fname + ".png")
    else:
        plt.show()


def extract_xy_long(data_file):
    f = open(data_file, encoding="utf-8")
    f.readline()            # Skip first row
    f.readline()            # Skip second row
    x = []
    y = []
    y0 = []
    for l in f.readlines():
        dummy, year, month, temp, dummy = l.split()
        y0.append(float(temp))
        if month == "12":
            x.append(year)
            y.append(sum(y0)/len(y0))
            y0 = []
    f.close()

    return np.array(x), np.array(y)

def extract_xy_short(data_file):
    f = open(data_file, encoding="utf-8")
    f.readline()            # Skip first row
    f.readline()            # Skip second row
    x = []
    y = []
    for l in f.readlines():
        dummy, year, temp, dummy, dummy, dummy, dummy, dummy, dummy, dummy, dummy, \
            dummy, dummy, dummy, dummy, dummy, dummy = l.split()
        if year == "NA" or temp == "NA":    # Drop dead readings
            continue
        else:
            x.append(year)
            y.append(temp)
    f.close()
    
    return np.array(x), np.array(y)

def extract_data(data_file):
    # Decide on long or short format

    response = requests.get(data_file)
    f = response.text
    f.encode(encoding="utf-8")

    filename = "dummy_data_file.txt"
    file_ = open(filename, 'w', encoding="utf-8")
    file_.write(f)
    file_.close()

    f_word1 = f.split()[0]

    if f_word1 == "Ársmeðaltöl":
        # Short form data file (few years)
        x, y = extract_xy_short(filename)
    else:
        # Long form data file (all years)
        x, y = extract_xy_long(filename) 

    return x, y
    

if __name__ == "__main__":

    # Long time series
    f_long = "https://www.vedur.is/Medaltalstoflur-txt/lengri/Storhofdi.txt"
    xlong, ylong = extract_data(f_long)
    first = -67     # Counted from last item towards first
    last = -4       # Counted from last item towards first
    plot_xy(xlong[first:last], ylong[first:last], fname="Long data, from " + str(xlong[first:][0]) + " to " + str(xlong[last]))

    # Short time series
    f_short = "https://www.vedur.is/Medaltalstoflur-txt/Stod_815_Storhofdi.ArsMedal.txt"
    xshort, yshort = extract_data(f_short)
    plot_xy(xshort, yshort, fname="Short data, from " + str(xshort[0]) + " to " + str(xshort[-1]))
  