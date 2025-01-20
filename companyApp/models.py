from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# GeneralInformation model 
class GeneralInfo(models.Model):
    company_name = models.CharField(max_length=222, default="Company Name")
    location = models.CharField(max_length=300)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    open_hours = models.CharField(max_length=100, blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
        # blank = true - allows an admin to create record without passing value to it.. 
        # null = True - allow the database to store empty value, allows users...
    def __str__(self):
        return self.company_name


# Services render
class Service(models.Model):
    icon = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=355, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


# Testimonials 
class Testimonial(models.Model):
    user_image = models.CharField(max_length=225, blank=True, null=True)
    star_count = [
        (1,'One'),
        (2,'Two'),
        (3,'Three'),
        (4,'Four'),
        (5,'Five'),
    ]
    rating_count = models.IntegerField(choices=star_count)
    
    username = models.CharField(max_length=200)
    user_job_title = models.CharField(max_length=100)
    review = models.TextField()

    def __str__(self):
        return f"{self.username} - job-tile {self.user_job_title}"
    

# FAQS 
class FrequentlyAskedQuestion(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField(default='add')

    def __str__(self):
        return self.question
    

# Contact Logs - number of times a particular user sent mail 
class ContactFormLog(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    subject = models.CharField(max_length=150)
    message = models.TextField()
    sent_time = models.DateTimeField(null=True, blank=True)
    is_success = models.BooleanField(default=False)
    is_error = models.BooleanField(default=False)
    error_message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
    

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=50)
    joined_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.first_name


class Blog(models.Model):
    blog_image = models.CharField(max_length=225, null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=100)
    # author = models.CharField(max_length=100, default="name")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    # on_delete=models.CASCADE - if deleting the author, django will auto delete the author's blog posts on delete of author
    # on_delete=models.PROTECT - if deleting the author, django will not delete the author if the author has blogs.
    # on_delete=models.SET_NULL - if deleting the author, django will make the author column as blank.
    
    created_at = models.DateTimeField(auto_now_add=True)
    content = RichTextField() #models.TextField()

    def __str__(self):
        return self.title
    
