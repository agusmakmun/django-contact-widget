# not used yet
from django import forms
from contact_widget.models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'
        exclude = ['created', ]
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'required': 'required'
                }
            ),
            'subject': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'required'
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'required': 'required',
                    'rows': '3'
                }
            ),
        }
