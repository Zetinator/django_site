from django import forms

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     sender = forms.EmailField()
#     telefon = forms.CharField(max_length=100)
#     message = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'class': 'full-width','placeholder':'Tu nombre'}), required = True)
    email = forms.EmailField(label='Email', max_length=50, widget=forms.TextInput(attrs={'class': 'full-width','placeholder':'Tu e-mail'}), required = True)
    tel = forms.CharField(label='Teléfono', max_length=20, widget=forms.TextInput(attrs={'class': 'full-width','placeholder':'Teléfono'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'id':'Message','class': 'full-width','placeholder':'Mensaje'}))

class SubscribeForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=50, widget=forms.TextInput(attrs={'id': 'mc-email','class': 'email','placeholder':'Corre electrónico'}))
