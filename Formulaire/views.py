from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Form,FieldForm
from .forms import PollForm,QuestionForm
from django.forms import modelformset_factory
# Create your views here.

def accueil(request):
    all_forms = Form.objects.all()
    context = {
        'all_forms' : all_forms
    }
    return render(request, 'Formulaire/accueil.html', context)

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
    QuestionFormSet = modelformset_factory(FieldForm, form = QuestionForm)
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

def edit(request, form_id):
    QuestionFormSet = modelformset_factory(FieldForm, form = QuestionForm)
    poll = get_object_or_404(Form, pk=form_id)
    if request.method == "POST":
        form = PollForm(request.POST, instance = poll)
        question = QuestionFormSet(request.POST)
        print(FieldForm.objects.filter(form = poll))
        if form.is_valid() and question.is_valid():
            s_form = form.save()
            s_question = question.save(commit=False)
            print(s_question)
            for q in s_question:
                q.form = s_form
                q.save()
            return redirect('detail', form_id=s_form.id)
    else:
        form = PollForm(instance=poll)
        question = QuestionFormSet(queryset = FieldForm.objects.filter(form=poll))
    return render(request, 'Formulaire/create.html', {'form': form, 'question': question})

def check_pass(request,form_id):
    if request.POST:
        passw = request.POST.get('password')
        poll = get_object_or_404(Form, pk=form_id)
        if poll.password == passw:
            return redirect('edit', form_id=form_id)
    return render(request, 'Formulaire/check_pass.html', {})

