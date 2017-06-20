from django import forms

from .models import Subscriber

class SubscribeForm(forms.ModelForm):
    email = forms.CharField(label=None, widget=forms.EmailInput(
                                attrs={
                                    'placeholder': 'E-mail',
                                }
                            ))
    class Meta:
        model = Subscriber
        fields = ['email',]
        
class UnsubscribeForm(forms.Form):
    email = forms.CharField(label=None, widget=forms.EmailInput(
                                attrs={
                                    'placeholder': 'E-mail',
                                }
                            ))