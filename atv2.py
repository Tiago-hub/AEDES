from datetime import datetime
import csv
import time
tarefa = dict()
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
    
    dataEntrega=(dataInput.strftime('%d/%m/%Y'))
    tarefa.update({int(len(tarefa))+1:(int(len(tarefa))+1,titulo,materia,pontuacao,dataEntrega)})
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
            print('')
            print('Lista de trabalhos (ordenada por id)')
            print('--------------------------------------------------------------------------------------------------------')
            start_time = time.time()
            pontuacao = dict()
            for entrada in tarefa.values():
                pontuacao.update({tuple(entrada)[0]:tuple(entrada)[0]})
            sorted_d = sorted(pontuacao.items(), key=lambda x: x[1])
            for x in sorted_d:
                print(tarefa[x[0]])
            print("--- %s seconds ---" % (time.time() - start_time))
        elif(resposta=='data'):
            print('')
            print('Lista de trabalhos (ordenada por data de entrega)')
            print('--------------------------------------------------------------------------------------------------------')
            start_time = time.time()
            pontuacao = dict()
            for entrada in tarefa.values():
                datetime_in_string = tuple(entrada)[4]
                datetime_format = "%d/%m/%Y"
                dataEntrega = datetime.timestamp(datetime.strptime(datetime_in_string, datetime_format))
                pontuacao.update({tuple(entrada)[0]:dataEntrega})
            sorted_d = sorted(pontuacao.items(), key=lambda x: x[1])
            for x in sorted_d:
                print(tarefa[x[0]])
            print("--- %s seconds ---" % (time.time() - start_time))
        elif(resposta=='pontos'):
            print('')
            print('Lista de trabalhos (ordenada por pontuação)')
            print('--------------------------------------------------------------------------------------------------------')
            start_time = time.time()
            pontuacao = dict()
            for entrada in tarefa.values():
                pontuacao.update({tuple(entrada)[0]:tuple(entrada)[3]})
            sorted_d = sorted(pontuacao.items(), key=lambda x: x[1])
            for x in sorted_d:
                print(tarefa[x[0]])
            print("--- %s seconds ---" % (time.time() - start_time))
        else:
            print('opção inválida')
def excluir ():
    global tarefa
    print('Digite a id da tarefa que deseja deletar')
    idTarefa = int(input())
    tarefa.pop(idTarefa)

def carregar():
    global tarefa
    with open('banco_dados.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if (not(len(tarefa))):
                #datetime_in_string = row[4]
                #datetime_format = "%d/%m/%Y"
                #dataEntrega = datetime.timestamp(datetime.strptime(datetime_in_string, datetime_format))
                dataEntrega = row[4]
                tarefa.update({int(row[0]):(int(row[0]),row[1],row[2],int(row[3]),dataEntrega)})
            else:
                #datetime_in_string = row[4]
                #datetime_format = "%d/%m/%Y"
                #dataEntrega = datetime.timestamp(datetime.strptime(datetime_in_string, datetime_format))
                dataEntrega = row[4]
                tarefa.update({int(len(tarefa))+1:(int(len(tarefa))+1,row[1],row[2],int(row[3]),dataEntrega)})
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