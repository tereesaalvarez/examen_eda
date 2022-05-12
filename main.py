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
print('-------------VALORES ID USER-------------')
pd.value_counts(conversiones['id_user'])
print(pd.value_counts(conversiones['id_user']))

print('------------------VALORES GCLID-------------')
pd.value_counts(conversiones['gclid'])
print(pd.value_counts(conversiones['gclid']))




navegacion= pd.read_csv('navegacion.csv')
print(navegacion)
print('----------INTRODUCCION-------------')
print(navegacion.columns)

print('-----------VARIABLES+DATOS------------')
print(navegacion.head())

print('--------------Descrpcion df------------')
print(navegacion.describe())

print('--------------informacion------------')
navegacion.info()

print('-------------VALORES ID USER-------------')
pd.value_counts(navegacion['id_user'])
print(pd.value_counts(navegacion['id_user']))

print('------------------VALORES GCLID-------------')
pd.value_counts(navegacion['gclid'])
print(pd.value_counts(navegacion['gclid']))

print('------------------VALORES COOKIES-------------')
pd.value_counts(navegacion['url_landing'])
print(pd.value_counts(navegacion['url_landing']))


# unir csv

output = pd.merge(conversiones, navegacion, on='id_user', how='outer')
print(output)
output.to_csv('union.csv')

union = pd.read_csv('union.csv')
print(union)

pd.value_counts(union['lead_type'])
print(pd.value_counts(union['lead_type']))

# Hay 24 Call y 14 Form
