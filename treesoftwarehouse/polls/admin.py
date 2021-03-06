from polls.models import Poll, Choice
from django.contrib import admin

class ChoiceInLine(admin.TabularInline):
	model = Choice
	extra = 3

class PollAdmin(admin.ModelAdmin):
	fieldsets = [('Date information', {'fields' : ['pub_date'], 'classes' : ['collapse']}), 
                     (None,	          {'fields' : ['question']}),
	]
	inlines = [ChoiceInLine]
	list_display = ('question', 'pub_date', 'was_published_today')
	list_filter = ['pub_date']
	date_hierarchy = 'pub_date'
	search_fields = ['question']

admin.site.register(Poll, PollAdmin)

