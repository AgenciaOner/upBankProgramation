from random import choice
from django.db import models

marcas = [
    ("1","green"),
    ("2","teste"),
    
]

class ClienteModel(models.Model):
    id   = models.AutoField(primary_key = True)
    nome_da_Empresa = models.CharField(max_length=128)

    

    def __str__(self):
        return self.nome

loas = [('nível brasil','Nível Brasil'),
         ('cidade','Cidade')]

especie=[('87 e 88','87 e 88'),
         ('só 87','só 87'),
         ('só 88','só 88')]         
class LoasModel(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(ClienteModel, on_delete=models.CASCADE, related_name="cliente")
    loas = models.CharField(max_length=100, choices=loas) 
    espécie  = models.CharField(max_length=100, choices = especie)

    def __str__(self):
        return self.loas 
selecionar =[('selecionado','Clique aqui')]    

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
    Troco_Acima_1000 = models.DecimalField(default= 0, max_digits = 100000, decimal_places= 2)
    
    
    def __str__(self):
        return "{}".format(self.REFIN) 

class OleModel(models.Model):
    RefinOle = models.ForeignKey(ClienteModel, on_delete = models.CASCADE, related_name = "oleCliente")   
    OLÉ = models.CharField(max_length=128, choices= selecionar)
    Troco_Acima_1000 = models.DecimalField(default= 0, max_digits = 100000, decimal_places= 2)
    
    
    def __str__(self):
        return "{}".format(self.OLE)

class BariModel(models.Model):
    RefinOle = models.ForeignKey(ClienteModel, on_delete = models.CASCADE, related_name = "bariCliente")   
    BARI = models.CharField(max_length=128, choices= selecionar)
    Venda_valor_acima_de_3000 = models.DecimalField(default= 0, max_digits = 100000, decimal_places= 2)
    
    
    def __str__(self):
        return "{}".format(self.BARI)                          
    
    
pacotes  = [('100-ENVIOS->R$ 59,90', '100-ENVIOS  -> R$ 59,90'),
            ('250-ENVIOS - R$ 99,90','250-ENVIOS - R$ 99,90'),
            ('250-ENVIOS - R$ 199,90','250-ENVIOS - R$ 199,90'),
            ('250-ENVIOS - R$ 299,90','250-ENVIOS - R$ 299,90'),
            ('250-ENVIOS - R$ 580,00','250-ENVIOS - R$ 580,00'),
            ('250-ENVIOS -  R$ 840,00','250-ENVIOS - R$ 840,00')]

class PacotesModel(models.Model):
    pacotesCliente = models.ForeignKey(ClienteModel, on_delete= models.CASCADE, related_name= "pacotesCliente")   
    pacotes = models.CharField(max_length =128, choices = pacotes)


class Marca(models.Model):
     marcaCliente = models.ForeignKey(ClienteModel, on_delete=models.CASCADE, related_name="marcaCliente")
     nome = models.CharField(max_length=100, choices=marcas)
     def __str__(self):
        return self.nome

