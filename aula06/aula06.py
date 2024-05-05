curso="Curso de python";



print (curso[0:5]);
print(curso[9:15]);
print("tamanho: "+str(len(curso)));

print("Strip:'"+curso.strip()+"'");
print("lower:'"+curso.lower()+"'");
print("upper:'"+curso.upper()+"'");
print("Replace:'"+curso.replace("py","C#")+"'");

s=curso.split(" ");
print("'"+s[0]+"'");
print("'"+s[1]+"'");
print("'"+s[2]+"'");
