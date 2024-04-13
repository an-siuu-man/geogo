from django.shortcuts import render
from django import forms
from .api.gptAPI import generateResponse

# Create your views here.
def homepage(request):
    return render(request, 'geogo/homepage.html')

def results(request):

    if request.method == 'POST':

        selected_option = request.POST.get('dropdown')
        
        # You can now use the selected option as needed
        if selected_option == 'MCI':
            origin = 'Kansas City'
        elif selected_option == 'LHR':
            origin = 'London'
        elif selected_option == 'ORD':
            origin = 'Chicago'
        else:
            origin = 'Unknown'

        # response = generateResponse(f'top 10 tourist locations in {origin} in a list with one line descriptions').split('\n')

        # locations = []
        # for i in response:
        #     if i != '':
        #         locations.append(i)
        # Get the selected option from the dropdown menu
        # For demonstration purposes, I'm just returning the selected option as part of the response

        locations = [
    "Eiffel Tower: Iconic wrought-iron lattice tower offering sweeping views of Paris.",
    "Louvre Museum: World's largest art museum and historic monument in Paris.",
    "Notre-Dame Cathedral: Famed Gothic cathedral known for its flying buttresses & gargoyles.",
    "Montmartre: Hill featuring the Basilica of the Sacré-Cœur & artists' square.",
    "Champs-Élysées: Famous avenue lined with shops, theaters, and cafes.",
    "Musée d'Orsay: Museum housed in a Beaux-Arts railway station, known for its Impressionist masterpieces.",
    "Palace of Versailles: Opulent 17th-century palace, the former home of French royalty, surrounded by gardens and fountains.",
    "Seine River Cruise: Scenic boat tours offering views of Paris landmarks such as the Eiffel Tower and Notre-Dame.",
    "Sainte-Chapelle: Gothic chapel known for its stunning stained glass windows.",
    "Musée Rodin: Museum showcasing the works of the French sculptor Auguste Rodin, set in a mansion with gardens."
]
        if origin != 'Unknown':
            return render(request, 'geogo/results.html', {
            'response': locations, 
            'origin':origin
        })

        else:
            return render(request, 'geogo/homepage.html', {
                'invalid_airport':True
                })
    
