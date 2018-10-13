b# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

class Plotter(object):

    def __init__(self, left=0.1, bottom=0.1, right=1.0, top=1.0):
        fig = plt.figure()
        self.ax = fig.add_axes([left, bottom, right, top])

    def 