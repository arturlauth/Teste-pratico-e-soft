from bootstrap_datepicker_plus import DatePickerInput
from django import forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit
from cadastro.base.models import Pessoa


class CadastroForm(forms.ModelForm):
    nome = forms.CharField(max_length=100)
    sobrenome = forms.CharField(max_length=100)
    idade = forms.IntegerField(min_value=0, widget=forms.NumberInput)
    data_de_nascimento = forms.DateField(
        widget=DatePickerInput(format='%d/%m/%Y'))
    email = forms.EmailField()
    apelido = forms.CharField(max_length=100, required=False)
    obs = forms.CharField(widget=forms.Textarea, max_length=400, required=False)

    # An inline class to provide additional information on the form.
    class Meta:
         # Provide an association between the ModelForm and a model
         model = Pessoa
         fields = ('nome', 'sobrenome', 'idade', 'data_de_nascimento', 'email', 'apelido', 'obs')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'post'
    #     self.helper.add_input(Submit('submit', 'Save person'))
