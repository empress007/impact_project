from django.shortcuts import render
from . import models
from companyApp.models import GeneralInfo

# to store queries executed by django ... 
from django.db import connection
file_path = 'sql_queries.txt'
def write_sql_queries_to_file(file_path):
    with open(file_path, 'w') as file_object:
        sql_queries = connection.queries
        for query in sql_queries:
            sql = query['sql']
            file_object.write(f"{sql}\n")

# Run the CRUD operations from the views 

# Create your views here.
def index(request):
     
    # context = {
    #     "name":"Iyanu",
    #     "age":28,
    #     "job":"code-instructor",
    # }

    # ORM - Object Relational Mapping 
    # It is a programming technique that allows developers to (perform CRUD or) interact with databases using python objects and instead of raw SQL queries

    # CREATE 
    # READ
    # UPDATE 
    # DELETE 
    # create 

    # to create 
    # GeneralInfo.objects.create(
    #     company_name = "Carboni",
    #     phone = "09067442825",
    #     email = "carboni@mail.com",
    #     location="Nigeria",
    #     open_hours = "8am-8pm"
    # )
    

    # read 
    # all_records = GeneralInfo.objects.all()
    # print(all_records)

    # update 
    all_records = GeneralInfo.objects.get(id=1)
    # print(all_records)
    all_records.email = "iarowosola123@gmail.com"
    all_records.save()
    
    # delete 
    all_records = GeneralInfo.objects.all()
    all_records.delete()
    
    write_sql_queries_to_file(file_path=file_path)
    context = {"records":all_records}
    # return render(request, "companyApp/index.html", context) # keeping templates inside the app folder
    return render(request, "index.html", context)



