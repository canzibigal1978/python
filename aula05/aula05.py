import random;

num_i=10;
num_f=5.2;
num_c=1j;

x=num_i;

print("Valor: " + str(x) + " - Tipo: " + str(type(x)));

x=num_f;

print("Valor: " + str(x) + " - Tipo: " + str(type(x)));

x=num_c;

print("Valor: " + str(x) + " - Tipo: " + str(type(x)));

x=int(num_f);

print("Valor: " + str(x) + " - Tipo: " + str(type(x)));

num_r=random.randrange(0,59);
x=num_r;

print("Valor: " + str(x) + " - Tipo: " + str(type(x)));

num_r=[
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59)
];
x=num_r;

print("Valor1: " + str(x[0]));
print("Valor2: " + str(x[1]));
print("Valor3: " + str(x[2]));
print("Valor4: " + str(x[3]));
print("Valor5: " + str(x[4]));
print("Valor6: " + str(x[5]));