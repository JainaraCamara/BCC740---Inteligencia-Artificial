class Usuario:

    seq = 0 #contador inicial
    objects = [] #tupla vazia

    def __init__(self, nome, idade): #Valor inicial atribuído aos atributos
        self.id = None #instância criada, mas não foi salva
        self.nome = nome
        self.idade = idade
    
    def save(self): #Salva os dados
        self.__class__.seq += 1  #Acessa a classe que criou a instância
        self.id = self.__class__.seq
        self.__class__.objects.append(self)
    
    def __str__(self): #Retorna representação do objeto como str
        return self.nome
    
    def __repr__(self): #Retorna representação do objeto usada para outros objetos
        return "<{}: {} - {} - {}>\n".format(self.__class__.__name__, self.id, self.nome, self.idade)
    
    @classmethod #Acessa todas as instâncias salvas
    def all(cls):
        return cls.objects

#Demonstrando o uso da classe:

x = 1
while x != 0:
    usname = input("Digite o nome: ")
    usage = int(input("Digite a idade: "))
    newus = Usuario(usname, usage)
    newus.save()
    
    x = int(input("Para sair digite 0, ou digite 1 para continuar: "))
print(Usuario.all())