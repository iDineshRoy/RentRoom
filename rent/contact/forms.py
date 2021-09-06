from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'class':"form-control mb-4", 'placeholder':"Name"}))
    from_email = forms.EmailField(required=True, label="", widget=forms.EmailInput(attrs={'class':"form-control mb-4", 'placeholder':"Email"}))
    subject = forms.ChoiceField(choices=[('Feedback','Feedback'),('Report a bug','Report a bug'),('Feature Request','Feature Request'), ('Promote Your Business','Promote Your Business'),], required=True, label="", widget=forms.Select(attrs={'class':"form-control mb-4", 'placeholder':"Subject"}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':"form-control mb-4", 'placeholder':"Message"}), required=True)