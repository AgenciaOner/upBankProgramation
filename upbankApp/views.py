from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from upbankApp.models import BariModel, ClienteModel, BmgInssModel, LoasModel, LoasCidadeModel, BmgSiapeModel, OleModel, PacotesModel, RefinModel, RefinBmgModel, RefinDaycovalModel 
from upbankApp.forms import BariForm, ClienteForm, LoasForm, LoasCidadeForm, BmgInssForm, BmgSiapeForm, ClienteVerificacao, OleForm, PacotesForm, RefinForm, RefinBmgForm, RefinDaycovalForm
from django.shortcuts import  render
from django.forms.models import inlineformset_factory
import time
from django.urls import reverse
from django.core.mail import EmailMessage
from pathlib import Path

#fpath = Path('/usr/bin/wkhtmltopdf').absolute()

def MandaEmail02(produto, cliente):
    
    
    nome = cliente[0]
    email = cliente[1]
    telefone = cliente[2]
    produtos = produto[0:]
    
    email = EmailMessage(
        'Programação UpBank! '+ nome+', telefone: '+ telefone, produtos, email , ['upbankvendas@gmail.com'])
    email.attach_file('contrato.png')
    email.send()

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
    
    form_loasCidade_factory = inlineformset_factory(ClienteModel, LoasCidadeModel, form= LoasCidadeForm, extra=1, can_delete=False)
    loasCidadeFormView = form_loasCidade_factory()
        
    form_loas_factory = inlineformset_factory(ClienteModel, LoasModel, form= LoasForm, extra=1, can_delete=False)
    loasFormView = form_loas_factory()
    
    #REFINBMG
    form_refinBmg_factory = inlineformset_factory(ClienteModel, RefinBmgModel, form= RefinBmgForm , extra=1, can_delete=False)
    refinBmgView = form_refinBmg_factory()
    
    #DAYCOVAL
    form_daycoval_factory = inlineformset_factory(ClienteModel, RefinDaycovalModel, form= RefinDaycovalForm , extra=1, can_delete=False)
    daycovalView = form_daycoval_factory()
    
    form_pacotes_factory = inlineformset_factory(ClienteModel, PacotesModel, form= PacotesForm, extra=1, can_delete=False)
    pacotesFormView = form_pacotes_factory()  
    
    context = {
        'Cliente':formDadosCliente,
        'loasForm':loasFormView,
        'loasCidadeFormView':loasCidadeFormView,
        'bmgInssForm':bmgInssFormView,
        'siapeForm':siapeFormView,
        'refinForm':refinFormView,
        'refinBmg':refinBmgView,
        'refinDaycoval':daycovalView,
        'oleForm':oleFormView,
        'bariForm':bariFormView,
        'pacoteForm':pacotesFormView
    }
   
    
    #MANDAR EMAIL
    cli = ClienteVerificacao(request.POST)
    
    if request.method == "POST":
        
        if cli.is_valid():
            MandaEmail02(globalArrayProdutos, globalDadosCliente)
            globalArrayProdutos.clear()       
            globalDadosCliente.clear()
            #return redirect(reverse("UpBank"))
            return render(request, 'main/upBank-form.html', context)  
        
        
        #Dados cliente
        formDadosCliente = ClienteForm(request.POST)
        
        #Pacotes
        form_pacotes_factory = inlineformset_factory(ClienteModel, PacotesModel, form= PacotesForm, extra=1, can_delete=False)
        pacotesFormView = form_pacotes_factory(request.POST)
        if pacotesFormView.is_valid():
            pacotes = pacotesFormView.cleaned_data.pop().get('pacotes')
               
        #BARI
        form_bari_factory = inlineformset_factory(ClienteModel, BariModel, form = BariForm, extra=1 , can_delete = False)
        bariFormView = form_bari_factory(request.POST)
        if bariFormView.is_valid():
            bari = bariFormView.cleaned_data.pop().get('BARI')
            trocoBari = bariFormView.cleaned_data.pop().get('Venda_valor_acima_de_3000')
            
        #REFIN BMG
        form_refinBmg_factory = inlineformset_factory(ClienteModel, RefinBmgModel, form= RefinBmgForm , extra=1, can_delete=False)
        refinBmgView = form_refinBmg_factory(request.POST)
        if refinBmgView.is_valid():
            bmg = refinBmgView.cleaned_data.pop().get('BMG')
        
        #DAYCOVAL
        form_daycoval_factory = inlineformset_factory(ClienteModel, RefinDaycovalModel, form= RefinDaycovalForm , extra=1, can_delete=False)
        daycovalView = form_daycoval_factory(request.POST)
        if daycovalView.is_valid():
            daycoval = daycovalView.cleaned_data.pop().get('DAYCOVAL')    
        
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
            trocoItau =  refinFormView.cleaned_data.pop().get('Troco_Acima_1000') 
            
        
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
        
        #LOAS CIDADE
        form_loasCidade_factory = inlineformset_factory(ClienteModel, LoasCidadeModel, form= LoasCidadeForm, extra=1, can_delete=False)
        loasCidadeFormView = form_loasCidade_factory(request.POST)
       
        
        if loasCidadeFormView.is_valid():
            cidadeCaptura = loasCidadeFormView.cleaned_data.pop().get('Cidade')
            cidade  = loasCidadeFormView.cleaned_data.pop().get('cidade')
            estado  = loasCidadeFormView.cleaned_data.pop().get('estado')
            especieCidade = loasCidadeFormView.cleaned_data.pop().get('espécie')
            
        
        #LOAS BRASIL
        form_loas_factory = inlineformset_factory(ClienteModel, LoasModel, form = LoasForm, extra=1, can_delete = False)
        loasFormView = form_loas_factory(request.POST)
              
        if loasFormView.is_valid():
           
            loas = loasFormView.cleaned_data.pop().get('Brasil')
            especie = loasFormView.cleaned_data.pop().get('espécie')
            
        globalArrayProdutos.clear()       
        globalDadosCliente.clear()
        time.sleep(0.5)
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
            time.sleep(0.2)
            dicionario = {'nome':nomeCliente, 'email':email, 'telefone':telefone,  'cli':cli, 'bari':'Bari', 'troco':trocoBari,
            'nivelBrasil':'Nivel Brasil', 'variasespecies':'Várias Espécies', 'variasIdades': 'Várias Idades', 'trocoCliente': 'Troco ao cliente acima R$ 500,00', 'pacotes':pacotes}
        
            return render(request, 'main/termoContrato/bari-termos.html', dicionario)
            #return HttpResponseRedirect(reverse('bari'))
            #return redirect(reverse('bari'))
        
        
        elif refinBmgView.is_valid() and formDadosCliente.is_valid() and bmg != None and pacotes!=None:
              
            
            nomeCliente  = formDadosCliente.data.get("nome_da_Empresa")
            email = formDadosCliente.data.get("Email_da_Empresa")
            telefone  =  formDadosCliente.data.get("telefone_da_Empresa")

            globalDadosCliente.append(nomeCliente)
            globalDadosCliente.append(email)
            globalDadosCliente.append(telefone)
            globalArrayProdutos.append('Refin Bmg')
            globalArrayProdutos.append('Nível Brasil')
            globalArrayProdutos.append('Saque Acima de R$ 1000,00')
            globalArrayProdutos.append('Várias espécies')
            globalArrayProdutos.append(pacotes)
            dicionario = {'nome':nomeCliente, 'email':email, 'telefone':telefone,  'cli':cli, 'pacotes':pacotes}
        
            return render(request, 'main/termoContrato/refinBmg-termos.html', dicionario) 
        
        #DAYCOVAL
        elif daycovalView.is_valid() and formDadosCliente.is_valid() and  daycoval != None and pacotes!=None:
              
            
            nomeCliente  = formDadosCliente.data.get("nome_da_Empresa")
            email = formDadosCliente.data.get("Email_da_Empresa")
            telefone  =  formDadosCliente.data.get("telefone_da_Empresa")

            globalDadosCliente.append(nomeCliente)
            globalDadosCliente.append(email)
            globalDadosCliente.append(telefone)
            globalArrayProdutos.append('Refin Bmg')
            globalArrayProdutos.append('Nível Brasil')
            globalArrayProdutos.append('Saque Acima de R$ 1000,00')
            globalArrayProdutos.append('Várias espécies')
            globalArrayProdutos.append(pacotes)
            dicionario = {'nome':nomeCliente, 'email':email, 'telefone':telefone,  'cli':cli, 'pacotes':pacotes}
        
            return render(request, 'main/termoContrato/daycoval-termos.html', dicionario) 
         
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
            dicionario =  {'nome':nomeCliente, 'email':email, 'telefone':telefone, 'cli':cli, 'refimOle':'Refin Olé', 'troco':trocoOle,
            'nivelBrasil':'Nível Brasil', 'variasespecies':'Várias Espécies', 'variasIdades': 'Várias Idades','pacotes':pacotes}
            return render(request, 'main/termoContrato/ole-termos.html', dicionario)
             
            
        
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
            globalArrayProdutos.append(trocoItau)
            globalArrayProdutos.append('Nível Brasil')
            globalArrayProdutos.append('Várias Espécies')
            globalArrayProdutos.append('Várias Idades')
            globalArrayProdutos.append(pacotes)
            dicionario =  {'nome':nomeCliente, 'email':email, 'telefone':telefone, 'cli':cli, 'refinItau':'Refin Itaú', 'troco':trocoItau,
            'nivelBrasil': 'Nível Brasil', 'variasespecies':'Várias espécies', 'variasIdades': 'Várias Idades','pacotes':pacotes} 

            return render(request, 'main/termoContrato/refin-termos.html', dicionario)
        
           
        
        #SIAPE 
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
            dicionario = {'nome':nomeCliente, 'email':email, 'telefone':telefone,  'siape': 'Saque Siape', 
            'nivelBrasil':'Nivel Brasil', 'saqueAcimaMil': 'Saque Acima de mil', 'variasespecies': 'Várias Espécies', 'pacotes':pacotes, 'cli':cli }
    
            return render(request, 'main/termoContrato/siape-termos.html', dicionario)

           
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
            dicionario = {'nome':nomeCliente, 'email':email, 'telefone':telefone, 'saqueBmgInss': 'Saque Bmg Inss',
            'nivelBrasil':'Nível Brasil', 'saqueAcimaMil':'Saque acima de mil', 'variasespecies':'Várias Espécies', 'pacotes':pacotes, 'cli':cli}
       
            return render(request, 'main/termoContrato/BmgInss-termos.html', dicionario)  
            
            
            #return redirect(reverse('bmg'))
            #return HttpResponseRedirect(reverse('bmg'))
            #return redirect(reverse("bmg"))
            #return render(request, 'main/termoContrato/BmgInss-termos.html', dicionario)
            #return HttpResponseRedirect(reverse("bmg", kwargs = dicionario))
            #return HttpResponseRedirect(reverse('bmg', args = dicionario))
        
        
        
        #LOAS CIDADE
        elif loasCidadeFormView.is_valid() and formDadosCliente.is_valid() and cidadeCaptura != None and pacotes!=None:
            
            
            globalDadosCliente.clear()
            globalArrayProdutos.clear()
            nomeCliente  = formDadosCliente.data.get("nome_da_Empresa")
            email = formDadosCliente.data.get("Email_da_Empresa")
            telefone  =  formDadosCliente.data.get("telefone_da_Empresa")
        
            globalDadosCliente.append(nomeCliente)
            globalDadosCliente.append(email)
            globalDadosCliente.append(telefone)
            globalArrayProdutos.append('Loas Cidade')
            
            globalArrayProdutos.append(cidade)
            globalArrayProdutos.append(estado)
            globalArrayProdutos.append(especieCidade)
            globalArrayProdutos.append(pacotes)
            
            dicionario = {'nome':nomeCliente, 'email':email, 'telefone':telefone, 'cli':cli, 'LOAS':'Loas Cidade',
            'cidade': cidade, 'estado':estado, 'especie': especieCidade , 'pacotes':pacotes}
    
            return render(request, 'main/termoContrato/loasCidade-termos.html', dicionario) 
        
        #LOAS BRASIL
        elif loasFormView.is_valid() and formDadosCliente.is_valid() and loas != None and pacotes!=None:
            
            
            globalDadosCliente.clear()
            globalArrayProdutos.clear()
            nomeCliente  = formDadosCliente.data.get("nome_da_Empresa")
            email = formDadosCliente.data.get("Email_da_Empresa")
            telefone  =  formDadosCliente.data.get("telefone_da_Empresa")
        
            globalDadosCliente.append(nomeCliente)
            globalDadosCliente.append(email)
            globalDadosCliente.append(telefone)
            globalArrayProdutos.append('Loas Brasil')
            globalArrayProdutos.append(especie)
            globalArrayProdutos.append(pacotes)
            dicionario = {'nome':nomeCliente, 'email':email, 'telefone':telefone, 'cli':cli, 'LOAS':'Loas Brasil',
            'especie': especie , 'pacotes':pacotes}
    
            return render(request, 'main/termoContrato/loasBrasil-termos.html', dicionario)      
            
            
       
    return render(request, 'main/upBank-form.html', context  )
