from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Profile, Complaint, Contact, Complaint_Categorie
# Register your models here.


class CustomAdminSite(admin.AdminSite):
    site_title = 'Complaint Management System'
    site_header = 'Complaint Management System'
    def each_context(self, request):
        context = super().each_context(request)
        # Remove the "View site" link from the context
        context.pop('site_url', None)
        return context

# Replace the default admin site with your custom admin site
admin.site = CustomAdminSite()



class UserProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False  # Prevents the deletion of the profile when editing the user
    verbose_name_plural = 'User Profiles'



class CustomUserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser'),}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    inlines = (UserProfileInline,)




# Unregister the default Group admin
admin.sites.NotRegistered(Group)
admin.sites.NotRegistered(User)



# Register your custom UserAdmin
admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
admin.site.register(Complaint)
admin.site.register(Contact)
admin.site.register(Complaint_Categorie)
