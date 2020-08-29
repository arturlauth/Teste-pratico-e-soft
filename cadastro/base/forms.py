from bootstrap_datepicker_plus import DatePickerInput
from django import forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit


class CadastroForm(forms.Form):
    nome = forms.CharField(max_length=100)
    sobrenome = forms.CharField(max_length=100)
    idade = forms.IntegerField(min_value=0, widget=forms.NumberInput)
    data_de_nascimento = forms.DateField(
        widget=DatePickerInput(format='%m/%d/%Y'))
    email = forms.EmailField()
    apelido = forms.CharField(max_length=100)
    obs = forms.CharField(widget=forms.Textarea, max_length=400)

    # An inline class to provide additional information on the form.
    # class Meta:
    #     # Provide an association between the ModelForm and a model
    #     model = Category
    #     fields = ('name',)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'post'
    #     self.helper.add_input(Submit('submit', 'Save person'))
