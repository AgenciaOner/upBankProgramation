from django.db import models

from random import choice
from django.db import models
from django.db.models.deletion import CASCADE

marcas = [
    ("1","green"),
    ("2","teste"),
    
]

class ClienteModel(models.Model):
    id   = models.AutoField(primary_key = True)
    nome_da_Empresa = models.CharField(max_length=128)
    Email_da_Empresa = models.EmailField(max_length=128)
    telefone_da_Empresa = models.BigIntegerField()

    

    def __str__(self):
        return self.nome

loas = [('nível brasil','Nível Brasil'),
         ('cidade','Cidade')]

especie=[('87 e 88','87 e 88'),
         ('só 87','só 87'),
         ('só 88','só 88')]         

selecionar =[('selecionado','Clique aqui')] 


    
class LoasModel(models.Model):

    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(ClienteModel, on_delete=models.CASCADE, related_name="cliente")
    Brasil  = models.CharField(max_length=128, choices = selecionar)
    espécie  = models.CharField(max_length=100, choices = especie)

    def __str__(self):
        return self.loas 
estado= [('Acre (AC)',   'Acre (AC)'),
('Alagoas (AL)' , 'Alagoas (AL)'), 
('Amapá (AP)' ,  'Amapá (AP)'),
('Amazonas (AM)', 'Amazonas (AM)'),  
('Bahia (BA)', 'Bahia (BA)') ,
('Ceará (CE)' ,  'Ceará (CE)'), 
('Distrito Federal (DF)',  'Distrito Federal (DF)'),
('Espírito Santo (ES)' , 'Espírito Santo (ES)'),
('Goiás (GO)', 'Goiás (GO)'),  
('Maranhão (MA)', 'Maranhão (MA)'), 
('Mato Grosso (MT)', 'Mato Grosso (MT)'),
( 'Mato Grosso do Sul (MS)' , 'Mato Grosso do Sul (MS)'), 
('Minas Gerais (MG)',  'Minas Gerais (MG)'), 
('Pará (PA)', 'Pará (PA)'), 
( 'Paraíba (PB)', 'Paraíba (PB)'),
('Paraná (PR)',  'Paraná (PR)'), 
('Pernambuco (PE)', 'Pernambuco (PE)'),
('Piauí (PI)' , 'Piauí (PI)'), 
('Rio de Janeiro (RJ)', 'Rio de Janeiro (RJ)'), 
('Rio Grande do Norte (RN)', 'Rio Grande do Norte (RN)'),
('Rio Grande do Sul (RS)', 'Rio Grande do Sul (RS)'),
('Rondônia (RO)', 'Rondônia (RO)'), 
('Roraima (RR)', 'Roraima (RR)' ),
('Santa Catarina (SC)' ,  'Santa Catarina (SC)'), 
('São Paulo (SP)',  'São Paulo (SP)'),
('Sergipe (SE)',  'Sergipe (SE)'),
('Tocantins (TO)', 'Tocantins (TO)')]
 
class LoasCidadeModel(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(ClienteModel, on_delete=models.CASCADE, related_name="clienteCidade")
    Cidade  = models.CharField(max_length=128, choices = selecionar)
    estado = models.CharField(max_length=100, choices=estado)
    cidade = models.CharField(max_length=100) 
    espécie  = models.CharField(max_length=100, choices = especie)

    def __str__(self):
        return self.loas 
    
    
   

class BmgInssModel(models.Model):
    id = models.AutoField(primary_key=True)
    bmgCliente = models.ForeignKey(ClienteModel, on_delete=models.CASCADE, related_name="bmgCliente")
    INSS  = models.CharField(max_length=128, choices = selecionar)
    nivelBrasil =  models.CharField(max_length=128,  default="Nível Brasil")
    saqueAcimaMil = models.CharField(max_length=128, default="Saque acima de R$ 1000,00")
    variasEspécies =  models.CharField(max_length=182, default= "Várias espécies")
    
    def __str__(self):
        return "{} ".format(self.bmgCliente.nome)

class BmgSiapeModel(models.Model):
    BmgSiape = models.ForeignKey(ClienteModel, on_delete = models.CASCADE, related_name = "siapeCliente")   
    SIAPE = models.CharField(max_length=128, choices= selecionar)
    
    
    def __str__(self):
        return "{}".format(self.SIAPE)
    
class RefinModel(models.Model):
    RefinSiape = models.ForeignKey(ClienteModel, on_delete = models.CASCADE, related_name = "refinCliente")   
    REFIN = models.CharField(max_length=128, choices= selecionar)
    Troco_Acima_1000 = models.FloatField(default= 0)
    
    
    def __str__(self):
        return "{}".format(self.REFIN) 

class OleModel(models.Model):
    RefinOle = models.ForeignKey(ClienteModel, on_delete = models.CASCADE, related_name = "oleCliente")   
    OLE = models.CharField(max_length=128, choices= selecionar)
    Troco_Acima_1000 = models.FloatField(default= 0)
    
    
    def __str__(self):
        return "{}".format(self.OLE)

class BariModel(models.Model):
    RefinOle = models.ForeignKey(ClienteModel, on_delete = models.CASCADE, related_name = "bariCliente")   
    BARI = models.CharField(max_length=128, choices= selecionar)
    Venda_valor_acima_de_3000 = models.FloatField(default= 0)
    
    
    def __str__(self):
        return "{}".format(self.BARI)                          
    
    
pacotes  = [('100-CONTRATOS-R$ 70,00', '100-CONTRATOS->R$70,00'),
            ('200-CONTRATOS - R$ 120,00','200-CONTRATOS->R$120,00'),
            ('500-CONTRATOS - R$ 290,00','500-CONTRATOS->R$290,00'),
            ('750-CONTRATOS - R$ 420,00','750-CONTRATOS->R$420,00'),
            ('1000-CONTRATOS - R$ 520,00','1000-CONTRATOS->R$520,00'),
            ('1500-CONTRATOS -  R$ 740,00','1500-CONTRATOS->R$740,00'),
            ('3000-CONTRATOS -  R$ 1390,00','3000-CONTRATOS->R$1390,00')]

class PacotesModel(models.Model):
    pacotesCliente = models.ForeignKey(ClienteModel, on_delete= models.CASCADE, related_name= "pacotesCliente")   
    pacotes = models.CharField(max_length =128, choices = pacotes)


class Marca(models.Model):
     marcaCliente = models.ForeignKey(ClienteModel, on_delete=models.CASCADE, related_name="marcaCliente")
     nome = models.CharField(max_length=100, choices=marcas)
     def __str__(self):
        return self.nome
