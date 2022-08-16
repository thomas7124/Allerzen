from django.shortcuts import render
import json
from survey.services.algorithm import *

with open('survey/allergies.json', 'r') as json_file:
    allergies = json.load(json_file)['allergies']

allergy_types = list(allergies.keys())


symptoms = []


for key in allergies:
    symptoms += allergies[key]["symptoms"]
symptoms = set(symptoms)
print(symptoms)


all_symptoms = []

for sym in symptoms:
    item = sym.replace(" ", "_").replace("/", "_")
    all_symptoms.append(item)

allergy_symptoms = []
temp = []

for i in range(len(all_symptoms)):
    temp.append(all_symptoms[i])
    if i % 3 == 2:
        allergy_symptoms.append(temp)
        temp = []
# loop through all_symptoms list and
# append an empty list containing 3 items in it
print(allergy_symptoms)

seasons = [["January", "February", "March", "April"], ["May",
           "June", "July", "August"], ["September", "October",
           "November", "December"]]

medical_conditions = [["Asthma", "Eczema", "Hay Fever"],
                      ["Lactose Intolerance", "Celiac Disease", "Oral Allergy Syndrome"]]


# Create your views here.
def homeview(request):
    print("user goes to website")


    data = {
        "symptoms_matrix": allergy_symptoms,
        "seasons":seasons,
        "medical_conditions": medical_conditions,
        "allergies": allergy_types
    }

    if request.method == "GET":
        return render(request, 'home.html', data)
    elif request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get('last_name')
        age = request.POST.get("age")
        clear_allergies()
        result = algo.calculate(request.POST)
        data['result'] = result
        print(result)

        return render(request, "home.html", data)