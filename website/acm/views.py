from django.shortcuts import render, redirect
from .forms import  FeedbackForm, UpcomingEventsForm
from .models import UpcomingEvents


def index_view(request):
    return render(request, 'acm/index.html', {})

def our_team_view(request):
    return render(request, 'acm/our_team.html', {})

def feedback(request):
    if request.method == "POST":
        form  = FeedbackForm(request.POST)
        if form.is_valid():
            fdbk = form.save(commit=False)
            print(fdbk)
            fdbk.save()
            return redirect('acm:index')
    else:
        form = FeedbackForm()
        return render(request, 'acm/feedback.html', {
            'form': form,
        })

def upcoming_events(request):
    events = UpcomingEvents.objects.filter(active =  True).order_by('-created')
    return render(request, 'acm/upcoming_events.html', {
        'events': events,
    })
