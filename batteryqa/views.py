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
        if form.is_valid():
            data = form.cleaned_data
            records = run_qa(data['select'], data['ques'], data['confidence'], data['context'])
            print(records)
            outputs = {'records': records}
            request.session['outputs'] = outputs
            return redirect(answers)
    else:
        form = QuestionForm()
    return render(request, 'batteryqa/qa.html', {'form': form})


@login_required()
def answers(request):
    outputs = request.session.get('outputs')
    return render(request, 'batteryqa/answers.html', outputs)


@login_required()
def answers_example(request, example):
    # outputs = request.session.get('outputs')
    if example == 1:
        records = [{'type': 'cathode', 'answer': 'LiFePO4', 'score': 0.9598992466926575, 'context':
                    'The cathode of this Li-ion battery system is LiFePO4. The anode is graphite.'},
                   {'type': 'anode', 'answer': 'graphite', 'score': 0.9511426091194153, 'context':
                    'The cathode of this Li-ion battery system is LiFePO4. The anode is graphite.'}]
        outputs = {'records': records}
        return render(request, 'batteryqa/answers.html', outputs)
    if example == 2:
        records = [{'type': 'anode', 'answer': 'graphite', 'score': 0.9511426091194153, 'context':
                    'The cathode of this Li-ion battery system is LiFePO4. The anode is graphite.'}]
        outputs = {'records': records}
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
