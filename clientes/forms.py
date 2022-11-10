from django.forms import ModelForm, ModelChoiceField
from django import forms

from clientes.models import Cad_Cliente, Info_cliente
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset
from crispy_forms.layout import Submit, Layout, Div, Fieldset
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab, InlineCheckboxes
from crispy_forms.helper import FormHelper

from crispy_forms.layout import Submit, Layout, Div, Fieldset

from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.urls import reverse
from django_select2.forms import (
    HeavySelect2MultipleWidget, HeavySelect2Widget, ModelSelect2MultipleWidget,
    ModelSelect2TagWidget, ModelSelect2Widget, Select2MultipleWidget,
    Select2Widget
)



class ClienteForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        my_field = Cad_Cliente.objects.filter(user=user)
        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-cliente-form'
        self.helper.form_method = 'post'
        # self.helper.form_action = reverse('index')
        self.helper.form_tag = False
        self.helper.form_class = 'blueForms'
        # self.fields["especialidades"].widget = forms.widgets.CheckboxSelectMultiple()
        self.helper.layout = Layout(
            Div(
                Div(Field('nm_cliente'), css_class="col-md-5", ),
                css_class="row", ),    
  
            Submit('submit', 'Enviar', css_class='btn-success col-centered')
        )
    class Meta:
        model = Cad_Cliente
        fields = ['nm_cliente',]


class Info_clienteForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(Info_clienteForm, self).__init__(*args, **kwargs)
        my_fields = Info_cliente.objects.filter(usuario=user)
        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-infocliente-form'
        self.helper.form_method = 'post'
    # self.helper.form_action = reverse('index')
        self.helper.form_tag = False
        self.helper.form_class = 'blueForms'
        self.helper.layout = Layout(
        Div(
        #Div(ModelChoiceField('paciente',required=False, queryset=Nome_paciente.objects.all()setup_field(Nome_paciente)), css_class="col-md-4", ),
        Div(Field('cliente'), css_class="col-md-4", ),
        Div(Field('email'), css_class="col-md-4", ),
        css_class="row", ),
        Div(
        Div(Field('ds_endereco'), css_class="col-md-4", ),
        Div(Field('cidade'), css_class="col-md-4", ),
        Div(Field('cep'), css_class="col-md-8", ),
        css_class="row", ),
        Div(
        Div(Field('idade'), css_class="col-md-3", ),
        Div(Field('sexo'), css_class="col-md-3", ),
        css_class="row", ),
        Div(
        Div(Field('telefone'), css_class="col-md-3", ),
        css_class="row", ),
        Div(
        Div(Field('comentarios'), css_class="col-md-3", ),
        css_class="row", ),

        Submit('submit', 'Enviar', css_class='btn-success col-centered')
    )

    class Meta:
        model = Info_cliente
        exclude=['usuario']
        fields = ['cliente', 'email', 'ds_endereco', 'cidade', 'cep', 'idade',
         'sexo', 'telefone', 'comentarios',]