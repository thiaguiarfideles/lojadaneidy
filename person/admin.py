from django.contrib import admin
from address.models import AddressField
from address.forms import AddressWidget
from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'address',
        'complemento',
        'cliente',
    )

    formfield_overrides = {
        AddressField: {
            'widget': AddressWidget(
                attrs={
                    'style': 'width: 300px;'
                }
            )
        }
    }
