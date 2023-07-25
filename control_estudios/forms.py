from django import forms
#crear formularios mediante api de django

class CursoFormulario(forms.Form):
   nombre = forms.CharField(required=True, max_length=64)
   comision = forms.IntegerField(required=True, max_value=50000)