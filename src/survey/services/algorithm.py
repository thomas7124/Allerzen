import json
from survey.templatetags.survey_tags import remove_underscores

with open('survey/allergies.json', 'r') as json_file:
    json_data = json.load(json_file)['allergies']


allergies = None
def clear_allergies():
    global allergies
    allergies = {"pollen":0, "mold":0, "dust":0, "latex":0, "insects":0,
                 "pets":0, "medication":0, "food":0}

'''
class Survey:
    def __init__(self):
        self.symptoms = ["runny nose", "itchy"]
        self.seasons = ["April", "May", "June"]
'''


class BaseCalc:
    @staticmethod
    def rank_by_indicator(survey, indicator, points):
        attr_list = survey.getlist(indicator)
        print(attr_list)
        for key in allergies:
            for symptom in attr_list:
                symptom = remove_underscores(symptom)
                if symptom in json_data[key][indicator]:
                    allergies[key] += points


class Symptoms(BaseCalc):
    next_chain = None

    def set_next_chain(self, next_chain):
        self.next_chain = next_chain

    def calculate(self, survey):
        print("calculating symptoms")
        self.rank_by_indicator(survey, "symptoms", 10)
        return self.next_chain.calculate(survey)


class Seasons(BaseCalc):
    next_chain = None

    def set_next_chain(self, next_chain):
        self.next_chain = next_chain

    def calculate(self, survey):
        print("calculating")
        self.rank_by_indicator(survey, "seasons", 10)
        return self.next_chain.calculate()


class Result:
    def calculate(self):
        print(allergies)

        values = []

        for i in allergies:
            values.append(allergies[i])
        values.sort()

        highest = []

        for i in allergies:
            if values[-1] == allergies[i]:
                highest.append(i)

        print(highest)

        return f"You may have problems with: {highest}".replace("[", "").replace("]", '').replace("'", '')


#survey = Survey()

algo = Symptoms()
seas = Seasons()
result = Result()

algo.set_next_chain(seas)
seas.set_next_chain(result)
