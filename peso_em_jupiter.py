# Saiba seu peso em Júpiter
# Sabendo que a aceleração da gravidade em Júpiter é 24,79 m/s².

a = float(24.79);

def calcF(m=None):
    if m is None:
        m = float(input("Informe sua massa em kg: "));

    if m > 0:
        f = float(m * a);
        print(f"Seu peso em Júpiter é {f:.2f}N.");
  
    elif not isinstance(m, int):
        print("Informe um valor válido!");
      
calcF();
