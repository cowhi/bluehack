import json
from os.path import join, dirname
from watson_developer_cloud import PersonalityInsightsV3
import generator

"""
The example returns a JSON response whose content is the same as that in
   ../resources/personality-v3-expect2.txt
"""

json_example1 = {
   "contentItems": [
      {
         "content": "Wow, I liked @TheRock before, now I really SEE how special he is. The daughter story was IT for me. So great! #MasterClass"
      },
      {
         "content": ".@TheRock how did you Know to listen to your gut and Not go back to football? #Masterclass"
      }
    ]
}

personality_insights = PersonalityInsightsV3(
    version='2016-10-20',
    username='1047ef84-6f8b-4657-98c8-a25190589099',
    password='6wt4CYpxpEzp')

def get_insight(json_dict):
    profile = personality_insights.profile(
        json_dict, content_type='application/json',
        raw_scores=True, consumption_preferences=True)

    print(json.dumps(profile, indent=2))

def get_insight_file(json_file = './resources/personality-v3.json'):
    with open(json_file) as profile_json:
        get_insight(profile_json.read())

if __name__ == "__main__":
    json_example = generator_api.get_list_text_amazon(UserID = 1234)
    get_insight(json_example)
    #get_insight_file()
