from transformers.pipelines import pipeline


def run_qa(bertmodel, question, score, text):
    if score == '' or score is None:
        score = 0.3
    if text == '':
        text = 'The cathode of this Li-ion battery system is LiFePO4. The anode is graphite.'
    answers = extract_data(bertmodel, question, text, score)  # list of dictionaries
    return answers


def extract_data(model_name, ques, context, confidence):
    confidence = float(confidence)
    if model_name == 'BatteryBERT':
        model_name = "batterydata/bert-base-qa"
    elif model_name == 'BatterySciBERT':
        model_name = "batterydata/bert-base-qa"
    elif model_name == 'BatteryOnlyBERT':
        model_name = "batterydata/bert-base-qa"
    output_model = pipeline('question-answering', model=model_name, tokenizer=model_name)

    qanswers = []
    if ques == '':
        words = ['cathode', 'anode', 'electrolyte']
        for word in words:
            wordn = word + 's'
            wordcase = word.capitalize()
            if word in context or wordn in context or wordcase in context:
                qa_input = {'question': "What's the {}?".format(word), 'context': context}
                res = output_model(qa_input, topk=3)
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
        qa_input = {'question': ques, 'context': context}
        res = output_model(qa_input, topk=3)
        # print(question, res)
        for answer in res:
            if answer['score'] > confidence:
                ianswer = {"type": ques, "answer": answer['answer'], "score": answer['score'],
                           "context": context}
                qanswers.append(ianswer)
                break
    return qanswers


def run_answer(question):
    print(question)
    pass