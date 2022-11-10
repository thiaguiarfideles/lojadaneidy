from django.forms import ModelForm
from django import forms
from person.models import Person
from address.forms import AddressField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset
from crispy_forms.layout import Submit, Layout, Div, Fieldset
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper

from crispy_forms.layout import Submit, Layout, Div, Fieldset

from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


  


class PersonForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        my_field = Person.objects.filter(user=user)
        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.form_id = 'id_cliente_form'
        self.helper.form_method = 'post'
        # self.helper.form_action = reverse('index')
        self.helper.form_tag = False
        self.helper.form_class = 'blueForms'
        self.helper.layout = Layout(
            Div(
                Div(Field('address'), css_class="col-md-5", ),
                Div(Field('complemento'), css_class="col-md-5", ),
                css_class="row", ),
            Div(
                Div(Field('cliente'), css_class="col-md-5", ),
                Div(Field('email'), css_class="col-md-5", ),
                css_class="row", ),
            Div(
                Div(Field('telefone'), css_class="col-md-3", ),
                Div(Field('sexo'), css_class="col-md-3", ),
                Div(Field('idade'), css_class="col-md-3", ),
                css_class="row", ),
            Submit('submit', 'Enviar', css_class='btn-success col-centered')
        )

    class Meta:
        model = Person
        exclude=['user', 'date_add',]
        fields = ['address', 'cliente','complemento', 'email', 'sexo', 'idade','telefone']