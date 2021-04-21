from django import forms

class formulario_contacto(forms.Form):

    camp_asunto = forms.CharField()
    camp_correo = forms.EmailField()
    camp_mensaj = forms.CharField()