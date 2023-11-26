#LISTAS
nome = ['Alex', 'Jéssica', 'Fábio', 'Magda']
idade = [41, 34, 50, 55]
peso = [89, 68, 88, 74]
altura = [1.85, 1.65, 1.78, 1.65]
imcs = [50, 40, 34, 70]


#MENU DE OPÇÕES
def menu():
    while True:
         print("1 - Incluir aluno")
         print("2 - Listar todos alunos e seus dados")
         print("3 - Listar os dados de um aluno")
         print("4 - Listar dados dos alunos de uma determinada Idade")
         print("9 - Fim")

         try:
             opcao = int(input("Digite número do menu: "))
             return opcao
         except ValueError:
             print("Digite somente o número!")

#1) incluir Aluno
#Digite adicione nas respectivas listas, o nome, a idade do aluno, o peso do aluno, a altura do aluno e Calcule
# o  IMC = Peso ÷ (Altura × Altura)
#Use o mesmo índice por aluno, digite enquanto o nome do aluno não for VAZIO.(INCOMPLETO)

def incluirAluno():
    print("Incluir aluno: ")
    nome = input("Digite o nome: ")
    idade = int(input("Digite sua idade:"))
    peso = int(input("Digite seu Peso: "))
    altura = float(input("Digite sua altura"))

    imcCalculo = peso / (altura * altura)

    imcs.append(imcCalculo)
    nome.append(nome)
    idade.append(idade)
    peso.append(peso)
    altura.append(altura)
    imcs.append(imcCalculo)
    return

    print(f"O IMC do aluno {nome} é:  {imcCalculo}")  


#2) listar todos alunos e seus dados
#Listar todos os alunos e seus dados e no final mostrar o IMC médio do grupo.(DUVIDAS E ANGUSTIAS)

def listar():
    print("Listar todos os alunos e seus dados")
    print(nome, idade, peso, altura)
    for i in range(len(nome)):
        print(nome[i], idade[i], peso[i], altura[i])
        print(imcCalculo / len(imcs))                    #????????????


#3) listar os dados de um aluno
#Pedir o nome de um aluno e listar todos os dados deste aluno.(INCOMPLETO)
def listarAlunoUnico():
    print("Listar os dados de um único aluno")
    aluno = input("Listar um aluno")
    for i in range(nome):
        if aluno == nome[i]:
            print(nome[i], idade[i], peso[i], altura[i])
            break
    else:
        print(f"Aluno não encontrado")

#4) listar os dados dos alunos de uma determinada idade
#Pedir uma idade e listar todos os dados dos alunos desta idade e no final mostrar o IMC médio deste grupo.(INCOMPLETO)
def detIdade():
    print("Listar alunos de uma determinada idade")
    idadeselecao = int(input("Listar alunos de uma determinada idade"))
    for i in range(len(nomes)):
        if idadeselecao == idades[i]:
            print(nome[i], idade[i], peso[i], altura[i], imcs[i])

while True:

    opcao = menu()

    if opcao == 1:
         incluirAluno()

    elif opcao == 2:
          listar()

    elif opcao == 3:
          listarAlunoUnico()

    elif opcao == 4:
        detIdade()

    elif opcao == 9:
        break    
