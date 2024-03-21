# Saiba seu peso em Júpiter
# Sabendo que a aceleração da gravidade em Júpiter é 24,79 m/s².

# a = float(24.79);

# def calcF(m=None):
#     if m is None:
#         m = float(input("Informe sua massa em kg: "));

#     if m > 0:
#         f = float(m * a);
#         print(f"Seu peso em Júpiter é {f:.2f}N.");
  
#     elif not isinstance(m, int):
#         print("Informe um valor válido!");
      
# calcF();

titulo = "Calcula o valor médio de avaliação do produto"
print(f'{titulo:^50}')

nota1 = int(input("Digite a primeira nota avaliada do produto pelo cliente: "))

nota2 = int(input("Digite a segunda nota avaliada do produto pelo cliente: "))

nota3 = int(input("Digite a terceira nota avaliada do produto pelo cliente: "))

media = (float(nota1) + float(nota2) + float(nota3))/3

print("A média alcançada foi: %s" % media)

if media > 6:
    print("Parabéns, produto adequado aos clientes!")
else:
    print("Que pena, esse produto inadequado e com muitas reclamações!")
