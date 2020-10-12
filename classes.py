class tarefas:

    def __init__(self,id,titulo,materia,pontuacao,dataEntrega):
        self.id=id
        self.titulo=titulo
        self.materia=materia
        self.pontuacao=pontuacao
        self.dataEntrega=dataEntrega

    def getTitulo(self):
        return self.titulo 
    
    def getMateria(self):
        return self.materia

    def getPontuacao(self):
        return self.pontuacao

    def getDataEntrega(self):
        return self.dataEntrega
    
    def getId(self):
        return self.id