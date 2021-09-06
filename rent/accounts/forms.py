from django import forms
from django.contrib.auth.models import User
from django.utils.encoding import smart_str
from .models import UserDetails, Comments
from django.contrib.auth import password_validation
from .addressdetails import skillslist as sl

class NumberForm(forms.Form):
    number = forms.CharField(widget=forms.NumberInput(attrs={'class':"form-control", 'placeholder':"Mobile Number"}), max_length=10, min_length=10, label="")

class OTPForm(forms.Form):
    otp = forms.CharField(widget=forms.NumberInput(attrs={'class':"form-control", 'placeholder':"4 digit OTP", 'label':""}), max_length=4, min_length=4, label="")

class RegistrationForm(forms.Form):
    number = forms.CharField(widget=forms.NumberInput(attrs={'class':"form-control", 'placeholder':"Mobile Number", 'readonly':'readonly'}), max_length=10, min_length=10)
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':"First Name"}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", 'placeholder':"Last Name"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control", 'placeholder':"Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control", 'placeholder':"Re-enter Password"}))

    def clean_password2(self, *args, **kwargs):
        p1 = self.cleaned_data.get('password1')
        p2 = self.cleaned_data.get('password2')
        if p1!=p2:
            raise forms.ValidationError("Password didn't match. Please enter again.")
        else:
            return p1
    
    def clean_number(self, *args, **kwargs):
        n = self.cleaned_data.get('number')
        obj = User.objects.filter(username__iexact=n)
        if obj.exists():
            raise forms.ValidationError("Sorry, the number is already registered. Please login or register with another number.")
        else:
            return n
    
    def clean_password1(self, *args, **kwargs):
        p = self.cleaned_data.get('password1')
        if len(smart_str(p, encoding='utf-8', strings_only=False, errors='strict'))<8:
            raise forms.ValidationError("Password must be at least 8 characters. Please enter again.")
        else:
            return p

class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control mb-4", 'placeholder':"Password"}), label="")
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username': "",
            'password':""
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':"form-control mb-4", 'placeholder':'Mobile Number'})
        self.fields['username'].help_text = ""

class UserDetailsForm(forms.Form):
    provinces = [('none','-- Please select your Province --'),('Province 1', 'Province 1'), ('Province 2', 'Province 2'), ('Bagmati Pradesh','Bagmati Pradesh'), ('Gandaki Pradesh','Gandaki Pradesh'), ('Province 5','Province 5'),('Karnali Pradesh','Karnali Pradesh'),('Sudurpashchim Pradesh','Sudurpashchim Pradesh')]
    province= forms.ChoiceField(choices=provinces, widget=forms.Select(attrs={'id': 'province', 'name':'province', 'class':"btn btn-secondary dropdown-toggle", 'onchange': 'javascript:getdis();'}), required=True)
    district= forms.ChoiceField(required=True, widget=forms.Select(attrs={'id': 'district', 'class':"btn btn-secondary dropdown-toggle", 'onchange': 'javascript:getmun();'}))
    municipality= forms.ChoiceField(widget=forms.Select(attrs={'id': 'municipality', 'class':"btn btn-secondary dropdown-toggle"}),required=True)
    wardno = forms.CharField(label=("Ward No.:"), widget=forms.NumberInput(attrs={'id': 'wardno','name':'wardno','class':"form-control", 'placeholder':"वडा नं", 'min':'1', 'max':'25'}),required=True)
    skillslist = forms.ChoiceField(label=("Preferred Job Type"),choices=sl,required=True,widget=forms.Select(attrs={'id': 'skillslist', 'name':'skillslist','class':"btn btn-secondary dropdown-toggle"}))
    aboutSkill = forms.CharField(label=("About Skill"), widget=forms.Textarea(attrs={'id': 'aboutSkill','name':'aboutSkill','class':"form-control", 'placeholder':"तपाइँकाे सिपकाे बारेमा थाेरै जानकारी", 'maxlength':'250'}))
    age = forms.CharField(label=("Age"), widget=forms.NumberInput(attrs={'id':'age', 'name':'age','class':'form-control', 'placeholder':"Age (उमेर)", 'min':'13', 'max':'130'}))
    
    def clean_province(self, *args, **kwargs):
        n=self.cleaned_data.get('province')
        return n
    def clean_district(self, *args, **kwargs):
        n=self.cleaned_data.get('district')
        return n
    def clean_municipality(self, *args, **kwargs):
        n=self.cleaned_data.get('municipality')
        return n

class UpdateDetailsForm(forms.ModelForm):
    skills = forms.ChoiceField(label=("Preferred Job Type"),choices=sl,required=True,widget=forms.Select(attrs={'id': 'skillslist', 'name':'skillslist','class':"btn btn-secondary dropdown-toggle"}))
    class Meta:
        model = UserDetails
        fields = ['skills', 'skilldetails' ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['skilldetails'].widget.attrs.update({'id': 'aboutSkill','name':'aboutSkill','class':"form-control", 'placeholder':"तपाइँकाे सिपकाे बारेमा थाेरै जानकारी", 'maxlength':'250'})

class UpdatePersonalDetails(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control mb-4", 'placeholder':"First Name"}), label="")
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control mb-4", 'placeholder':"Last Name"}), label="")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':"form-control mb-4", 'placeholder':"Email"}), label="")

    class Meta:
        model = User
        fields = ['first_name','last_name','email']

    def clean_first_name(self, *args, **kwargs):
        n=self.cleaned_data.get('first_name')
        return n

    def clean_last_name(self, *args, **kwargs):
        n=self.cleaned_data.get('last_name')
        return n    

    def clean_email(self, *args, **kwargs):
        n = self.cleaned_data.get('email')
        return n

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'id':'commentcontent','class':"form-control", 'placeholder':"तपाईंले वहाँकाे काम गराइ कस्ताे पाउनुभयो, लेख्नुहाेस्..", 'maxlength':'398'}), label="Comment")
    class Meta:
        model = Comments
        fields = ['content']