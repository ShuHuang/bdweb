from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import QuestionForm, SearchForm
from .tasks import run_qa, run_answer


@login_required()
def batterysearch(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            question = data['search']
            records = run_answer(question)
            print(records)
            outputs = {'records': records}
            request.session['search_results'] = outputs
            return redirect(search_results)
    else:
        form = SearchForm()
    return render(request, 'batteryqa/search.html', {'form': form})


@login_required()
def search_results(request):
    outputs = request.session.get('search_results')
    print(outputs)
    return render(request, 'batteryqa/search-results.html', outputs)


@login_required()
def search_results_example(request, example):
    if example == 1:
        outputs = {'records': [{'original_question': "what's the most common anode in 2015 ", 'answer': 'graphite'}]}
    elif example == 2:
        outputs = {'records': [{'original_question': "what's the most common cathode in 2021 ", 'answer': 'sulfur'}]}
    elif example == 3:
        outputs = {'records': [{'original_question': "what's the most common electrolyte in 1999 ", 'answer': 'propylene carbonate'}]}
    elif example == 4:
        outputs = {'records': [{'original_question': 'No similar questions found', 'answer': 'No answers found. Ask me some questions about batteries.'}]}
    return render(request, 'batteryqa/search-results.html', outputs)


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
    if example == 1:
        records = [{'type': 'cathode', 'answer': 'lithium iron phosphate', 'score': 0.7359284162521362, 'context':
                    'The lithium iron phosphate battery (LiFePO4 battery) or LFP battery (lithium ferrophosphate), '
                    'is a type of lithium-ion battery using lithium iron phosphate (LiFePO4) as the cathode material, '
                    'and a graphitic carbon electrode with a metallic backing as the anode.'},
                   {'type': 'anode', 'answer': 'graphitic carbon electrode with a metallic backing',
                    'score': 0.34201282262802124, 'context':
                    'The lithium iron phosphate battery (LiFePO4 battery) or LFP battery (lithium ferrophosphate), '
                    'is a type of lithium-ion battery using lithium iron phosphate (LiFePO4) as the cathode material, '
                    'and a graphitic carbon electrode with a metallic backing as the anode.'}]
        outputs = {'records': records}
        return render(request, 'batteryqa/answers.html', outputs)
    elif example == 2:
        records = [{'type': 'electrolyte', 'answer': 'a solution of LiPF6 in linear and cyclic carbonates',
                    'score': 0.19098393619060516, 'context':
                    'The typical non-aqueous electrolyte for commercial Li-ion cells is a solution of LiPF6 in linear '
                    'and cyclic carbonates such as dimethyl carbonate and ethylene carbonate, respectively [1], [2].'}]
        outputs = {'records': records}
        return render(request, 'batteryqa/answers.html', outputs)
    elif example == 3:
        records = [{'type': "What's the maximum capacity of LiC6?", 'answer': '372 mAh g−1',
                    'score': 0.6613584756851196, 'context':
                    'The mechanism of lithium intercalation in the so-called ‘soft’ anodes, i.e. graphite or '
                    'graphitable carbons, is well known: it develops through well-identified, reversible stages, '
                    'corresponding to progressive intercalation within discrete graphene layers, to reach the '
                    'formation of LiC6 with a maximum theoretical capacity of 372 mAh g−1.'}]
        outputs = {'records': records}
        return render(request, 'batteryqa/answers.html', outputs)
    elif example == 4:
        records = [{'type': "What is a possible application for NCA cathode?", 'answer': 'electric vehicles',
                    'score': 0.13558681309223175, 'context':
                        "For current LIBs based on OLE system, the employed cathodes could be mainly divided into two "
                        "categories: LCO is still very popular in the consumer electronics market and Ni-rich "
                        "compounds have already taken a place in the electric vehicles where the Tesla "
                        "LiNi0.8Co0.15Al0.05O2 (NCA) cathode is a good example."}]
        outputs = {'records': records}
        return render(request, 'batteryqa/answers.html', outputs)


# @login_required()
# def test(request):
#     if request.method == 'POST':
#         form = QuestionForm(request.POST)
#         print(form.is_valid())
#         if form.is_valid():
#             data = form.cleaned_data
#             records = run_qa(data['select'], data['ques'], data['confidence'], data['context'])
#             outputs = {'records': records}
#             request.session['outputs'] = outputs
#             return redirect(answers)
#     else:
#         form = QuestionForm()
#     return render(request, 'batteryqa/test.html', {'form': form})
