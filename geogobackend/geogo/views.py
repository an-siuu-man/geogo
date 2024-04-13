from django.shortcuts import render
from django import forms
from .api.gptAPI import generateResponse

# Create your views here.
def homepage(request):
    return render(request, 'geogo/homepage.html')

def results(request):
    
    response = generateResponse('top 10 tourist locations in Paris in a list with one line descriptions').split('\n')

    parsedResponse = []
    for i in response:
        if i != '':
            parsedResponse.append(i)

    return render(request, 'geogo/results.html', {
        'response': parsedResponse
    })
