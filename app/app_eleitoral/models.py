from django.db import models
from django.contrib.auth.models import User

class Departamento(models.Model):
    nomeDep = models.CharField('Nome do Departamento:', max_length=255)
    numDep = models.CharField('Número do Departamento:', max_length=255)

    def __str__(self):
        return self.nomeDep

class Pessoa(models.Model):
    nome = models.CharField('Nome:', max_length=255)
    cpf = models.CharField('CPF:', max_length=255)
    pessoa = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null = True)

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.SET_NULL, blank=True, null=True)
    matricula = models.CharField('Matricula:', max_length=255)

    def __str__(self):
        return self.pessoa.nome



class Processo(models.Model):
    numProcesso = models.CharField('Número do Processo:', max_length=255)
    dep = models.ForeignKey(Departamento, on_delete=models.SET_NULL, blank=True, null=True)
    func = models.OneToOneField(Funcionario, on_delete=models.SET_NULL, blank=True, null=True)
    dataCriacao = models.DateTimeField('Data de Abertura:',auto_now_add=True)
    investigada = models.ManyToManyField(Pessoa,related_name = 'Investigados')
    interessada = models.ManyToManyField(Pessoa,related_name = 'Interessados')


    def __str__(self):
        return self.numProcesso

class Documento(models.Model):
    processo = models.ForeignKey(Processo, on_delete=models.SET_NULL, blank=True, null=True)
    dataCriacao = models.DateTimeField('Data de Abertura:', auto_now_add=True)
    numDoc = models.CharField('Número do documento:', max_length=255)
    titulo = models.CharField('Título:', max_length=255)
    descricao = models.TextField('Descrição do Documento:')
    func = models.OneToOneField(Funcionario, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.titulo

class Portaria(Documento):
    numPortaria = models.CharField('Número da Portaria de Instauração:', max_length=255)

    def __str__(self):
        return self.numPortaria


class Tramitacao(models.Model):
    processo = models.ForeignKey(Processo, on_delete=models.SET_NULL, blank=True, null=True)
    origemD =  models.ForeignKey(Departamento, on_delete = models.SET_NULL, blank = True, null = True, related_name = 'Destino:')
    dataD = models.ForeignKey(Departamento,on_delete= models.SET_NULL, blank = True, null = True)
    dataChegada = models.DateField('Data de Chegada:')
    dataSaida = models.DateField('Data de Saída:')

    def __str__(self):
        return 'Processo: {} '.format(self.processo.numProcesso)

class PedidoPrazo(Documento):
    justificativa = models.TextField('Justificativa de Prazo:')
    prazoAnterior = models.DateField('Prazo Anterior:')
    prazoNovo = models.DateField('Novo Prazo:')

    def __str__(self):
        return 'Processo: {} foi revogado para: {}.'.format(self.processo.numProcesso, self.prazoNovo.strftime("%d/%m/%y"))


class EnvioProcesso(Documento):
    dep = models.ForeignKey(Departamento, on_delete=models.SET_NULL, blank=True, null=True)
    dataEnvio = models.DateTimeField('Data de Envio:', auto_now_add=True)


    def __str__(self):
        return 'Processo: {}'.format(self.processo.numProcesso)




