from django.contrib import admin
from PollApp.models import Poll, Choice, Vote
# Register your models here.

# add the models to the databse and admin site
admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Vote)