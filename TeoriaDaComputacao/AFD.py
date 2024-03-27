'''
Paulo Eduardo Pereira Carvalho
Teoria da computacao
Exemplo:# w termina em a
   {q0,q1},             //conjunto finito de estados
   {a,b},               //alfabeto finito
   {
      (q0)->(q1,a),
      (q0)->(q0,b),
      (q1)->(q0,b),
      (q1)->(q1,a),
   },                   //funcao de transicao de estado
   q0,                  //estado inicial
   {q1}                 //conjunto de estados finais
'''

estados = []
estados = input("Insira os estados do automato: ").split()#Inserir q0 q1

alfabeto = []
alfabeto = input("Insira o alfabeto do automato: ").split()#Inserir a b

estadoInicial = input("Insira o estado inicial: ").strip()#Inserir q0

estadosFinais = []
estadosFinais = input("Insira os estados finais: ").split()#Inserir q1

estadoAtual = estadoInicial#Recebe q0 como primeiro estado

proximoEstado = ''

transicoes = {}#Dicionario para fazer as transicoes do AFD

for estado in estados:#Logica para colocar as transicoes
    for letra in alfabeto:
        print(f'{estado} lendo "{letra}" vai para o estado: ', end='')
        proximoEstado = input()
        transicoes[(estado, letra)] = proximoEstado

palavra = input("Escreva uma entrada, para sair digite 'sair': ")#Inserir palavra para testar
while palavra != 'sair':
    for char in palavra:
        estadoFinal  = transicoes[(estadoAtual, char)]#Itera ate o final da palavra e atualiza o estado
    
    if estadoFinal in estadosFinais:
        print("Palavra aceita!")
    else:
         print("Palavra rejeitada!")
    palavra = input("Escreva uma entrada, para sair digite 'sair': ")#Inserir palavra para testar
    estadoAtual = estadoInicial