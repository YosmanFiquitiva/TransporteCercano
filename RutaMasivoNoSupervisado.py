from sklearn.cluster import KMeans
datos = [
    ["ESTACION A","ESTACION B", 7.0],
    ["ESTACION A","ESTACION C", 11.0],
    ["ESTACION A","ESTACION D", 42.0],
    ["ESTACION B","ESTACION A", 7.0],
    ["ESTACION B","ESTACION D", 5.0],
    ["ESTACION B","ESTACION E", 15.0],
    ["ESTACION B","ESTACION F", 5.0],
    ["ESTACION C","ESTACION D", 3.0],
    ["ESTACION D","ESTACION B", 5.0],
    ["ESTACION D","ESTACION F", 20.0],
    ["ESTACION E","ESTACION F", 19.0],
    ["ESTACION F","ESTACION B", 5.0],
]
kmeans = KMeans(n_clusters=3)
kmeans.fit(datos)
etiquetas = kmeans.labels_
centroides = kmeans.cluster_centers_

source = input("Por favor ingrese el nombre de la ESTACION inicial: ")
target = input("Por favor ingrese el nombre de la ESTACION final: ")

MejorRuta = nx.dijkstra_path(Rutas, source= source, target= target)
RecorridoRuta = nx.dijkstra_path_length(Rutas, source= "ESTACION E", target="ESTACION B");

print("EL mejor recorrido entre el punto : ");
print(MejorRuta);
print("Km recorridos de la ruta = ");
print(RecorridoRuta);