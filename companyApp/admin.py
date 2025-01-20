from django.contrib import admin
# from django.http import HttpRequest
from .models import (
    GeneralInfo, Service, Testimonial, FrequentlyAskedQuestion, ContactFormLog, Blog, Author
)

# courseadmin
# admin4321
# courseadmin@gmail.com

# # Register your models here.
# class CompanyInfoAdmin(admin.ModelAdmin):
#     list_display = ['company_name', 'location', 'email']
# admin.site.register(GenerateInfo, CompanyInfoAdmin)

# OR, its preferred
@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'location', 'email']
   
    # other functions/operations that can be performed on the model on the admin site...
    # To disable add permission 
    def has_add_permission(self, request, obj=None):
        return False
    
    # To disable update permission 
    def has_change_permission(self, request, obj=None):
        return False
    
    # set specific field to diable update 
    readonly_fields = [
        'email'
    ]
    
    # To disable delete permission 
    def has_delete_permission(self, request, obj=None):
        return False
    
    # To disable module from displaying 
    def has_module_permission(self, request, obj=None):
        return False


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']

    search_fields = ['title', 'description']
    
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['username','user_job_title','display_rating_count']
    
    def display_rating_count(self, obj):
        return "*" * obj.rating_count
    display_rating_count.short_description = "Rating"


@admin.register(FrequentlyAskedQuestion)
class FrequentlyAskedAdmin(admin.ModelAdmin):
    list_display = [
        'question', 'answer'
    ]


# OR, its preferred
@admin.register(ContactFormLog)
class ContactFormLogAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_success', 'is_error', 'sent_time']

        # To disable delete permission 
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at']

@admin.register(Author)
class BlogAdmin(admin.ModelAdmin):
    # list_display = ['title', 'category', 'created_at']
    pass

