from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Template, Context
from facebookapp.forms import FacebookForm
import requests
import re

def home(request):
	d = {'title': 'FacebookApp :: Input Facebook Url'}
	form = FacebookForm(request.POST or None)
	if form.is_valid():
		data = form.cleaned_data
		return HttpResponseRedirect('/companyDetails/?company=' + data['url'])
	d['form'] = form
	return render(request, 'home.html', d)

def getCompany(request):
	d = {'title': 'FacebookApp :: Company Details'}
	url = request.GET.get('company', '')
	m = re.match(r".*facebook.com/(?P<company>\w+)/*.*", url)
	try:
		companyName = m.group(1)
	except(AttributeError):
		companyName = 'Invalid URL'
	company = requests.get("https://graph.facebook.com/" + companyName)
	d['text'] = company.text
	return render(request, 'companyDetails.html', d)
