################################################################################################################## VÁRIAVEIS

var_opcao = 0
base = 0
altura = 0
controla_loop = False

################################################################################################################## FUNÇÕES

def calcula_areatriangulo():
    area = (base * altura)/2
    print("ÁREA:",area,"M²")
    
def calcula_perimetrotriangulo():
    perimetro = 3*base
    print("PERIMETRO:",perimetro,"M")

##################################################################################################################  GUARDA DADOS
print("\nPROGRAMA QUE CALCULA A AREA DO TRIANGULO EQUILATERO OU SEU PERIMETRO\n")

base = float(input("INFORME A BASE EM METROS:\n"))
altura = float(input("INFORME A ALTURA EM METROS:\n"))

##################################################################################################################  ESCOLHA DE FUNÇÃO

while controla_loop == False:
    var_opcao= float(input("DESEJA CALCULAR A ÁREA(OPÇÃO 1) OU ALTURA(OPÇÃO 2) DO TRIANGULO?"))
    if var_opcao == 1:
        calcula_areatriangulo()
        controla_loop = True

    elif var_opcao == 2:
        calcula_perimetrotriangulo()
        controla_loop = True
    else:
        print("OPÇÃO INVALIDA!")  
   
#################################################################################################################### FIM PROGRAMA
                   



