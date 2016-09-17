from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Form,FieldForm
# Create your views here.

def index(request):
    all_forms = Form.objects.all()
    context = {
        'all_forms' : all_forms
    }
    return render(request, 'Formulaire/index.html', context)

def detail(request, form_id):
    try:
        form = Form.objects.get(pk=form_id)
    except Form.DoesNotExist:
        raise Http404("Form does not exist")
    return render(request, 'Formulaire/detail.html' , {'form' : form})