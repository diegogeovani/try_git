from polls.models import Poll
from django.contrib import admin

class PollAdmin(admin.ModelAdmin):
	fieldsets = [('Date information', {'fields' : ['pub_date'], 'classes' : ['collapse']}), 
                     (None,	          {'fields' : ['question']}),
	]

admin.site.register(Poll, PollAdmin)
