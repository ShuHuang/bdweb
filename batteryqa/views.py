from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import QuestionForm
from .tasks import run_qa

# @login_required()
# def batteryqa(request):
#     return render(request, 'batteryqa/qa.html')


@login_required()
def batterysearch(request):
    return render(request, 'batteryqa/search.html')


@login_required()
def batteryqa(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            data = form.cleaned_data
            records = run_qa(data['select'], data['ques'], data['confidence'], data['context'])
            outputs = {'records': records}
            request.session['outputs'] = outputs
            return redirect(answers)
    else:
        form = QuestionForm()
    return render(request, 'batteryqa/qa.html', {'form': form})


def answers(request):
    outputs = request.session.get('outputs')
    return render(request, 'batteryqa/answers.html', outputs)


@login_required()
def test(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            data = form.cleaned_data
            records = run_qa(data['select'], data['ques'], data['confidence'], data['context'])
            outputs = {'records': records}
            request.session['outputs'] = outputs
            return redirect(answers)
    else:
        form = QuestionForm()
    return render(request, 'batteryqa/test.html', {'form': form})
