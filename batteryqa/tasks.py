from transformers.pipelines import pipeline
from django.conf import settings
import os
import numpy as np
import queue as Q
import re
# import codecs


def run_qa(bertmodel, question, score, text):
    if score == '' or score is None:
        score = 0.3
    if text == '':
        text = 'The cathode of this Li-ion battery system is LiFePO4.'
    answers = extract_data(bertmodel, question, text, score)  # list of dictionaries
    return answers


def extract_data(model_name, ques, context, confidence):
    confidence = float(confidence)
    if model_name == 'BatteryBERT':
        model_name = "batterydata/test1"
    elif model_name == 'BatterySciBERT':
        model_name = "batterydata/test2"
    elif model_name == 'BatteryOnlyBERT':
        model_name = "batterydata/test3"
    output_model = pipeline('question-answering', model=model_name, tokenizer=model_name)

    qanswers = []
    if ques == '' or ques == "What's the device component?":
        words = ['cathode', 'anode', 'electrolyte']
        for word in words:
            wordn = word + 's'
            wordcase = word.capitalize()
            if word in context or wordn in context or wordcase in context:
                qa_input = {'question': "What's the {}?".format(word), 'context': context}
                res = output_model(qa_input, topk=3)
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
        print(qa_input)
        res = output_model(qa_input, topk=3)
        print(qa_input, res)
        for answer in res:
            if answer['score'] > confidence:
                ianswer = {"type": ques, "answer": answer['answer'], "score": answer['score'],
                           "context": context}
                qanswers.append(ianswer)
                break
    return qanswers


def run_answer(question):
    """
    return: list of answers (dict of answer and original_question)
    """
    print(question)
    text = question
    if text.endswith('?') or text.endswith('.') or text.endswith(','):
        text = text[:-1]
    qlist, alist = [], []
    with open(os.path.join(settings.MEDIA_ROOT, 'answer.txt'), 'r', encoding='utf-8') as f:
        for line in f:
            alist.append(line[:-1])
    with open(os.path.join(settings.MEDIA_ROOT, 'question.txt'), 'r', encoding='utf-8') as f:
        for line in f:
            qlist.append(line[:-1])
    new_list = tokenizer(qlist)
    vocab_count, count = createVocab(new_list)
    # writeVocab(vocab_count, "train.vocab")
    qlist = new_list

    TF, word2id, id2word = computeTF(vocab_count, count)
    IDF = computeIDF(word2id, qlist)
    vectorizer = np.multiply(TF, IDF)
    X_tfidf = computeSentence(qlist, word2id, vectorizer)
    que = Q.PriorityQueue()

    questions, answers, similarity = get_top_results_tfidf_noindex(query=text, vectorizer=vectorizer, word2id=word2id,
                                                                   X_tfidf=X_tfidf, que=que, qlist=qlist, alist=alist)

    return_answers = []
    if similarity == True:
        for i in range(len(questions)):
            dic = {'original_question': questions[i], 'answer': answers[i]}
            return_answers.append(dic)
    else:
        for i in range(len(questions)):
            dic = {'original_question': 'No similar questions found',
                   'answer': 'No answers found. Ask me some questions about batteries.'}
            return_answers.append(dic)
    print(return_answers)

    return return_answers


def tokenizer(ori_list):
    SYMBOLS = re.compile('[\s;\"\",.!?\\/\[\]\{\}\(\)-]+')
    new_list = []
    for q in ori_list:
        words = SYMBOLS.split(q.lower().strip())
        new_list.append(' '.join(words))
    return new_list


def createVocab(ori_list):
    count = 0
    vocab_count = dict()
    for q in ori_list:
        words = q.strip().split(' ')
        count += len(words)
        for w in words:
            if w in vocab_count:
                vocab_count[w] += 1
            else:
                vocab_count[w] = 1
    return vocab_count,count


# def writeFile(oriList,filename):
#     with codecs.open(filename,'w','utf8') as Fout:
#         for q in oriList:
#             Fout.write(q + u'\n')
#
#
# def writeVocab(vocabulary,filename):
#     sortedList = sorted(vocabulary.items(),key = lambda d:d[1])
#     with codecs.open(filename,'w','utf8') as Fout:
#         for (w,c) in sortedList:
#             Fout.write(w + u':' + str(c) + u'\n')


def computeTF(vocab,c):
    TF = np.ones(len(vocab))
    word2id = dict()
    id2word = dict()
    for word,fre in vocab.items():
        TF[len(word2id)] = 1.0 * fre / c
        id2word[len(word2id)] = word
        word2id[word] = len(word2id)
    return TF,word2id,id2word


def computeIDF(word2id,qlist):
    IDF = np.ones(len(word2id))
    for q in qlist:
        words = set(q.strip().split())
        for w in words:
            IDF[word2id[w]] += 1
    IDF /= len(qlist)
    IDF = -1.0 * np.log2(IDF)
    return IDF


def computeSentenceEach(sentence,tfidf,word2id):
    sentence_tfidf = np.zeros(len(word2id))
    for w in sentence.strip().split(' '):
        if w not in word2id:
            continue
        sentence_tfidf[word2id[w]] = tfidf[word2id[w]]
    return sentence_tfidf


def computeSentence(qlist,word2id,tfidf):
    X_tfidf = np.zeros((len(qlist),len(word2id)))
    for i,q in enumerate(qlist):
        X_tfidf[i] = computeSentenceEach(q,tfidf,word2id)
    return X_tfidf


def cosineSimilarity(vec1, vec2):
    return np.dot(vec1, vec2.T) / (np.sqrt(np.sum(vec1 ** 2)) * np.sqrt(np.sum(vec2 ** 2)))


def get_top_results_tfidf_noindex(query, vectorizer, word2id, X_tfidf, que, qlist, alist):
    top = 1
    query_tfidf = computeSentenceEach(query.lower(), vectorizer, word2id)
    for i, vec in enumerate(X_tfidf):
        result = cosineSimilarity(vec, query_tfidf)
        que.put((-1 * result, i))
    i = 0
    top_idxs = []
    top_scores = []
    while (i < top and not que.empty()):
        qidx = que.get()
        top_idxs.append(qidx[1])
        top_scores.append(qidx[0])
        i += 1
    print(top_idxs)
    if abs(top_idxs[0]) < 0.9:
        similar = False
    else:
        similar = True
    return np.array(qlist)[top_idxs].tolist(), np.array(alist)[top_idxs].tolist(), similar
