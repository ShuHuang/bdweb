from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
# from .forms import QuestionForm
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
        bertmodel = request.POST.get('model_name', '')
        question = request.POST.get('ques', '')
        score = request.POST.get('confidence', '')
        text = request.POST.get('context', '')
        # print(bertmodel, question, score, text)
        records = run_qa(bertmodel, question, score, text)
        # print(records)
        outputs = {'records': records}
        request.session['outputs'] = outputs
        return redirect(answers)
        # return render(request, 'batteryqa/answers.html', outputs)
    # form = QuestionForm(request.GET)
    # print(form)
    # print(form.is_valid())
    # if form.is_valid():
    #     cd = form.cleaned_data
    #     print(cd['model_name'])
    #     return HttpResponse("Do something")
    return render(request, 'batteryqa/qa.html')


def answers(request):
    outputs = request.session.get('outputs')
    return render(request, 'batteryqa/answers.html', outputs)
