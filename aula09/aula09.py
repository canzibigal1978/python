carros=["HRV","Golf","Argo","Focus"]; #list

carros.append("Fit");
carros.append("Fusion");
carros.append("Polo");

print(carros);
print(carros[0]); #list indice
print(carros[-1]); #lista Indice inverso.
print(str(len(carros))+" carros na lista.");

carros.remove("Polo");
print(str(len(carros))+" carros na lista.");

carros.pop();
print(str(len(carros))+" carros na lista.");

del carros[2];
print(str(len(carros))+" carros na lista.");

#carros.clear();
#print(str(len(carros))+" carros na lista.");

carros2 = list(carros);
print(str(len(carros2))+" carros na lista.");

carro3=["Fusca","147","Brasilia","Celta"];

carro4=carros+carro3

print(carro4);

