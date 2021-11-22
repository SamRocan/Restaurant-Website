from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}),label="Email", required=True)
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=True)