from classes import *
from pprint import pprint
from datetime import datetime
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
    print('Qual a pontuação do trabalho? Insira um valor entre 0 e 99 no formato xx')
    while True:
        try:
            pontuacao = int(input())
            break
        except ValueError:
            print("Apenas numeros inteiros...")  
            continue
    print('Qual a data de entrega?')
    datetime_format = "%d/%m/%Y"
    while True:
        try:
            dataInput=datetime.strptime(str(input()), datetime_format)
            break
        except ValueError:
            print("Data inválida. Insira data na forma dd/mm/aaaa")  
            continue
    
    
    dataEntrega = datetime.timestamp(dataInput)
    quick_sort(tarefa, 0, len(tarefa) - 1, lambda x, y: x.id > y.id)
    tarefa.append(tarefas(int(tarefa[-1].getId())+1,titulo,materia,pontuacao,dataEntrega))
    print('Tarefa Cadastrada com sucesso')

def listar ():
    global tarefa

    if (not(len(tarefa))):
        print('sem tarefas cadastradas')
    else:
        print('')
        print('Deseja ordenar por id, data ou pontos?')
        resposta = str(input())
        if(resposta=='id'):
            quick_sort(tarefa, 0, len(tarefa) - 1, lambda x, y: x.id > y.id)
            print('')
            print('Lista de trabalhos (ordenada por id)')
            print('--------------------------------------------------------------------------------------------------------')
            for umatarefa in tarefa:
                
                string = 'Id: '+str(umatarefa.getId())+' | Titulo: '+str(umatarefa.getTitulo())+' | Materia: '+str(umatarefa.getMateria())+' | Pontuação: '+str(umatarefa.getPontuacao())+' | Data de Entrega: '+str(datetime.fromtimestamp((umatarefa.getDataEntrega())).strftime('%d/%m/%Y'))
                print(string)
        elif(resposta=='data'):
            quick_sort(tarefa, 0, len(tarefa) - 1, lambda x, y: x.dataEntrega > y.dataEntrega)
            print('')
            print('Lista de trabalhos (ordenada por data de entrega)')
            print('--------------------------------------------------------------------------------------------------------')
            for umatarefa in tarefa:
                
                string = 'Id: '+str(umatarefa.getId())+' | Titulo: '+str(umatarefa.getTitulo())+' | Materia: '+str(umatarefa.getMateria())+' | Pontuação: '+str(umatarefa.getPontuacao())+' | Data de Entrega: '+str(datetime.fromtimestamp((umatarefa.getDataEntrega())).strftime('%d/%m/%Y'))
                print(string)
        elif(resposta=='pontos'):
            quick_sort(tarefa, 0, len(tarefa) - 1, lambda x, y: x.pontuacao > y.pontuacao)
            print('')
            print('Lista de trabalhos (ordenada por pontuação)')
            print('--------------------------------------------------------------------------------------------------------')
            for umatarefa in tarefa:
                
                string = 'Id: '+str(umatarefa.getId())+' | Titulo: '+str(umatarefa.getTitulo())+' | Materia: '+str(umatarefa.getMateria())+' | Pontuação: '+str(umatarefa.getPontuacao())+' | Data de Entrega: '+str(datetime.fromtimestamp((umatarefa.getDataEntrega())).strftime('%d/%m/%Y'))
                print(string)
        else:
            print('opção inválida')
def excluir ():
    global tarefa
    print('Digite a id da tarefa que deseja deletar')
    idTarefa = int(input()) - 1 
    quick_sort(tarefa, 0, len(tarefa) - 1, lambda x, y: x.id > y.id)
    del(tarefa[idTarefa])

def carregar():
    global tarefa
    with open('banco_dados.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if (not(len(tarefa))):
                datetime_in_string = row[4]
                datetime_format = "%d/%m/%Y"
                dataEntrega = datetime.timestamp(datetime.strptime(datetime_in_string, datetime_format))
                tarefa.append(tarefas(int(row[0]),row[1],row[2],int(row[3]),dataEntrega))
            else:
                datetime_in_string = row[4]
                datetime_format = "%d/%m/%Y"
                dataEntrega = datetime.timestamp(datetime.strptime(datetime_in_string, datetime_format))
                tarefa.append(tarefas(int(tarefa[-1].getId())+1,row[1],row[2],int(row[3]),dataEntrega))
            line_count += 1
        print(f'Processed {line_count} lines.')

def salvar():
    with open('banco_dados.csv', mode='w',newline='') as data_file:
        data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for umatarefa in tarefa:
            data_writer.writerow([str(umatarefa.getId()), str(umatarefa.getTitulo()), str(umatarefa.getMateria()),str(umatarefa.getPontuacao()),str(umatarefa.getDataEntrega())])

def partition(array, start, end, compare_func):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and compare_func(array[high], pivot):
            high = high - 1

        while low <= high and not compare_func(array[low], pivot):
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high

def quick_sort(array, start, end, compare_func):
    if start >= end:
        return

    p = partition(array, start, end, compare_func)
    quick_sort(array, start, p-1, compare_func)
    quick_sort(array, p+1, end, compare_func)

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