from django.shortcuts import redirect, render
from django.contrib import messages
from app.models import Complaint, Profile
from app.forms import update_profile, profile_pic_update, ComplaintForm, Contact_form
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy


def home(req):
    if req.user.profile.user_type == "user":
        form = ComplaintForm(req.POST)
        ContactForm = Contact_form()
        if form.is_valid():
            nform = form.save(commit=False)
            nform.user = req.user
            nform.save()
            messages.success(req, "Your Complaint has been registered!")
            return redirect('/view_status')

        args = {'form': form, 'ContactForm': ContactForm, 'home': 'active'}
        return render(req, 'Users/home.html', args)
    else:
        return render(req, 'errorpage.html')


def my_profile(request):
    if request.user.profile.user_type == "user":
        if request.user.is_authenticated:
            data = Profile.objects.get(connect=request.user)
            return render(request, 'Users/my_profile.html', {'form': data, 'my_profile': 'active'})
        else:
            messages.success(
                request, "You must be logged in to see your profile!")
            return redirect('/')
    else:
        return render(request, 'errorpage.html')


class PasswordsChangeView(SuccessMessageMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('user_home')

    # Override error messages if needed
    def form_invalid(self, form):
        messages.error(
            self.request, "There was an error changing your password. Please try again!")
        return super().form_invalid(form)

    # Add context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_profile'] = 'active'
        return context


def update_profiles(request):
    if request.user.profile.user_type == "user":
        form = update_profile(request.POST or None, instance=request.user)
        p_form = profile_pic_update(
            request.POST or None, request.FILES or None, instance=request.user.profile)
        if form.is_valid() and p_form.is_valid():
            form.save()
            p_form.save()
            return redirect('my_profile')

        args = {'form': form, 'p_form': p_form, 'my_profile': 'active'}
        return render(request, 'Users/update_profile.html', args)
    else:
        return render(request, 'errorpage.html')


def contact_us(req):
    form = Contact_form(req.POST)
    if form.is_valid():
        nform = form.save(commit=False)
        nform.user = req.user
        nform.save()
        return redirect('/user_home')


def view_status(req):
    if req.user.profile.user_type == "user":
        status = Complaint.objects.filter(user=req.user)

        args = {'status': status, 'view_status': 'active'}
        return render(req, 'Users/view_status.html', args)
    else:
        return render(req, 'errorpage.html')


def delete_complaint(req, ID):
    complain = Complaint.objects.get(pk=ID)
    complain.delete()
    return redirect('/view_status')


def view_complaint(req, ID):
    complain = Complaint.objects.get(pk=ID)

    args = {'complain': complain}
    return render(req, 'Users/view_complaint.html', args)
