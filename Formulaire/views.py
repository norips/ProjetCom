from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Form,FieldForm
from .forms import PollForm,QuestionForm
from django.forms import modelformset_factory
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

def create(request):
    QuestionFormSet = modelformset_factory(FieldForm,fields=('question',))
    if request.POST:
        form = PollForm(request.POST)
        question = QuestionFormSet(request.POST)
        if form.is_valid() and question.is_valid():
            s_form = form.save()
            s_question = question.save(commit = False)
            for q in s_question:
                print(q.question)
                q.form = s_form
                q.save()
            return redirect('detail', form_id = s_form.id)
    form = PollForm()
    question = QuestionFormSet(queryset=FieldForm.objects.none())
    return render(request,'Formulaire/create.html',{'form' : form, 'question' : question })