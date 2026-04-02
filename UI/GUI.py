import tkinter as tk
from tkinter import *

import pandas as pd

from Algorithms.Adaline import adaline_algorithm
from Algorithms.SinglePerceptron import perceptron_algorithm


def choose_algorithm():
    algo = algorithm_radioButton.get()
    num_epochs = m.get()
    learning_rate = eta.get()
    mse = mse_threshold.get()

    bias = bias_Checkbutton.get()

    feature1_value = feature1_radioButton.get()
    feature2_value = feature2_radioButton.get()
    classes_value = classes_radioButton.get()
    if algo == 1:
        perceptron_algorithm(num_epochs, learning_rate, bias, feature1_value, feature2_value, classes_value)
    elif algo == 2:
        data = pd.read_excel('Dataset/Dry_Bean_Dataset.xlsx')
        adaline_algorithm(num_epochs, learning_rate, mse, bias, feature1_value, feature2_value, classes_value)
    else:
        raise Exception('You must choose an algorithm to train and evaluate')


# -------------------------Main Window-------------------------#

window = Tk()

window.geometry('950x700+250+10')

tk.Label(text="( Dry Beans Classification )").place(x=400, y=0)

window.title('Tasks Window')

# -------------------------Main Window-------------------------#

# -------------------Task 1 GUI----------------------------------#

# tk.Label(text='Choose the file with the sample data to generate the signal :').place(x=420, y=385)

# sineWave_Checkbutton = tk.IntVar()
# cosineWave_Checkbutton = tk.IntVar()
# tk.Checkbutton(text="sin wave", variable=sineWave_Checkbutton, onvalue=1, offvalue=0).place(x=30, y=10)
# tk.Checkbutton(text="cosine wave", variable=cosineWave_Checkbutton, onvalue=1, offvalue=0).place(x=120, y=10)

tk.Label(text='HyperParameters :-').place(x=20, y=40)

tk.Label(text='Enter number of epochs (m) : ').place(x=0, y=70)
tk.Label(text='Enter learning rate (eta) : ').place(x=0, y=110)
tk.Label(text='Enter MSE Threshold : ').place(x=0, y=150)

m = IntVar()
tk.Entry(textvariable=m).place(x=170, y=70)
eta = DoubleVar()
tk.Entry(textvariable=eta).place(x=140, y=110)
mse_threshold = DoubleVar()
tk.Entry(textvariable=mse_threshold).place(x=120, y=150)

tk.Label(text='Select two features :-').place(x=20, y=210)

feature1_radioButton = tk.IntVar()
feature2_radioButton = tk.IntVar()

tk.Radiobutton(window, text="Area", variable=feature1_radioButton, value=1).place(x=20, y=260)
tk.Radiobutton(window, text="Perimeter", variable=feature1_radioButton, value=2).place(x=80, y=260)
tk.Radiobutton(window, text="MajorAxisLength", variable=feature1_radioButton, value=3).place(x=160, y=260)
tk.Radiobutton(window, text="MinorAxisLength", variable=feature1_radioButton, value=4).place(x=280, y=260)
tk.Radiobutton(window, text="roundnes", variable=feature1_radioButton, value=5).place(x=400, y=260)

tk.Radiobutton(window, text="Area", variable=feature2_radioButton, value=1).place(x=20, y=310)
tk.Radiobutton(window, text="Perimeter", variable=feature2_radioButton, value=2).place(x=80, y=310)
tk.Radiobutton(window, text="MajorAxisLength", variable=feature2_radioButton, value=3).place(x=160, y=310)
tk.Radiobutton(window, text="MinorAxisLength", variable=feature2_radioButton, value=4).place(x=280, y=310)
tk.Radiobutton(window, text="roundnes", variable=feature2_radioButton, value=5).place(x=400, y=310)

tk.Label(text='Select whether you want bias in data or not :-').place(x=600, y=260)
bias_Checkbutton = tk.IntVar()
tk.Checkbutton(text="bias", variable=bias_Checkbutton, onvalue=1, offvalue=0).place(x=700, y=285)

tk.Label(text='Select two classes :-').place(x=20, y=385)
classes_radioButton = tk.IntVar()
tk.Radiobutton(window, text="BOMBAY & CALI", variable=classes_radioButton, value=1).place(x=20, y=420)
tk.Radiobutton(window, text="BOMBAY & SIRA", variable=classes_radioButton, value=2).place(x=140, y=420)
tk.Radiobutton(window, text="CALI & SIRA", variable=classes_radioButton, value=3).place(x=260, y=420)

tk.Label(text='Choose the used algorithm :-').place(x=20, y=485)
algorithm_radioButton = tk.IntVar()
tk.Radiobutton(window, text="Single layer Perceptron", variable=algorithm_radioButton, value=1).place(x=20, y=520)
tk.Radiobutton(window, text="Adaline", variable=algorithm_radioButton, value=2).place(x=180, y=520)

tk.Button(text='Choose Algorithm', width=22, height=1, cursor='hand2', bd=3, command=choose_algorithm).place(x=390,
                                                                                                             y=600)
# tk.Button(text='Choose file', width=22, height=1, cursor='hand2', bd=3, command=dyF.read_data).place(x=450, y=460)

# -------------------Task 1 GUI----------------------------------#
