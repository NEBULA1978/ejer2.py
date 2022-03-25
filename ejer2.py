"""
ejer2
Dada la siguienteslistsa:

ejem:
estudiante=["Axel","Pau,"Patricio","Roberto","Jhoa"]
parcial1=[59,75,69,40,60]
parcial2[59,40,55,10,50]
mejoramiento=[30,60,50,75,45]

Calcular el promedio de cada estudiante(se eligen las dos
notas mas altas)

Realizar:

Presentar los estudiantes que pasaron la materia,con su promedio
Presentar los Reprobados,con su promedio
El profesor decide regalar 1pt alestudiante que tenga
59 en promedio(modifique la lista) y presente nuevamente
nuevamentelo aprobados.

Recorriendo 4listas paralelas con un for
"""
estudiante=["Axel","Pau","Patricio","Roberto","Jhoa"]
parcial1=[59,75,60,40,60]
parcial2=[59,40,55,10,50]
mejoramiento=[30,60,50,75,45]
promedios=[]#[59.0, 67.5, 57.5, 57.5, 55.0]
for i in range(len(estudiante)):
    n1=parcial1[i]
    n2=parcial2[i]
    mj=mejoramiento[i]
    temp=[n1,n2,mj]#[59,59,30]
    suma= sum(temp) - min(temp)
    prom= suma/2
    promedios.append(prom)
print("---Aprobados---")
for j in range(len(promedios)):
    est=estudiante[j]
    prom=promedios[j]
    if prom >= 60:
        print(est,":",prom)
print("---Reprobados---")
for x in range(len(estudiante)):
    est=estudiante[x]
    prom=promedios[x]
    if prom < 60:
        print(est,":",prom)


print("---Se suma 1 a los que tienen 59---")

for y in range(len(promedios)):
    prom=promedios[y]
    if prom==59:
        promedios[y]+=1


for j in range(len(promedios)):
    est=estudiante[j]
    prom=promedios[j]
    if prom >= 60:
        print(est, ":", prom)