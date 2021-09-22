from django.forms import ModelForm

from .models import make

class MakeForm(ModelForm):
    class Meta:
        model=make
        fields='__all__'