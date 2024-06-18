
from django.contrib.auth.decorators import login_required
import re
from django import forms



class CreateOrderForm(forms.Form):
    phone_number = forms.CharField(label='Номер телефона', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '79991234567'}))

    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']
        

        if not data.isdigit():
            raise forms.ValidationError("Номер телефона должен содержать только цифры")
        
        pattern = re.compile(r'^\d{11}$')
        if not pattern.match(data):
            raise forms.ValidationError("Неверный формат номера")

        return data