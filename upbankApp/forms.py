from django import forms 
from .models import BariModel, BmgInssModel, BmgSiapeModel, ClienteModel, LoasModel, Marca, OleModel, PacotesModel, RefinModel, marcas, loas, especie, selecionar

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
    loas  = forms.CharField(widget=forms.RadioSelect(choices=loas))
    espécie = forms.CharField(widget=forms.RadioSelect(choices=especie))
    class Meta:
        model  = LoasModel
        fields = '__all__' 
        
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
    OLÉ = forms.CharField(widget=forms.RadioSelect(choices = selecionar))
    
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
        
