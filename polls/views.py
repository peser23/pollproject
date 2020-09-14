from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Question, Choice


def index(request):
    latest_questions_list = Question.objects.order_by('-pub_date')[:5:]
    output = '\n'.join(q.question_text for q in latest_questions_list)
    return render(request, 'polls/index.html', {'latest_questions_list':latest_questions_list})


class IndexView(generic.ListView):
    model = Question
    template_name = 'polls/index.html'
    context_object_name = 'latest_questions_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5:]


def detail(request, question_id):
    #question = Question.objects.get(pk=question_id)
    question = get_object_or_404(Question, pk=question_id)

    context = {'question': question}
    return render(request, 'polls/detail.html', context)


class DetailView(generic.DetailView):
    model = Question
    context_object_name = 'question'
    template_name = 'polls/detail.html'


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


class ResultsView(generic.DetailView):
    model = Question
    context_object_name = 'question'
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:ques-results', args=(question.id,)))


