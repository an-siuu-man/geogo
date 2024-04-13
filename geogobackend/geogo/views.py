from django.shortcuts import render
from django import forms
from .api.gptAPI import generateResponse

# Create your views here.
def homepage(request):
    return render(request, 'geogo/homepage.html')

def results(request):
    
    # response = generateResponse('top 10 tourist locations in Paris in a list with one line descriptions').split('\n')

    # parsedResponse = []
    # for i in response:
    #     if i != '':
    #         parsedResponse.append(i)

    parsedResponse = ['1. Eiffel Tower: This iconic Parisian landmark offers breathtaking views of the city and is a symbol of French engineering prowess.',
"2. Louvre Museum: The world's largest art museum and historic monument in Paris, famed for housing Da Vinci's Mona Lisa.",
"3. Notre-Dame Cathedral: A stunning example of French Gothic architecture, known for its detailed facades and tragic 2019 fire.",
"4. Montmartre: Known for its bohemian past, cobbled streets and the white-domed Basilica of the Sacré-Cœur on the hilltop.",
"5. Champs-Élysées: This famous avenue is home to luxury shops, cafes and the Arc de Triomphe.",
"6. Palace of Versailles: A grand and opulent former royal residence located outside of Paris, known for its Hall of Mirrors and extensive gardens.",
"7. Seine River Cruise: Offers a unique perspective of the city's landmarks including Notre-Dame Cathedral and Louvre Museum.",
"8. Musée d'Orsay: An art museum housed in a former railway station, featuring extensive collections of impressionist and post-impressionist masterpieces.",
"9. The Latin Quarter: Famous for its vibrant student life, as it's home to the Sorbonne University, and its lively atmosphere with numerous bistros, shops and theatres.",
"10. Sainte-Chapelle: This stunning Gothic chapel is known for its magnificent stained glass windows depicting biblical scenes."]

    return render(request, 'geogo/results.html', {
        'response': parsedResponse
    })
