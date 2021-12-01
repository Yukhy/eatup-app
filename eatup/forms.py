from django import forms
from django.forms import fields
from .models import *
from pos.models import *

class ScanItemForm(forms.Form):
    pos_id = forms.CharField(max_length=40, required=True)

    def __init__(self, *args, **kwargs):
        super(ScanItemForm, self).__init__(*args, **kwargs)
        
    
    def get_scanning_pos_id(self):
        return self.data['pos_id']

class AddCartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['user', 'pos']

    def __init__(self, *args, **kwargs):
        super(AddCartForm, self).__init__(*args, **kwargs)