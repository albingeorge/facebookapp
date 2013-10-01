from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Template, Context
from facebookapp.forms import FacebookForm
import requests
import re
import json

def home(request):
	d = {'title': 'FacebookApp :: Input Facebook Url'}
	form = FacebookForm(request.POST or None)
	if form.is_valid():
		data = form.cleaned_data
		m = re.match(r".*facebook.com/(?P<company>\w+)/*.*", data['url'])
		try:
			companyName = m.group(1)
		except(AttributeError):
			companyName = 'Invalid URL'
		return HttpResponseRedirect('/companyDetails/?company=' + companyName)
	d['form'] = form
	return render(request, 'home.html', d)

def getCompany(request):
	d = {'title': 'FacebookApp :: Company Details'}
	companyName = request.GET.get('company', '')
	if companyName == 'Invalid URL':
		company = companyName
	else:
		d['companyName'] = companyName
		try:
			company = requests.get("https://graph.facebook.com/" + companyName)
			company = json.loads(company.text)
			name = company['name']
		except:
			company = 'Something went wrong'

	d['text'] = name
	return render(request, 'companyDetails.html', d)
