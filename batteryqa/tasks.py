from celery import shared_task
from transformers.pipelines import pipeline

from .models import Question

@shared_task
def run_qa(question_id):
    question = Question.objects.get(pk=question_id)
    model_name = question.model_name
    ques = question.ques
    context = question.context
    confidence = question.confidence
    answers = extract_data(model_name, ques, context, confidence)  #list of dictionaries
    if answers:
        question.score = answers[0]['score']
        question.answer = answers[0]['answer']
        question.save()
    return answers


def extract_data(model_name, ques, context, confidence):
    if model_name == 'BatteryBERT':
        model_name = "batterydata/bert-base-qa"
    output_model = pipeline('question-answering', model=model_name, tokenizer=model_name)

    qanswers = []
    if ques == '':
        words = ['cathode', 'anode', 'electrolyte']
        for word in words:
            wordn = word + 's'
            wordcase = word.capitalize()
            if word in context or wordn in context or wordcase in context:
                QA_input = {'question': "What's the {}?".format(word), 'context': context}
                res = output_model(QA_input, topk=3)
                # print(res)
                for answer in res:
                    if 'battery' in answer['answer'] or 'batteries' in answer['answer'] or 'LIB' in answer['answer']:
                        continue
                    if word == 'electrolyte' and ('lithium' in answer['answer'] or 'Li' in answer['answer']):
                        continue
                    # cem_doc = Document(answer['answer'])
                    if answer['score'] > confidence:
                        ianswer = {"type": word, "answer": answer['answer'], "score": answer['score'],
                                   "context": context}
                        qanswers.append(ianswer)
                        break
    else:
        QA_input = {'question': ques, 'context': context}
        res = output_model(QA_input, topk=3)
        # print(question, res)
        for answer in res:
            if answer['score'] > confidence:
                ianswer = {"type": ques, "answer": answer['answer'], "score": answer['score'],
                           "context": context}
                qanswers.append(ianswer)
                break
    return qanswers
