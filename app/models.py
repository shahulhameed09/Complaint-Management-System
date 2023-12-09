import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

user_type_data = (('officer', "Officer"), ('user', "User"))

class Profile(models.Model):
    user_type = models.CharField(default='user', choices=user_type_data, max_length=10)
    image=models.ImageField(default="images/default.png", upload_to="media")
    connect= models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"{self.connect}'s profile"
    
class Complaint_Categorie(models.Model):
    Add_Category = models.CharField(max_length=50)
    
    def __str__(self):
        return self.Add_Category

class Complaint(models.Model):
    STATUS =((1,'Solved'),(2, 'InProgress'),(3,'Pending'))
    
    user=models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    Subject=models.CharField(max_length=200,blank=False,null=True)
    Type_of_complaint=models.ForeignKey(Complaint_Categorie, on_delete=models.CASCADE, null=True, default=0)
    Description=models.TextField(max_length=4000,blank=False,null=True)
    Time = models.DateField(auto_now=True)
    status=models.IntegerField(choices=STATUS,default=3)
    
   
    def __init__(self, *args, **kwargs):
        super(Complaint, self).__init__(*args, **kwargs)
        self.__status = self.status

    def save(self, *args, **kwargs):
        if self.status and not self.__status:
            self.active_from = datetime.now()
        super(Complaint, self).save(*args, **kwargs)
 
    def __str__(self):
 	    return f"{self.user}'s complaint for {self.Type_of_complaint}"
  
class Contact(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    Name=models.CharField(max_length=25)
    Email=models.EmailField()
    Subject=models.CharField(max_length=25)
    Message=models.TextField()
    
    def __str__(self):
        return f"{self.user}'s Contact"