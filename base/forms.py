from django import forms
from .models import ContactMessage
from .models import Subscriber

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = [ 'fullname', 'Email', 'QueryRelated', 'message']
        labels ={ 'fullname': '', 'Email':'', 'QueryRelated':'','message':'' }
        widgets={
            'fullname': forms.TextInput(attrs={
                'placeholder':'Full Name',
                'class':'form-input'
            }),
            'Email': forms.EmailInput(attrs={
                'placeholder':'Your Email',
                'class':'form-input'
            }),
            'QueryRelated': forms.Select(attrs={
                'class':'form-select'
            }),

            'message': forms.Textarea(attrs={
                'placeholder':'Message',
                'class':'form-textarea',
                'rows': 6
            }),
            

        }
    

class Subscriberform(forms.ModelForm):
    class Meta:
        model=Subscriber
        fields=['email']
        labels={'email': ''}
        widgets={
            'email':forms.EmailInput(attrs={
            'placeholder': 'Enter Your Email',
            'class': 'subscriber-input' ,
        }),
    }

