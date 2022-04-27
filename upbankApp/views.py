from django.http import HttpResponse

from upbankApp.models import BariModel, ClienteModel, BmgInssModel, LoasModel, BmgSiapeModel, OleModel, PacotesModel, RefinModel
from .forms import BariForm, ClienteForm, LoasForm, BmgInssForm, BmgSiapeForm, ClienteVerificacao, OleForm, PacotesForm, RefinForm
from django.shortcuts import render
from django.forms.models import inlineformset_factory
from django.core.mail import EmailMultiAlternatives


def MandaEmail(produto, cliente, verificacaoSecliente):
    nome  = cliente[0]
    print("nome ",nome)
    produtos=produto[1:]
    troco = ""
    if 'Refin Itaú' in produto:
        troco = "troco acima de R$1000,00:"
    elif('Refin Olé' in produto):
        troco = "troco acima de R$1000,00:"
    elif('Port Bari' in produto):
        troco = "troco acima de R$3000,00:"    
               
    subject = 'Olá me chamo', nome,',', verificacaoSecliente, ", e  gostaria do produto", produto[0]
    text_content =  produtos
    html_content = troco, produtos
    
    produtos
    msg = EmailMultiAlternatives(subject, text_content, from_email="mail@gmail.com", to=["leonardosieds@gmail.com"])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    
global loas, especie, pacotes 
global refin, troco
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
        nomeCliente  = formDadosCliente.data.get("nome_da_Empresa")
        
        
        #verificação para ver se é cliente
        cli = ClienteVerificacao(request.POST)
        
        #Pacotes
        form_pacotes_factory = inlineformset_factory(ClienteModel, PacotesModel, form= PacotesForm, extra=1, can_delete=False)
        pacotesFormView = form_pacotes_factory(request.POST)
        if pacotesFormView.is_valid():
            pacotes = pacotesFormView.cleaned_data.pop().get('pacotes')
        
         
        if cli.is_valid():
            verificacaoSecliente = cli.data.get('selecione')
            MandaEmail(globalArrayProdutos, globalDadosCliente, verificacaoSecliente)
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
       
        #OK
        if bariFormView.is_valid() and formDadosCliente.is_valid() and bari != None and pacotes != None:
            print("entrou bari")
            globalArrayProdutos.clear()       
            globalDadosCliente.clear()
            globalDadosCliente.append(nomeCliente)
            globalArrayProdutos.append('Port Bari')
            globalArrayProdutos.append(trocoBari)
            globalArrayProdutos.append('Nível Brasil')
            globalArrayProdutos.append('Várias Espécies')
            globalArrayProdutos.append('Várias Idades')
            globalArrayProdutos.append('Troco ao cliente acima R$ 500,00')
            globalArrayProdutos.append(pacotes)
                       
            return render(request, 'main/termoContrato/bari-termos.html', {'nome':nomeCliente, 'cli':cli, 'bari':'Port Bari', 'troco':trocoBari,
            'nivelBrasil':'Nível Brasil', 'variasespecies':'Várias espécies', 'variasIdades': 'Várias Idades', 'trocoCliente':'Troco ao cliente acima R$500,00', 'pacotes':pacotes})
        
        #rever
        elif oleFormView.is_valid() and formDadosCliente.is_valid() and ole != None and pacotes != None:
            globalArrayProdutos.clear()       
            globalDadosCliente.clear()
            globalDadosCliente.append(nomeCliente)
            globalArrayProdutos.append('Refin Olé')
            globalArrayProdutos.append(trocoOle)
            globalArrayProdutos.append('Nível Brasil')
            globalArrayProdutos.append('Várias Espécies')
            globalArrayProdutos.append('Várias Idades')
            globalArrayProdutos.append(pacotes)
                       
            return render(request, 'main/termoContrato/ole-termos.html', {'nome':nomeCliente, 'cli':cli, 'oleItau':'Ole Itaú', 'troco':trocoOle,
            'nivelBrasil':'Nível Brasil', 'variasespecies':'Várias espécies', 'variasIdades': 'Várias Idades','pacotes':pacotes})
            
        
        #rever 
        elif refinFormView.is_valid() and formDadosCliente.is_valid() and refin != None and pacotes != None:
            globalArrayProdutos.clear()       
            globalDadosCliente.clear()
            globalDadosCliente.append(nomeCliente)
            globalArrayProdutos.append('Refin Itaú')
            globalArrayProdutos.append(troco)
            globalArrayProdutos.append('Nível Brasil')
            globalArrayProdutos.append('Várias Espécies')
            globalArrayProdutos.append('Várias Idades')
            globalArrayProdutos.append(pacotes)
                       
            return render(request, 'main/termoContrato/refin-termos.html', {'nome':nomeCliente, 'cli':cli, 'refinItau':'Refin Itaú', 'troco':troco,
            'nivelBrasil':'Nível Brasil', 'variasespecies':'Várias espécies', 'variasIdades': 'Várias Idades','pacotes':pacotes})
            
        
        #rever 
        elif siapeFormView.is_valid() and formDadosCliente.is_valid() and siape != None and pacotes != None:
            globalArrayProdutos.clear()       
            globalDadosCliente.clear()
            globalDadosCliente.append(nomeCliente)
            globalArrayProdutos.append('Saque Bmg Siape')
            globalArrayProdutos.append('Nível Brasil')
            globalArrayProdutos.append('Saque Acima de R$ 1000,00')
            globalArrayProdutos.append('Várias espécies')
            globalArrayProdutos.append(pacotes)
                       
            return render(request, 'main/termoContrato/siape-termos.html', {'nome':nomeCliente, 'cli':cli, 'saquebmgsiape':'Saque Bmg Siape',
            'nivelBrasil':'Nível Brasil', 'saqueAcimaMil':'Saque acima de R$1000', 'variasespecies':'Várias espécies', 'pacotes':pacotes})
            
        #rever    
        elif bmgInssFormView.is_valid() and formDadosCliente.is_valid() and bmg != None and pacotes!=None:
            globalArrayProdutos.clear()       
            globalDadosCliente.clear()
            globalDadosCliente.append(nomeCliente)
            globalArrayProdutos.append('Saque Bmg Inss')
            globalArrayProdutos.append('Nível Brasil')
            globalArrayProdutos.append('Saque Acima de R$ 1000,00')
            globalArrayProdutos.append('Várias espécies')
            globalArrayProdutos.append(pacotes)
                       
            return render(request, 'main/termoContrato/BmgInss-termos.html', {'nome':nomeCliente, 'cli':cli, 'saqueBmgInss':'Saque Bmg Inss',
            'nivelBrasil':'Nível Brasil', 'saqueAcimaMil':'Saque acima de R$1000', 'variasespecies':'Várias espécies'})
            
        #rever
        elif loasFormView.is_valid() and formDadosCliente.is_valid() and loas != None and pacotes!=None:
            globalArrayProdutos.clear()
            globalDadosCliente.clear()
            globalDadosCliente.append(nomeCliente)
            globalArrayProdutos.append('Loas')
            globalArrayProdutos.append(loas)
            globalArrayProdutos.append(especie)
                                   
            return render(request, 'main/termoContrato/loas-termos.html', {'nome':nomeCliente, 'cli':cli,
            'loas': loas, 'especie': especie})
            
       
    
    
    
    return render(request, 'main/upBank-form.html', context  )