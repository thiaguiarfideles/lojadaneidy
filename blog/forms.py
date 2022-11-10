from django.forms import ModelForm, ModelChoiceField
from django import forms

from blog.models import Post
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



class PostForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        my_fields = blog.objects.filter(usuario=user)
        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.form_id = 'id-blog-form'
        self.helper.form_method = 'post'
    # self.helper.form_action = reverse('index')
        self.helper.form_tag = False
        self.helper.form_class = 'blueForms'
        self.helper.layout = Layout(
        Div(
        Div(Field('title'), css_class="col-md-4", ),
        css_class="row", ),
        Div(
        Div(Field('content'), css_class="col-md-4", ),
        css_class="row", ),
        Div(
        Div(Field('image'), css_class="col-md-3", ),
        css_class="row", ),

        Submit('submit', 'Enviar', css_class='btn-success col-centered')
    )

    class Meta:
        model = Post
        exclude=['author']
        fields = ['title', 'content', 'image',]