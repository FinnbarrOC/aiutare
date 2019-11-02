#!/usr/bin/env python3
import importlib
import mongoengine
import plotly
import plotly.graph_objs as go
from bin.benching.config import config
from scipy import stats
from operator import attrgetter
import numpy as np
import os
import math

INCLUDE_SAT = True
INCLUDE_UNSAT = True
INCLUDE_TIMEOUT = True
INCLUDE_UNKNOWN = False
INCLUDE_ERROR = False

X_AXIS = None
Y_AXIS = None
Z_AXIS = None   # If this is assigned a value then we are creating a 3D scatterplot

X_COORDS = []
Y_COORDS = []
Z_COORDS = []

DATA = []


def initialize_coords(names, schemas):
    for i in range(len(names)):
        X_COORDS.append([])
        Y_COORDS.append([])
        Z_COORDS.append([])

    x_parser = attrgetter(X_AXIS)
    y_parser = attrgetter(Y_AXIS)
    z_parser = None
    if Z_AXIS:
        z_parser = attrgetter(Z_AXIS)

    for result in schemas.Result.objects():
        index = names.index(result.nickname)
        if (result.result == "sat" and INCLUDE_SAT) or \
                (result.result == "unsat" and INCLUDE_UNSAT) or \
                (result.elapsed == config["timeout"] and INCLUDE_TIMEOUT) or \
                (result.result == "error" and INCLUDE_ERROR) or\
                (result.result == "unknown" and INCLUDE_UNKNOWN):
            X_COORDS[index].append(x_parser(result))
            Y_COORDS[index].append(y_parser(result))
            if Z_AXIS:
                Z_COORDS[index].append(z_parser(result))

    for i in range(len(names)):
        counter = 0
        while counter < len(X_COORDS[i]):
            if X_COORDS[i][counter] is None or Y_COORDS[i][counter] is None or \
                    (Z_AXIS and Z_COORDS[i][counter] is None):
                X_COORDS[i].pop(counter)
                Y_COORDS[i].pop(counter)
                if Z_AXIS:
                    Z_COORDS[i].pop(counter)
            else:
                counter += 1


def quadratic_r_squared(i):
    z = np.polyfit(X_COORDS[i], Y_COORDS[i], 2)
    f = np.poly1d(z)

    yhat = f(X_COORDS[i])
    ybar = np.sum(Y_COORDS[i]) / len(Y_COORDS[i])
    ssreg = np.sum((yhat - ybar) ** 2)
    sstot = sum([(yi - ybar) ** 2 for yi in Y_COORDS[i]])
    r_squared = ssreg / sstot
    return r_squared


def linear_regress(i, names, r_squared):
    slope, intercept, r_value, p_value, std_err = stats.linregress(X_COORDS[i], Y_COORDS[i])
    DATA.append(go.Scatter(
        x=[0.0, max(X_COORDS[i])],
        y=[intercept, slope * max(X_COORDS[i]) + intercept],
        mode='lines',
        name=(names[i] + " Regression Line Linear")
    ))
    if RF:
        print("\n-" + names[i] + "-")
        print("The formula for the line of best fit is:\ny = ("+str(slope)+")x + ("+str(intercept)+")")
        print("The r squared value is: " + str(r_squared))


def exp_regress(i, names, r_squared):
    slope, intercept, r_value, p_value, std_err = stats.linregress(X_COORDS[i], np.log(Y_COORDS[i]))
    x_coords_tmp = np.linspace(0, max(X_COORDS[i]), 200)
    y_coords_tmp = np.exp(slope * x_coords_tmp + intercept)
    DATA.append(go.Scatter(
        x=x_coords_tmp,
        y=y_coords_tmp,
        mode='lines',
        name=(names[i] + " Regression Line Exponential")
    ))
    if RF:
        print("\n-" + names[i] + "-")
        print("The formula for the line of best fit is:\ny = (" + str(math.exp(intercept)) +
              ")(" + str(math.exp(slope)) + ")^x")
        print("The r squared value is: " + str(r_squared))


def quadratic_regress(i, names, r_squared):
    z = np.polyfit(X_COORDS[i], Y_COORDS[i], 2)
    f = np.poly1d(z)
    x_coords_tmp = np.linspace(0, max(X_COORDS[i]), 200)
    y_coords_tmp = f(x_coords_tmp)

    DATA.append(go.Scatter(
        x=x_coords_tmp,
        y=y_coords_tmp,
        mode='lines',
        name=(names[i] + " Regression Line Quadratic")
    ))
    if RF:
        print("\n-" + names[i] + "-")
        print("The formula for the line of best fit is:\ny = (" + str(z[0]) + ")x^2 + " +
              "(" + str(z[1])+")x + ("+str(z[2])+")")
        print("The r squared value is: " + str(r_squared))


def format_data(nicknames):
    for i in range(len(nicknames)):
        if not (len(X_COORDS[i]) == 0 or not len(X_COORDS[i]) == len(Y_COORDS[i])):
            if Z_AXIS is not None:
                # 3D scatterplot case
                DATA.append(go.Scatter3d(
                    x=X_COORDS[i],
                    y=Y_COORDS[i],
                    z=Z_COORDS[i],
                    mode='markers',
                    name=nicknames[i]
                ))
            else:
                # 2D scatterplot case (with regression lines)
                DATA.append(go.Scatter(
                    x=X_COORDS[i],
                    y=Y_COORDS[i],
                    mode='markers',
                    name=nicknames[i]
                ))
                arr_r_squared = [0.0, 0.0, 0.0]

                arr_r_squared[0] = stats.linregress(X_COORDS[i], Y_COORDS[i])[2]
                arr_r_squared[1] = quadratic_r_squared(i)
                arr_r_squared[2] = stats.linregress(X_COORDS[i], np.log(Y_COORDS[i]))[2]
                optimal_fit = arr_r_squared.index(max(arr_r_squared))
                if optimal_fit == 0:
                    linear_regress(i, nicknames, max(arr_r_squared))
                elif optimal_fit == 1:
                    quadratic_regress(i, nicknames, max(arr_r_squared))
                else:
                    exp_regress(i, nicknames, max(arr_r_squared))


def format_layout():
    if Z_AXIS is not None:
        # 3D scatterplot case
        layout = go.Layout(
            scene=dict(
                xaxis=dict(
                    title=X_AXIS),
                yaxis=dict(
                    title=Y_AXIS),
                zaxis=dict(
                    title=Z_AXIS), ),
        )
    else:
        # 2D scatterplot case (with regression lines)
        layout = go.Layout(
            hovermode='closest',
            xaxis=dict(
                title=X_AXIS,
                ticklen=5,
                zeroline=False,
                gridwidth=2,
            ),
            yaxis=dict(
                title=Y_AXIS,
                ticklen=5,
                gridwidth=2,
            )
        )

    return layout


def scatterplot(x, y, z, rf):
    global X_AXIS, Y_AXIS, Z_AXIS, RF
    X_AXIS, Y_AXIS, Z_AXIS, RF = x, y, z, rf

    schemas = importlib.import_module(config["schemas"])
    mongoengine.connect(config["database_name"], replicaset="monitoring_replSet")

    nicknames = [nickname for programs, specifications in config["commands"].items() for
                 nickname, command in specifications.items()]

    initialize_coords(nicknames, schemas)

    format_data(nicknames)
    layout = format_layout()

    if Z_AXIS is None:
        filename = "plots" + os.sep + "Scatterplot2D.html"
    else:
        filename = "plots"  + os.sep + "Scatterplot3D.html"

    plotly.offline.plot({
        "data": DATA,
        "layout": layout,
    }, auto_open=True, filename=filename)

    mongoengine.connection.disconnect()
