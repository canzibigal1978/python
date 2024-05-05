x=1; #int
x="CFB Cursos "; #string
x=15.6; #float
x=False; #bool
n1=5;n2=2;x=complex(n1,n2);

print(x.real);
print(x.imag);

print("valor: " + str(x));
print("Tipo: "+str(type(x)));

x=["carro","aviao","navio"];#list / Array

print("valor: "+x[0]);
print("Tipo: "+str(type(x)));

x=("carro","aviao","navio");#tupla

print("valor: "+x[0]);
print("Tipo: "+str(type(x)));

x=range(0,100,1); #list

print("valor: "+str(x[0]));
print("Tipo: "+str(type(x)));

x={#Dict
    "canal":"CFB Cursos",
    "curso":"Curso de python",
    "nome":"Francisco"
    }; 

print("valor: "+str(x["curso"]));
print("Tipo: "+str(type(x)));

x={5,7,4,5,7,4,8}; #set

print("valor: "+str(x));
print("Tipo: "+str(type(x)));

x=frozenset({5,7,4,5,7,4,8}); #set congelado

print("valor: "+str(x));
print("Tipo: "+str(type(x)));




