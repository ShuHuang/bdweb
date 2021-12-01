from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import celery

from .forms import QuestionForm
from . import tasks

# @login_required()
# def batteryqa(request):
#     return render(request, 'batteryqa/qa.html')


@login_required()
def batterysearch(request):
    return render(request, 'batteryqa/search.html')


@login_required()
def batteryqa(request):
    if request.method == 'post':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.save()
            async_result = tasks.extract_data.apply_async(question_id=question.id)
            # return render(request, 'batteryqa/results.html', result_id=async_result.id)
            return redirect(results, result_id=async_result.id)

    else:
        return render(request, 'batteryqa/qa.html')


def results(request, result_id):
    task = celery.AsyncResult(result_id)
    return render(request, 'batteryqa/results.html', task=task)
