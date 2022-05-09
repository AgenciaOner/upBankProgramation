from django import forms 
from .models import BariModel, BmgInssModel, BmgSiapeModel, ClienteModel, LoasCidadeModel, LoasModel, Marca, OleModel, PacotesModel, RefinModel, marcas, especie, selecionar

class MarcaForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.RadioSelect(choices=marcas))
    class Meta:
        model = Marca
        fields = ['nome'] 

class ClienteForm(forms.ModelForm):
    class Meta:
        model  = ClienteModel
        fields = '__all__'

class LoasForm(forms.ModelForm):
    Brasil  = forms.CharField(widget=forms.RadioSelect(choices=selecionar))
    espécie = forms.CharField(widget=forms.RadioSelect(choices=especie))
    class Meta:
        model  = LoasModel
        fields = '__all__' 
class LoasCidadeForm(forms.ModelForm):
    Cidade  = forms.CharField(widget=forms.RadioSelect(choices=selecionar))
    espécie = forms.CharField(widget=forms.RadioSelect(choices=especie))
    class Meta:
        model = LoasCidadeModel
        fields ='__all__' 


        
class BmgInssForm(forms.ModelForm):
    INSS = forms.CharField(widget=forms.RadioSelect(choices=selecionar))
    class Meta:
        model  = BmgInssModel
        fields = ['INSS']         
   
class BmgSiapeForm(forms.ModelForm):
    SIAPE = forms.CharField(widget=forms.RadioSelect(choices = selecionar))
    class Meta:
        model = BmgSiapeModel
        fields = ['SIAPE']
        
class RefinForm(forms.ModelForm):
    REFIN = forms.CharField(widget=forms.RadioSelect(choices = selecionar))
    
    class Meta:
        model = RefinModel
        fields = '__all__'

class OleForm(forms.ModelForm):
    OLE = forms.CharField(widget=forms.RadioSelect(choices = selecionar))
    class Meta:
        model = OleModel
        fields = '__all__'
        
class BariForm(forms.ModelForm):
    BARI = forms.CharField(widget=forms.RadioSelect(choices = selecionar))
    
    class Meta:
        model = BariModel
        fields = '__all__'                        
                
class PacotesForm(forms.ModelForm):
    class  Meta:
        model  = PacotesModel 
        fields = '__all__'


selector = [('sou cliente','Sou cliente'),
            ('não sou cliente','Não sou cliente')]   
class ClienteVerificacao(forms.Form):
    selecione = forms.ChoiceField(choices=selector, widget=forms.RadioSelect)



        
