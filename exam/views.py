from django.shortcuts import render, redirect
from .models import Test, Question, Option, Answer
import uuid

def test_list(request):
    tests = Test.objects.all()
    return render(request, 'exam/test_list.html', {'tests': tests})

def start_test(request, test_id):
    test = Test.objects.get(pk=test_id)
    session_id = str(uuid.uuid4())
    request.session['session_id'] = session_id
    return render(request, 'exam/test_detail.html', {'test': test, 'session_id': session_id})

def submit_test(request, test_id):
    test = Test.objects.get(pk=test_id)
    session_id = request.session.get('session_id')
    for question in test.question_set.all():
        selected = request.POST.get(str(question.id))
        if selected:
            Answer.objects.create(
                question=question,
                selected_option=Option.objects.get(pk=selected),
                session_id=session_id
            )
    return redirect('result', test_id=test.id)

def result(request, test_id):
    test = Test.objects.get(pk=test_id)
    session_id = request.session.get('session_id')
    answers = Answer.objects.filter(session_id=session_id)
    correct = sum([1 for a in answers if a.selected_option.is_correct])
    total = test.question_set.count()
    return render(request, 'exam/result.html', {
        'test': test,
        'score': correct,
        'total': total
    })
