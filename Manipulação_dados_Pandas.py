import pandas as pd



notas = pd.Series ([2,7,5,10,6], index=["Alex", "João", "Pedro", "Zé", "Abel"])

print (notas)
print ("A nota do Alex é:",notas["Alex"]) #é possível trazer uma nota referenciada pelo seu index, no caso "Alex"
print("Média:", notas.mean()) #notas.mean calcula a média aritmética para o vetor nota
print("Desvio padrão:", notas.std()) #notas.std calcula o desvio padrão do vetor notas
print(notas.describe()) #descibr da o resumo estatístico do vetor notas.
print (np.log(notas)) #calcula o logatirmo neperiano do vetor notas.

df = pd.DataFrame({'Aluno' : ["Alex", "João", "Pedro", "Zé", "Abel"], #Criação de um dataframe (tabela)
                   'Faltas' : [3,4,2,1,4],
                   'P1' : [2,7,5,10,6],
                   'Seminário': [8.5,7.5,9.0,7.5,8.0],
                   'P2' : [10,8,10,7,9]})
print (df)

print (df.sort_values(by="P2")) #ordena o df pela coluna escolhida
print (df.loc[1]) #traz os valores do índice explicitado
print (df[df["P2"]>8.0]) #traz somente os valors condicionais do df
print (df[(df["P2"] > 8.0) & (df["Seminário"] > 6)]) #traz somente os valors condicionais do df.
#os valores boleanos devem ser bitwise & = and, | = or, ~ = not