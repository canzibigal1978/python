a=True;
a=False;

a=10;
b=5;
op="/";
res=0;


if a:
    print("CFB Cursos");

if a>b:
    print("e maior");

if a<b:
    print("e menor");

if op=="+":
    res=a+b;

if op=="-":
    res=a-b;

if op=="*":
    res=a*b;

if op=="/":
    res=a/b;

cat="{} {} {} = {}";
print(cat.format(a,op,b,res));

print("Fim Programa.")