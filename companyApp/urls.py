from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("contact/", views.contact_form, name='contact-form'),
    path("blog-details/<blog_id>", views.blog_details, name='blog_details'),
    path("blogs/", views.blogs, name='blogs'),
]

