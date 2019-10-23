from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, Http404
from .models import Poll
from django.template import loader
def index(request):

    latest_poll_list = Poll.objects.order_by('-pub_date')[:5] # decreased order
    #latest_poll_list = Poll.objects.order_by('pub_date')[:5] # increased order
    context = {
        'latest_poll_list': latest_poll_list,
    }
    return render(request, 'polls/index.html', context)
    # -------------------------------
    # latest_pool_list = Poll.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_pool_list': latest_pool_list,
    # }
    return HttpResponse(template.render(context,request))
    # --------------------------------
    # latest_pool_list = Poll.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_txt for q in latest_pool_list])
    # return HttpResponse(output)

    #return HttpResponse("Hellow, world. You're at the polls index.")

from django.shortcuts import get_object_or_404

def detail(request, poll_id):

    poll = get_object_or_404(Poll,pk=poll_id)
    '''
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404("Poll {} does not exist!".format(poll_id))
    '''
    return render(request, 'polls/detail.html',{'poll': poll})
    #return HttpResponse("You're looking at {}".format(poll_id))

def results(request, poll_id):
    # response = "You're looking at the results of question {}.".format(poll_id)
    # return HttpResponse(response)
    poll = get_object_or_404(Poll,pk=poll_id)
    #return render(request, reverse('ds_polls:results'), {'poll':poll})
    return render(request, 'polls/results.html', {'poll':poll})

from django.urls import reverse
from .models import Choice
from django.http import HttpResponseRedirect

def vote(request, poll_id):
    # return HttpResponse("You're voting on the poll {}".format(poll_id))
    poll = get_object_or_404(Poll,pk=poll_id)
    try:
        selected_choice = poll.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form (detail)
        #return render(request, reverse('ds_polls:detail'), {
        return render(request, 'polls/detail.html', {
            'poll':poll,
            'error_message':"You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('ds_polls:results', args=(poll.id,)))
