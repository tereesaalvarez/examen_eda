import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

conversiones = pd.read_csv('conversiones.csv')
print(conversiones)
print('----------INTRODUCCION-------------')
print(conversiones.columns)

print('-----------VARIABLES+DATOS------------')
print(conversiones.head())

print('--------------Descrpcion conversiones------------')
print(conversiones.describe())

print('--------------informacion------------')
conversiones.info()

#contar valores

pd.value_counts(conversiones['date'])




navegacion= pd.read_csv('navegacion.csv')
print(navegacion)
print('----------INTRODUCCION-------------')
print(navegacion.columns)

print('-----------VARIABLES+DATOS------------')
print(navegacion.head())

print('--------------Descrpcion conversiones------------')
print(navegacion.describe())

print('--------------informacion------------')
navegacion.info()