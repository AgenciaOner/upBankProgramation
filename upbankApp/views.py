from email.mime import base
from lib2to3.pytree import Base
from sys import api_version
from tkinter.font import BOLD
from xmlrpc.client import boolean
from django.http import HttpResponse, HttpResponseRedirect

from upbankApp.models import BariModel, ClienteModel, BmgInssModel, LoasModel, BmgSiapeModel, OleModel, PacotesModel, RefinModel
from upbankApp.forms import BariForm, ClienteForm, LoasForm, BmgInssForm, BmgSiapeForm, ClienteVerificacao, OleForm, PacotesForm, RefinForm
from django.shortcuts import redirect, render
from django.forms.models import inlineformset_factory
from django.core.mail import EmailMultiAlternatives
import  pdfkit
from django.urls import reverse
import os

from django.core.mail import EmailMessage



def MandaEmail03(pdf):
      
    email = EmailMessage(
        'Subject here', 'Here is the message.', 'leonardosieds@gmail.com', ['leonardosieds@gmail.com'])
    email.attach_file(pdf)
    email.send()

def MandaEmail02(produto, cliente):
    nome  = cliente[0]
    email = cliente[1]
    telefone =cliente[2]
    produtos=produto[1:]
    troco = ""
    if 'Refin Itaú' in produto:
        troco = "troco acima de R$1000,00:"
    elif('Refin Olé' in produto):
        troco = "troco acima de R$1000,00:"
    elif('Port Bari' in produto):
        troco = "troco acima de R$3000,00:" 
    
    
               
    subject = 'Programação UpBank: ',nome 
    text_content =  produtos
    html_content = nome, telefone, troco, produtos
    
    produtos
    msg = EmailMultiAlternatives(subject, text_content, from_email=email, to=["leonardosieds@gmail.com"])
    msg.attach_alternative(html_content, "text/html")
    msg.send()    

globalDadosCliente = []
globalArrayProdutos = []


    
    
    
     

def UpBank(request):
 
    formDadosCliente = ClienteForm()
    cli = ClienteVerificacao()
     
    # fabrica de  formularios inline
    form_bari_factory = inlineformset_factory(ClienteModel, BariModel, form = BariForm, extra=1 , can_delete = False)
    bariFormView = form_bari_factory()
    
    form_ole_factory = inlineformset_factory(ClienteModel, OleModel, form = OleForm, extra=1 , can_delete = False)
    oleFormView = form_ole_factory()
    
    form_refin_factory = inlineformset_factory(ClienteModel, RefinModel, form = RefinForm, extra=1 , can_delete = False)
    refinFormView = form_refin_factory()
    
    
    form_siape_factory = inlineformset_factory(ClienteModel, BmgSiapeModel, form = BmgSiapeForm, extra=1 , can_delete = False)
    siapeFormView = form_siape_factory()
    
    form_bmgInss_factory = inlineformset_factory(ClienteModel,BmgInssModel, form = BmgInssForm, extra=1, can_delete = False)
    bmgInssFormView = form_bmgInss_factory()
    
    form_loas_factory = inlineformset_factory(ClienteModel, LoasModel, form= LoasForm, extra=1, can_delete=False)
    loasFormView = form_loas_factory()
    
    form_pacotes_factory = inlineformset_factory(ClienteModel, PacotesModel, form= PacotesForm, extra=1, can_delete=False)
    pacotesFormView = form_pacotes_factory()  
    
    context = {
        'Cliente':formDadosCliente,
        'loasForm':loasFormView,
        'bmgInssForm':bmgInssFormView,
        'siapeForm':siapeFormView,
        'refinForm':refinFormView,
        'oleForm':oleFormView,
        'bariForm':bariFormView,
        'pacoteForm':pacotesFormView
    }
    
    if request.method == "POST":
        #Dados cliente
        formDadosCliente = ClienteForm(request.POST)
        
        #Pacotes
        form_pacotes_factory = inlineformset_factory(ClienteModel, PacotesModel, form= PacotesForm, extra=1, can_delete=False)
        pacotesFormView = form_pacotes_factory(request.POST)
        if pacotesFormView.is_valid():
            pacotes = pacotesFormView.cleaned_data.pop().get('pacotes')
        
        #MANDAR EMAIL
        cli = ClienteVerificacao(request.POST)
        
        if cli.is_valid():
            
            
            return render(request, 'main/upBank-form.html', context)    
        
        
        #BARI
        form_bari_factory = inlineformset_factory(ClienteModel, BariModel, form = BariForm, extra=1 , can_delete = False)
        bariFormView = form_bari_factory(request.POST)
        if bariFormView.is_valid():
            bari = bariFormView.cleaned_data.pop().get('BARI')
            trocoBari = bariFormView.cleaned_data.pop().get('Venda_valor_acima_de_3000')
        
        #OLE
        form_ole_factory = inlineformset_factory(ClienteModel, OleModel, form = OleForm, extra=1 , can_delete = False)
        oleFormView = form_ole_factory(request.POST)
        
    
        if oleFormView.is_valid():
            ole = oleFormView.cleaned_data.pop().get('OLE')
            trocoOle = oleFormView.cleaned_data.pop().get('Troco_Acima_1000')
        
        #REFIN   
        form_refin_factory = inlineformset_factory(ClienteModel, RefinModel, form = RefinForm, extra=1 , can_delete = False)
        refinFormView = form_refin_factory(request.POST)
        if refinFormView.is_valid():
            refin = refinFormView.cleaned_data.pop().get('REFIN')
            troco =  refinFormView.cleaned_data.pop().get('Troco_Acima_1000') 
            
        
        #SIAPE
        form_siape_factory = inlineformset_factory(ClienteModel, BmgSiapeModel, form = BmgSiapeForm, extra=1 , can_delete = False)
        siapeFormView = form_siape_factory(request.POST)
        if siapeFormView.is_valid():
            siape = siapeFormView.cleaned_data.pop().get('SIAPE')
           
        
        #BmgInss
        form_bmgInss_factory = inlineformset_factory(ClienteModel,BmgInssModel, form = BmgInssForm, extra=1, can_delete = False)
        bmgInssFormView = form_bmgInss_factory(request.POST)
        if bmgInssFormView.is_valid():
            bmg = bmgInssFormView.cleaned_data.pop().get('INSS')
        
        #LOAS
        form_loas_factory = inlineformset_factory(ClienteModel, LoasModel, form = LoasForm, extra=1, can_delete = False)
        loasFormView = form_loas_factory(request.POST)
        if loasFormView.is_valid():
            loas = loasFormView.cleaned_data.pop().get('loas')
            especie = loasFormView.cleaned_data.pop().get('espécie')
       
        globalArrayProdutos.clear()       
        globalDadosCliente.clear()
        
        #BARI OK
        if bariFormView.is_valid() and formDadosCliente.is_valid() and bari != None and pacotes != None:

            globalArrayProdutos.clear()       
            globalDadosCliente.clear()
            nomeCliente  = formDadosCliente.data.get("nome_da_Empresa")
            email = formDadosCliente.data.get("Email_da_Empresa")
            telefone  =  formDadosCliente.data.get("telefone_da_Empresa")
            globalDadosCliente.append(nomeCliente)
            globalDadosCliente.append(email)
            globalDadosCliente.append(telefone)
            globalArrayProdutos.append('Port Bari')
            globalArrayProdutos.append(trocoBari)
            globalArrayProdutos.append('Nível Brasil')
            globalArrayProdutos.append('Várias Espécies')
            globalArrayProdutos.append('Várias Idades')
            globalArrayProdutos.append('Troco ao cliente acima R$ 500,00')
            globalArrayProdutos.append(pacotes)
            MandaEmail02(globalArrayProdutos, globalDadosCliente)
                       
            return render(request, 'main/termoContrato/bari-termos.html', {'nome':nomeCliente, 'email':email, 'telefone':telefone,  'cli':cli, 'bari':'Port Bari', 'troco':trocoBari,
            'nivelBrasil':'Nível Brasil', 'variasespecies':'Várias espécies', 'variasIdades': 'Várias Idades', 'trocoCliente':'Troco ao cliente acima R$500,00', 'pacotes':pacotes})
        
        #OLE OK
        elif oleFormView.is_valid() and formDadosCliente.is_valid() and ole != None and pacotes != None:
           
            globalArrayProdutos.clear()       
            globalDadosCliente.clear()
            nomeCliente  = formDadosCliente.data.get("nome_da_Empresa")
            email = formDadosCliente.data.get("Email_da_Empresa")
            telefone  =  formDadosCliente.data.get("telefone_da_Empresa")
        
            globalDadosCliente.append(nomeCliente)
            globalDadosCliente.append(email)
            globalDadosCliente.append(telefone)
            globalArrayProdutos.append('Refin Olé')
            globalArrayProdutos.append(trocoOle)
            globalArrayProdutos.append('Nível Brasil')
            globalArrayProdutos.append('Várias Espécies')
            globalArrayProdutos.append('Várias Idades')
            globalArrayProdutos.append(pacotes)
            MandaEmail02(globalArrayProdutos, globalDadosCliente)
                       
            return render(request, 'main/termoContrato/ole-termos.html', {'nome':nomeCliente, 'email':email, 'telefone':telefone, 'cli':cli, 'refimOle':'Refim Olé', 'troco':trocoOle,
            'nivelBrasil':'Nível Brasil', 'variasespecies':'Várias espécies', 'variasIdades': 'Várias Idades','pacotes':pacotes})
            
        
        #REFIN OK
        elif refinFormView.is_valid() and formDadosCliente.is_valid() and refin != None and pacotes != None:
            
            globalArrayProdutos.clear()       
            globalDadosCliente.clear()
            nomeCliente  = formDadosCliente.data.get("nome_da_Empresa")
            email = formDadosCliente.data.get("Email_da_Empresa")
            telefone  =  formDadosCliente.data.get("telefone_da_Empresa")
        
            globalDadosCliente.append(nomeCliente)
            globalDadosCliente.append(email)
            globalDadosCliente.append(telefone)
            globalArrayProdutos.append('Refin Itaú')
            globalArrayProdutos.append(troco)
            globalArrayProdutos.append('Nível Brasil')
            globalArrayProdutos.append('Várias Espécies')
            globalArrayProdutos.append('Várias Idades')
            globalArrayProdutos.append(pacotes)
            MandaEmail02(globalArrayProdutos, globalDadosCliente)
                       
            return render(request, 'main/termoContrato/refin-termos.html', {'nome':nomeCliente, 'email':email, 'telefone':telefone, 'cli':cli, 'refinItau':'Refin Itaú', 'troco':troco,
            'nivelBrasil':'Nível Brasil', 'variasespecies':'Várias espécies', 'variasIdades': 'Várias Idades','pacotes':pacotes})
            
        
        #SIAPE OK
        elif siapeFormView.is_valid() and formDadosCliente.is_valid() and siape != None and pacotes != None:
            
            globalArrayProdutos.clear()       
            globalDadosCliente.clear()
            nomeCliente  = formDadosCliente.data.get("nome_da_Empresa")
            email = formDadosCliente.data.get("Email_da_Empresa")
            telefone  =  formDadosCliente.data.get("telefone_da_Empresa")
        
            globalDadosCliente.append(nomeCliente)
            globalDadosCliente.append(email)
            globalDadosCliente.append(telefone)
            globalArrayProdutos.append('Saque Bmg Siape')
            globalArrayProdutos.append('Nível Brasil')
            globalArrayProdutos.append('Saque Acima de R$ 1000,00')
            globalArrayProdutos.append('Várias espécies')
            globalArrayProdutos.append(pacotes)
            MandaEmail02(globalArrayProdutos, globalDadosCliente)
                       
            return render(request, 'main/termoContrato/siape-termos.html', {'nome':nomeCliente, 'email':email, 'telefone':telefone, 'cli':cli, 'saquebmgsiape':'Saque Bmg Siape',
            'nivelBrasil':'Nível Brasil', 'saqueAcimaMil':'Saque acima de R$1000', 'variasespecies':'Várias espécies', 'pacotes':pacotes})
            
        #INSS    
        elif bmgInssFormView.is_valid() and formDadosCliente.is_valid() and bmg != None and pacotes!=None:
            
            
            
            globalDadosCliente.clear()
            globalArrayProdutos.clear()
            nomeCliente  = formDadosCliente.data.get("nome_da_Empresa")
            email = formDadosCliente.data.get("Email_da_Empresa")
            telefone  =  formDadosCliente.data.get("telefone_da_Empresa")
        
            globalDadosCliente.append(nomeCliente)
            globalDadosCliente.append(email)
            globalDadosCliente.append(telefone)
            globalArrayProdutos.append('Saque Bmg Inss')
            globalArrayProdutos.append('Nível Brasil')
            globalArrayProdutos.append('Saque Acima de R$ 1000,00')
            globalArrayProdutos.append('Várias espécies')
            globalArrayProdutos.append(pacotes)
            dicionario = {'nome':nomeCliente, 'email':email, 'telefone':telefone, 'saqueBmgInss':'Saque Bmg Inss',
            'nivelBrasil':'Nível Brasil', 'saqueAcimaMil':'Saque acima de R$1000', 'variasespecies':'Várias espécies', 'pacotes':pacotes, 'cli':cli}
            
            pdfkit.from_url('http://127.0.0.1:8000', 'out.pdf')
            MandaEmail03('out.pdf')
            os.remove('out.pdf')
            
            return render(request, 'main/termoContrato/BmgInss-termos.html', dicionario)
            #return redirect(reverse("bmg", kwargs = {'usuario':'leonardo souza'}))
            #return HttpResponseRedirect(reverse("bmg", kwargs = dicionario))

            #return HttpResponseRedirect(reverse('bmg', args = dicionario))
        #OK
        elif loasFormView.is_valid() and formDadosCliente.is_valid() and loas != None and pacotes!=None:
            
            
            globalDadosCliente.clear()
            globalArrayProdutos.clear()
            nomeCliente  = formDadosCliente.data.get("nome_da_Empresa")
            email = formDadosCliente.data.get("Email_da_Empresa")
            telefone  =  formDadosCliente.data.get("telefone_da_Empresa")
        
            globalDadosCliente.append(nomeCliente)
            globalDadosCliente.append(email)
            globalDadosCliente.append(telefone)
            globalArrayProdutos.append('Loas')
            globalArrayProdutos.append(loas)
            globalArrayProdutos.append(especie)
            globalArrayProdutos.append(pacotes)
            MandaEmail02(globalArrayProdutos, globalDadosCliente)
            return render(request, 'main/termoContrato/loas-termos.html', {'nome':nomeCliente, 'email':email, 'telefone':telefone, 'cli':cli, 'LOAS':'Loas',
            'loas': loas, 'especie': especie , 'pacotes':pacotes})
            
       
    
    
    
    return render(request, 'main/upBank-form.html', context  )