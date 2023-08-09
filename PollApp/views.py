from django.shortcuts import render
from django.views import View

from PollApp.models import Poll, Choice, Vote

# Create your views here.

# This HomeView will be the home page, were we'll show all the polls list
class HomeView(View):

    def get(self, request):
        poll = Poll.objects.all()
        return render(
            request,
            template_name="home.html",
            context={
                "polls": poll,
            }
        )
# when the user clciks on a poll, it'll take the user to the page where they can vote on the poll.
class PollView(View):

    def get(self, request, poll_id):
        poll = Poll.objects.get(id=poll_id)
        return render(
            request,
            template_name="poll.html",
            context={
                "poll": poll,
            }
        )
    
    def post(self, request, poll_id):
        requestData = request.POST

        choice_id = requestData.get('choice_id')

        poll = Poll.objects.get(id=poll_id)
        choice = Choice.objects.get(id=choice_id)
        Vote.objects.create(
            poll=poll,
            choice=choice,
        )
        poll_results = []
        for choice in poll.choices.all():
            voteCount = Vote.objects.filter(poll=poll, choice=choice).count()
            poll_results.append([choice.choice_text, voteCount])

        return render(
            request,
            template_name="poll.html",
            context={
                "poll": poll,
                "success_message": "Voted Successfully",
                "poll_results": poll_results,
            }
        )