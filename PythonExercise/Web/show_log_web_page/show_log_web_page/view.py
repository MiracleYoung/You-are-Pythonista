from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from . import main

def show_log(request):
    log_data_dict = main.log_generate()
    print(log_data_dict)
    return render(request, 'index.html',{'data':log_data_dict})
