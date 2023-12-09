from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib import messages
from app.models import Complaint, Profile, Complaint_Categorie
from app.forms import statusupdate, ComplaintForm, update_profile, profile_pic_update
from django.db.models import Count, Q

def counter(req):
    if req.user.profile.user_type == "officer":
        total=Complaint.objects.all().count()
        inprogress=Complaint.objects.all().exclude(Q(status='1') | Q(status='3')).count()
        solved=Complaint.objects.all().exclude(Q(status='3') | Q(status='2')).count()
        pending=Complaint.objects.all().exclude(Q(status='1') | Q(status='2')).count()
        dataset=Complaint.objects.values('Type_of_complaint').annotate(total=Count('status'),solved=Count('status', filter=Q(status='1')),
                    notsolved=Count('status', filter=Q(status='3')),inprogress=Count('status',filter=Q(status='2'))).order_by('Type_of_complaint')
        args={'total':total,'inprogress':inprogress,'solved':solved,'dataset':dataset,'counter':'active','pending':pending, 'home':'text-dark'}
        return render(req, 'Officer/counter.html',args)
    else:
        return render(req,'errorpage.html')


class PasswordsChangeView(SuccessMessageMixin,PasswordChangeView):
    form_class=PasswordChangeForm
    success_url=reverse_lazy('counter')

    # Override error messages if needed
    def form_invalid(self, form):
        messages.error(self.request, "There was an error changing your password. Please try again!")
        return super().form_invalid(form)
    
    # Add context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pass'] = 'active'
        return context

def allComplaints(request):
    if request.user.profile.user_type == "officer":
        c=Complaint.objects.all()
        category = Complaint_Categorie.objects.all()
        comp=request.GET.get("search")
        drop=request.GET.get("drop")

        if drop:
            c=c.filter(Q(Type_of_complaint__icontains=drop))
        if comp:
            c=c.filter(Q(Type_of_complaint__icontains=comp)|Q(Description__icontains=comp)|Q(Subject__icontains=comp))
            
        args={'c':c,'comp':comp,'category':category ,'all':'active'}
        return render(request, 'Officer/allComplaints.html',args)
    else:
        return render(request,'errorpage.html')


def view_details(req, ID):
    if req.user.profile.user_type == "officer":
        c=Complaint.objects.get(pk=ID)
        form = statusupdate(req.POST or None, instance=c)
        form2 = ComplaintForm(req.POST or None, instance=c)
        if form.is_valid():
            form.save()
            messages.success(req, 'Status has been updated successfully!')
            return redirect('/allComplaints')
        args={'c':c, 'forms':form, 'form2':form2}
        return render(req, 'Officer/view_details.html',args)
    else:
            return render(req,'errorpage.html')

    
def solved(request):
    if request.user.profile.user_type == "officer":
        c=Complaint.objects.all().exclude(Q(status='3') | Q(status='2'))
        category = Complaint_Categorie.objects.all()
        comp=request.GET.get("search")
        drop=request.GET.get("drop")

        if drop:
                c=c.filter(Q(Type_of_complaint__icontains=drop))
        if comp:
                
                c=c.filter(Q(Type_of_complaint__icontains=comp)|Q(Description__icontains=comp)|Q(Subject__icontains=comp))
    
        
        args={'c':c,'comp':comp,'category':category , 'solved':'active'}
        return render(request, 'Officer/solved.html', args)
    else:
        return render(request,'errorpage.html')

def inProgress(request):
    if request.user.profile.user_type == "officer":
        c=Complaint.objects.all().exclude(Q(status='1') | Q(status='3'))
        category = Complaint_Categorie.objects.all()
        comp=request.GET.get("search")
        drop=request.GET.get("drop")

        if drop:
                c=c.filter(Q(Type_of_complaint__icontains=drop))
        if comp:
                
                c=c.filter(Q(Type_of_complaint__icontains=comp)|Q(Description__icontains=comp)|Q(Subject__icontains=comp))
    
        
        args={'c':c,'comp':comp,'category':category , 'inProgress':'active'}
        return render(request, 'Officer/inProgress.html', args)
    else:
        return render(request,'errorpage.html')
    
def pending(request):
    if request.user.profile.user_type == "officer":
        c=Complaint.objects.all().exclude(Q(status='1') | Q(status='2'))
        category = Complaint_Categorie.objects.all()
        comp=request.GET.get("search")
        drop=request.GET.get("drop")

        if drop:
                c=c.filter(Q(Type_of_complaint__icontains=drop))
        if comp:
                
                c=c.filter(Q(Type_of_complaint__icontains=comp)|Q(Description__icontains=comp)|Q(Subject__icontains=comp))
    
        
        args={'c':c,'comp':comp,'category':category , 'pending':'active'}
        return render(request, 'Officer/pending.html', args)
    else:
        return render(request,'errorpage.html')

def officer_profile(request):
    if request.user.profile.user_type == "officer":
        if request.user.is_authenticated:
            data=Profile.objects.get(connect=request.user)
            return render(request, 'Officer/officer_profile.html',{'form':data, 'officer_profile':'text-dark'})
        else:
            messages.success(request, "You must be logged in to see your profile!")
            return redirect('/')
    else:
        return render(request,'errorpage.html')
        
    
def update_officer_profiles(request):
    if request.user.profile.user_type == "officer":
        form = update_profile(request.POST or None, instance=request.user)
        p_form = profile_pic_update(request.POST or None, request.FILES or None, instance=request.user.profile)
        if form.is_valid() and p_form.is_valid():
            form.save()
            p_form.save()
            return redirect('officer_profile')

        context={'form':form,'p_form':p_form, 'officer_profile':'text-dark'}
        return render(request,'Officer/update_officer_profile.html', context)
    else:
        return render(request,'errorpage.html')