from django import forms
from .models import Room, Images, RoomComments, RoomUserMoreDetails
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class RoomForm(forms.ModelForm):
    c = [('Available', 'Available'),('Sold', 'Sold')]
    status = forms.ChoiceField(label=("Status"),choices=c,widget=forms.Select(attrs={'class':"btn btn-secondary dropdown-toggle"}))
    price = forms.FloatField(label=("Price (NPR)"))
    class Meta:
        model = Room
        fields = ['title', 'description', 'status', 'tags', 'image', 'price']
        labels = {
            'image': 'Main Image (अरू पछि थप्नुहाेला)'
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'class':"form-control", 'placeholder':"तपाइँकाे सामानकाे बारेमा थाेरै जानकारी", 'maxlength':'399'})
        self.fields['price'].widget.attrs.update({'class':"form-control", 'placeholder':"मुल्य (रुपैँयामा)"})
        self.fields['tags'].widget.attrs.update({'placeholder':"यहाँ केहि नलेख्नुभए पनि हुन्छ"})


class ImageForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = [ 'image' ]
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Upload Pic(s)', css_class='btn-primary'))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'multiple':True})

class RoomCommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'id':'commentcontent','class':"form-control", 'placeholder':"सामानबारे प्रश्न वा किनिसक्नुभए कस्ताे लाग्याे, लेख्नुहाेस्..", 'maxlength':'500'}), label="Comment")
    class Meta:
        model = RoomComments
        fields = [ 'content' ]

class RoomUserMoreDetailsForm(forms.ModelForm):
    class Meta:
        model = RoomUserMoreDetails
        db_table = 'room_moreuserdetails'
        fields = ['phone', 'email']
