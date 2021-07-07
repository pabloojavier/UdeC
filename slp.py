import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def matrizTriangular(clase,bool):
    df = pd.read_excel("/Users/pablo/OneDrive - Universidad de Concepción/Material UdeC/Cuarto año/Septimo semestre/Diseños de sistemas de producción/proyecto semestral/python/Algoritmo SLP.xlsx" ,sheet_name="datos"+clase,index_col=0)

    df.replace("A", 4, inplace=True)
    df.replace("E", 3, inplace=True)
    df.replace("I", 2, inplace=True)
    df.replace("O", 1, inplace=True)
    df.replace("U", 0, inplace=True)
    df.replace("X", -4, inplace=True)

    df = df.transpose()

    return df


def graficar(clase,df):
    #df = df.transpose()
    fig, ax = plt.subplots(figsize=(5,5)) 

    sns.heatmap(df,cmap="Spectral",ax = ax)
    ax.set_title("Matriz de relevancia\nClase "+clase)
    #plt.show()

def sumarFilas(df):
    df = df.transpose()
    df["SumaF"]=df.sum(axis=1)
    return df

def ordenar_filas(df): return df.sort_values(by=["SumaF"],ascending=False)   

def orden(df):
    lista = []
    for i in range(len(df)):
        if df.index[i] not in lista:
            lista.append(df.index[i])   
            df.drop(labels='SumaF', axis=1)   
        a = df.max(axis=1)
        a = a[i]
        while a > 0:
            for j in range(len(df)): 
                if df.iloc[i][j] == a and df.columns[j] not in lista:
                    lista.append(df.columns[j])
            a -= 1     
    print(lista)
    return lista

datos = ["A","B-1","B-2","C"]
for i in datos:
    df = matrizTriangular(i,True)
    aux = df.copy()
    df = sumarFilas(df)
    df = ordenar_filas(df)
    print("Datos ",i)
    lista = orden(df)
    graficar(i,aux)
    print("")


    

