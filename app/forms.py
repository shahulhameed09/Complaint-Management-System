from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from app.models import Complaint, Profile, Contact


class register(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        
class ComplaintForm(ModelForm):
    class Meta:
        model=Complaint
        fields=('Subject','Type_of_complaint','Description')
        
class statusupdate(ModelForm):
    class Meta:
        model=Complaint
        fields=('status',)  
    
class update_profile(ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

class profile_pic_update(ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        
class Contact_form(ModelForm):
    class Meta:
        model = Contact
        fields = ['Name','Email','Subject','Message']