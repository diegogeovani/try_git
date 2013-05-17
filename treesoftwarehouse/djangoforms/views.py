from django.shortcuts import render
from django.http import HttpResponseRedirect
from djangoforms.forms import ContactForm

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.clened_data['subject']
			message  = form.clened_data['message']
			sender = form.clened_data['sender']
			cc_myself = form.clened_data['cc_myself']
			recipients = ['diego@agenciatree.com']
			
			if cc_myself:
				recipients.append(sender)
				send_mail(subject, message, sender, recipients)									
				return HttpResponseRedirect('/thanks/')
	else:
		form = ContactForm()
	return render(request, 'djangoforms/contact.html', {'form' : form,})
