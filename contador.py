with open("days","r") as apertura:
    digito = int(apertura.read())

with open("days","w") as escrito:
    escrito.write(str(digito + 1))
