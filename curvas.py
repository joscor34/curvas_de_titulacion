import matplotlib.pyplot as plt
from matplotlib.collections import EventCollection
import numpy as np
import pandas as pd

valores = []

resultado = 0

resultado_reaccion = 0
suma_reactivos = 0
poh = 0
ph = 0

pre_suma = 0

valores_mili = []

molaridad_acido = float(input("Dame la molaridad de tu acido: ")) 
hidrogenos_acido = float(input("Dame la cantidad de hidrogenos de tu acido: ")) 
molaridad_base = float(input("Dame la molaridad de tu base: "))
ml_acido= int(input("Dame la cantidad en ml de tu acido: "))
parse_table = input("Quieres hacer un archivo xlsx? y/n: ")

for i in range(0,101):
  valores_mili.append(i)


for i in range(0, ml_acido + 1):
  if(i == 0):
    resultado = -1 * (np.log10(molaridad_acido * hidrogenos_acido) )
    valores.append(resultado)
  else:
    resultado_reaccion = (molaridad_acido * ml_acido) - (molaridad_base * i)
    suma_reactivos = (ml_acido + i)
    if(resultado_reaccion == 0):
      valores.append(7)
    else:
      pre_suma = (-1 * np.log10((resultado_reaccion / suma_reactivos) * hidrogenos_acido))
      valores.append(pre_suma)


for j in range(ml_acido + 1, 101):
  resultado_reaccion = abs((molaridad_acido * ml_acido) - (molaridad_base * j))
  suma_reactivos = (ml_acido + j)
  # print(suma_reactivos)
  poh = -1 * (np.log10(resultado_reaccion/suma_reactivos))
  ph = 14 - poh
  valores.append(ph) 


yevents1 = EventCollection(valores, color='tab:orange', linelength=0.05, orientation='horizontal')

if(parse_table == "y"):
  nombre_archivo = input("Dame el nombre para el archivo xlsx")
  df = pd.DataFrame({ 'militros base': valores_mili, 'pH': valores })
  df.index.name = 'ID'

  df.to_excel(nombre_archivo + '.xlsx')


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
#ax.plot([7], marker=11)
#ax.plot(valores_mili, valores, color='tab:blue')
#ax.add_collection(yevents1)
markers_on = [ml_acido]
ax.plot(valores_mili, valores, '-gD', markevery=markers_on, label='Punto neutro', color='tab:blue')
ax.legend()
ax.set_title('Curva de titulación')
ax.set_xlabel("ml de NaOH")
ax.set_ylabel("pH Solución")
#plt.stem(valores_mili, valores)
plt.show()