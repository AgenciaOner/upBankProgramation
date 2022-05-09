
from django.shortcuts import redirect

from upbankApp.models import BariModel, ClienteModel, BmgInssModel, LoasModel, LoasCidadeModel, BmgSiapeModel, OleModel, PacotesModel, RefinModel
from upbankApp.forms import BariForm, ClienteForm, LoasForm, LoasCidadeForm, BmgInssForm, BmgSiapeForm, ClienteVerificacao, OleForm, PacotesForm, RefinForm
from django.shortcuts import  render
from django.forms.models import inlineformset_factory
from django.core.mail import EmailMultiAlternatives
import  pdfkit
import os
from django.urls import reverse
from django.core.mail import EmailMessage

def MandaEmail03(pdf, produto, cliente):
    
    nome = cliente[0]
    email = cliente[1]
    produtos = produto[0:]
    email = EmailMessage(
        'Programação UpBank! '+ nome, produtos, email , ['leonardosieds@gmail.com'])
    email.attach_file(pdf)
    email.send()

globalDadosCliente = []
globalArrayProdutos = []

def bari(request):
            
    nome = globalDadosCliente[0]
    email = globalDadosCliente[1]
    telefone  = globalDadosCliente[2]
    bari = globalArrayProdutos[0]
    troco = globalArrayProdutos[1]
    nivel = globalArrayProdutos[2]
    especie = globalArrayProdutos[3]
    idades = globalArrayProdutos[4]
    trocoquinze = globalArrayProdutos[5]
    pacotes  = globalArrayProdutos[6]
        
    cli = ClienteVerificacao(request.POST)
    if cli.is_valid():
        pdfkit.from_url('http://127.0.0.1:8000/bari', 'contrato.pdf')
        MandaEmail03('contrato.pdf', globalArrayProdutos, globalDadosCliente)
        os.remove('contrato.pdf')
        return redirect('UpBank')
    
    dicionario = {'nome':nome, 'email':email, 'telefone':telefone,  'cli':cli, 'bari':bari, 'troco':troco,
            'nivelBrasil':nivel, 'variasespecies':especie, 'variasIdades': idades, 'trocoCliente': trocoquinze, 'pacotes':pacotes}
        
    return render(request, 'main/termoContrato/bari-termos.html', dicionario) 

def ole(request):
            
    nome = globalDadosCliente[0]
    email = globalDadosCliente[1]
    telefone  = globalDadosCliente[2]
    refinOle = globalArrayProdutos[0]
    troco = globalArrayProdutos[1]
    nivel = globalArrayProdutos[2]
    especie = globalArrayProdutos[3]
    idades = globalArrayProdutos[4]
    pacotes  = globalArrayProdutos[5]
 
    cli = ClienteVerificacao(request.POST)
    if cli.is_valid():
        pdfkit.from_url('http://127.0.0.1:8000/ole', 'contrato.pdf')
        MandaEmail03('contrato.pdf', globalArrayProdutos, globalDadosCliente)
        os.remove('contrato.pdf')
        return redirect('UpBank')
    
    dicionario =  {'nome':nome, 'email':email, 'telefone':telefone, 'cli':cli, 'refimOle':refinOle, 'troco':troco,
    'nivelBrasil':nivel, 'variasespecies':especie, 'variasIdades': idades,'pacotes':pacotes}
       
    return render(request, 'main/termoContrato/ole-termos.html', dicionario) 
 
def refin(request):
      
    nome = globalDadosCliente[0]
    email = globalDadosCliente[1]
    telefone  = globalDadosCliente[2]
    refinItau = globalArrayProdutos[0]
    troco = globalArrayProdutos[1]
    nivel = globalArrayProdutos[2]
    especie = globalArrayProdutos[3]
    idades = globalArrayProdutos[4]
    pacotes  = globalArrayProdutos[5]
        
    cli = ClienteVerificacao(request.POST)
    if cli.is_valid():
        pdfkit.from_url('http://127.0.0.1:8000/refin', 'contrato.pdf')
        MandaEmail03('contrato.pdf', globalArrayProdutos, globalDadosCliente)
        os.remove('contrato.pdf')
        return redirect('UpBank')
    
    dicionario =  {'nome':nome, 'email':email, 'telefone':telefone, 'cli':cli, 'refinItau':refinItau, 'troco':troco,
            'nivelBrasil': nivel, 'variasespecies':especie, 'variasIdades': idades,'pacotes':pacotes}   
   
    return render(request, 'main/termoContrato/refin-termos.html', dicionario)               


def siape(request):
        
    nome = globalDadosCliente[0]
    email = globalDadosCliente[1]
    telefone  = globalDadosCliente[2]
    saqueSiape = globalArrayProdutos[0]
    nivel = globalArrayProdutos[1]
    saqueMil = globalArrayProdutos[2]
    especie = globalArrayProdutos[3]
    pacotes = globalArrayProdutos[4]
    
    
    cli = ClienteVerificacao(request.POST)
    if cli.is_valid():
        pdfkit.from_url('http://127.0.0.1:8000/siape', 'contrato.pdf')
        MandaEmail03('contrato.pdf', globalArrayProdutos, globalDadosCliente)
        os.remove('contrato.pdf')
        return redirect('UpBank')
    
    dicionario = {'nome':nome, 'email':email, 'telefone':telefone,  'siape': saqueSiape, 
    'nivelBrasil':nivel, 'saqueAcimaMil': saqueMil, 'variasespecies': especie, 'pacotes':pacotes, 'cli':cli }
    
    return render(request, 'main/termoContrato/siape-termos.html', dicionario)       

def bmg(request):
    
    nome = globalDadosCliente[0]
    email = globalDadosCliente[1]
    telefone  = globalDadosCliente[2]
    saque = globalArrayProdutos[0]
    nivel = globalArrayProdutos[1]
    saqueMil = globalArrayProdutos[2]
    especie = globalArrayProdutos[3]
    pacotes = globalArrayProdutos[4]
    
    cli = ClienteVerificacao(request.POST)
    if cli.is_valid():
        pdfkit.from_url('http://127.0.0.1:8000/bmg', 'contrato.pdf')
        MandaEmail03('contrato.pdf', globalArrayProdutos, globalDadosCliente)
        os.remove('contrato.pdf')
        return redirect('UpBank')
    
    dicionario = {'nome':nome, 'email':email, 'telefone':telefone, 'saqueBmgInss': saque,
    'nivelBrasil':nivel, 'saqueAcimaMil':saqueMil, 'variasespecies':especie, 'pacotes':pacotes, 'cli':cli}
       
    return render(request, 'main/termoContrato/BmgInss-termos.html', dicionario)  
            
      
def loasCidade(request):
       
    nome = globalDadosCliente[0]
    email = globalDadosCliente[1]
    telefone  = globalDadosCliente[2]
    loasCidade = globalArrayProdutos[0]
    cidade  = globalArrayProdutos[1]
    estado  = globalArrayProdutos[2]
    especie = globalArrayProdutos[3]
    pacotes = globalArrayProdutos[4]
     
    cli = ClienteVerificacao(request.POST)
    if cli.is_valid():
        pdfkit.from_url('http://127.0.0.1:8000/loasCidade', 'contrato.pdf')
        MandaEmail03('contrato.pdf', globalArrayProdutos, globalDadosCliente)
        os.remove('contrato.pdf')
        return redirect('UpBank')
    dicionario = {'nome':nome, 'email':email, 'telefone':telefone, 'cli':cli, 'LOAS':loasCidade,
            'cidade': cidade, 'estado':estado, 'especie': especie , 'pacotes':pacotes}
    
    return render(request, 'main/termoContrato/loasCidade-termos.html', dicionario)   


def loasBrasil(request):
      
    nome = globalDadosCliente[0]
    email = globalDadosCliente[1]
    telefone  = globalDadosCliente[2]
    loas = globalArrayProdutos[0]
    especie = globalArrayProdutos[1]
    pacotes = globalArrayProdutos[2]
    
    cli = ClienteVerificacao(request.POST)
    if cli.is_valid():
        pdfkit.from_url('http://127.0.0.1:8000/loasBrasil', 'contrato.pdf')
        MandaEmail03('contrato.pdf', globalArrayProdutos, globalDadosCliente)
        os.remove('contrato.pdf')
        return redirect('UpBank')
    dicionario = {'nome':nome, 'email':email, 'telefone':telefone, 'cli':cli, 'LOAS':loas,
    'especie': especie , 'pacotes':pacotes}
    
    return render(request, 'main/termoContrato/loasBrasil-termos.html', dicionario)        



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
    
    form_pacotes_factory = inlineformset_factory(ClienteModel, PacotesModel, form= PacotesForm, extra=1, can_delete=False)
    pacotesFormView = form_pacotes_factory()  
    
    context = {
        'Cliente':formDadosCliente,
        'loasForm':loasFormView,
        'loasCidadeFormView':loasCidadeFormView,
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
        
        #LOAS CIDADE
        form_loasCidade_factory = inlineformset_factory(ClienteModel, LoasCidadeModel, form= LoasCidadeForm, extra=1, can_delete=False)
        loasCidadeFormView = form_loasCidade_factory(request.POST)
        boleo = loasCidadeFormView.is_valid()
        
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
            return redirect(reverse('bari'))
                       
         
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
            return redirect(reverse('ole'))
         
            
        
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
            return redirect(reverse('refin'))           
           
        
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
            
            return redirect(reverse('siape'))
           
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
            return redirect(reverse('bmg'))
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
            print('especie 3', globalArrayProdutos[3])

            globalArrayProdutos.append(pacotes)
            
            return redirect(reverse('loasCidade'))
        
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
            
            return redirect(reverse('loasBrasil'))
            
            
       
    
    
    
    return render(request, 'main/upBank-form.html', context  )