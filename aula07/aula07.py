curso="Curso de python";
texto=curso;
palavra="Python";
canal="CFB Cursos";
dia=5;
mes="Maio";
ano=2024;
cidade="São Paulo";
data="{}, {} de {} de {} \n\"{}\"";

resp=palavra.upper() in curso.upper();

print(resp);

resp=palavra.upper() not in curso.upper();

print(resp);

resp=curso+" do canal"+canal;

print(resp);

print (cidade+", "+str(dia)+" de "+ mes + " de " + str(ano));

print(data.format(cidade,dia,mes,ano,canal));