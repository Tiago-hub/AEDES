from classes import *
import csv
tarefa = []
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

carregar()

for umatarefa in tarefa:
        attrs = vars(umatarefa);
        print(attrs.items())

quick_sort(tarefa, 0, len(tarefa) - 1, lambda x, y: x.pontuacao > y.pontuacao)
for umatarefa in tarefa:
        attrs = vars(umatarefa);
        print(attrs.items())
