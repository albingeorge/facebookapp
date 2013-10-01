from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Template, Context
from facebookapp.forms import FacebookForm
import requests

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
	companyName = 
	company = requests.get("https://graph.facebook.com/" + companyName)
	return render(request, 'companyDetails.html', d)
