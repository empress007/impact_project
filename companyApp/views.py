from django.shortcuts import render, redirect
from .models import (
    GeneralInfo, 
    Service, 
    Testimonial, 
    FrequentlyAskedQuestion,
    ContactFormLog,
    Blog
)
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# # to store queries executed by django ... 
# from django.db import connection
# file_path = 'sql_queries.txt'
# def write_sql_queries_to_file(file_path):
#     with open(file_path, 'w') as file_object:
#         sql_queries = connection.queries
#         for query in sql_queries:
#             sql = query['sql']
#             file_object.write(f"{sql}\n")


# Create your views here.
# landing page 
def index(request):

    general_info = GeneralInfo.objects.first()
    # write_sql_queries_to_file(file_path=file_path)
    # print(general_info.location)

    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    faqs = FrequentlyAskedQuestion.objects.all()

    recent_blogs = Blog.objects.all().order_by('-created_at')[:3]

    context = {
        # "company_name": general_info.company_name,
        "company_name": getattr(general_info, "company_name", ""),
        "location": getattr(general_info, "location", ""),
        "email": getattr(general_info, "email" , ""),
        "phone": getattr(general_info, "phone", ""),
        "open_hours": getattr(general_info, "open_hours", ""),
        "video_url": getattr(general_info, "video_url", ""),
        "twitter":getattr(general_info, "twitter_url", ""),
        "facebook": getattr(general_info, "facebook_url", ""),
        "instagram": getattr(general_info, "instagram_url", ""),
        "linkedin": getattr(general_info, "linkedin_url", ""),

        "services":services,
        "testimonials":testimonials,
        "faqs":faqs,
        "recent_blogs":recent_blogs,
    }

    return render(request, "index.html", context)


# Contact form creation 
def contact_form(request):
    # using post request, to enable user to send mail 
    if request.method == "POST":
        print('\nContact form submitted by user...')
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # # console print 
        # print(f'request POST: {request.POST}')
        # print(f'name: {name}')
        # print(f'request POST: {email}')
        # print(f'request POST: {subject}')
        # print(f'request POST: {message}')

        # Styling sent contact message
        context = {
            "name":name,
            "email":email,
            "subject":subject,
            "message":message,
        }

        html_context = render_to_string('email.html', context)
        
        is_success = False        
        is_error = False
        error_message = ""        
        # send mail .... 
        try:
            send_mail(
                subject=subject,
                # message=f"{name} - {email} - {message}",
                message=None,
                html_message=html_context,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False, # True is default
            )
        except Exception as e:
            is_error = True
            error_message = str(e)
            print(f'Email failed')
            messages.error(request, "There is an error, could not send email!")
        else:
            is_success = True
            print(f"Email has been sent out...")
            messages.success(request, "Email has been sent successfully!")

        # Contact form log 
        ContactFormLog.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
            sent_time=timezone.now(),
            is_success=is_success,
            is_error=is_error,
            error_message=error_message,
        )

    return redirect('home')



def blog_details(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    recent_blogs = Blog.objects.all().exclude(id=blog_id).order_by('-created_at')[:2]

    context = {
        "blog":blog,
        "recent_blogs":recent_blogs,
    }
    return render(request, 'blog_details.html', context)


def blogs(request):

    all_blogs = Blog.objects.all()
    paginator = Paginator(all_blogs, 3)

    print(f"Paginator page: {paginator.num_pages}")

    # for page to work 
    page = request.GET.get('page')

    # error handling 
    try:
        pag_blogs = paginator.page(page)
    except PageNotAnInteger:
        pag_blogs = paginator.page(1)
    except EmptyPage:
        pag_blogs = paginator.page(paginator.num_pages)

    context = {
        "pag_blogs":pag_blogs,
    }

    return render(request, 'blogs.html', context)

