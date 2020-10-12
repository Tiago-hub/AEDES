from classes import *
import csv
tarefa = []
idTarefa = 1
def default():
    print ('Opção Inválida')

def adicionar ():
    global idTarefa
    print('Qual o nome da materia?')
    materia = str(input())
    print('Qual o titulo do trabalho?')
    titulo = str(input())
    print('Qual a pontuação do trabalho?')
    pontuacao = int(input())
    print('Qual a data de entrega?')
    dataEntrega = str(input())
    tarefa.append(tarefas(int(tarefa[-1].getId())+1,titulo,materia,pontuacao,dataEntrega))
    print('Tarefa Cadastrada com sucesso')

def listar ():
    global tarefa

    if (not(len(tarefa))):
        print('sem tarefas cadastradas')
    else:
        for umatarefa in tarefa:
            string = 'Id: '+str(umatarefa.getId())+' | Titulo: '+str(umatarefa.getTitulo())+' | Materia: '+str(umatarefa.getMateria())+' | Pontuação: '+str(umatarefa.getPontuacao())+' | Data de Entrega: '+str(umatarefa.getDataEntrega())
            print(string)

def excluir ():
    global tarefa
    print('Digite a id da tarefa que deseja deletar')
    idTarefa = int(input()) - 1 
    del(tarefa[idTarefa])

def carregar():
    global tarefa
    with open('banco_dados.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if (not(len(tarefa))):
                tarefa.append(tarefas(row[0],row[1],row[2],row[3],row[4]))
            else:
                tarefa.append(tarefas(int(tarefa[-1].getId())+1,row[1],row[2],row[3],row[4]))
            line_count += 1
        print(f'Processed {line_count} lines.')

def salvar():
    with open('banco_dados.csv', mode='w',newline='') as data_file:
        data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for umatarefa in tarefa:
            data_writer.writerow([str(umatarefa.getId()), str(umatarefa.getTitulo()), str(umatarefa.getMateria()),str(umatarefa.getPontuacao()),str(umatarefa.getDataEntrega())])

carregar()  
while (1):

      
    print('\nDeseja adicionar, listar, excluir ou salvar as tarefa(s)?')
    typedstr = str(input())



        

    menu = {
        'adicionar':adicionar,
        'listar':listar,
        'excluir':excluir,
        'salvar':salvar,
        'carregar':carregar
    }

    try:
        menu[typedstr]()
    except KeyError:
        default()