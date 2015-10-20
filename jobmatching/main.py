#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import jinja2
import operator
import webapp2
import os #added
from google.appengine.ext.webapp import template #also added

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

#handler for the mainpage
class MainPage(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'index.html') #takes index.html in a path variable
        self.response.out.write(template.render(path, {})) #display the rendered path
    def post(self):
        name = self.request.get("name")
        #getting data from the source
        choice1 = self.request.get("choice1")
        choice2 = self.request.get("choice2")
        choice3 = self.request.get("choice3")
        choice4 = self.request.get("choice4")
        choice5 = self.request.get("choice5")
        choice6 = self.request.get("choice6")
        choice7 = self.request.get("choice7")
        choice8 = self.request.get("choice8")
        choice9 = self.request.get("choice9")
        choice10 = self.request.get("choice10")
        choice11= self.request.get("choice11")
        choice12= self.request.get("choice12")
        choice13= self.request.get("choice13")
        choice14= self.request.get("choice14")
        choice15= self.request.get("choice15")
        choice16= self.request.get("choice16")
        choice17= self.request.get("choice17")
        choice18= self.request.get("choice18")
        choice19= self.request.get("choice19")
        choice20= self.request.get("choice20")
        choice21= self.request.get("choice21")
        choice22= self.request.get("choice22")
        choice23 = self.request.get("choice23")
        choice24 = self.request.get("choice24")

        choices = []

        choices.append(choice1)
        choices.append(choice2)
        choices.append(choice3)
        choices.append(choice4)
        choices.append(choice5)
        choices.append(choice6)
        choices.append(choice7)
        choices.append(choice8)
        choices.append(choice9)
        choices.append(choice10)
        choices.append(choice11)
        choices.append(choice12)
        choices.append(choice13)
        choices.append(choice14)
        choices.append(choice15)
        choices.append(choice16)
        choices.append(choice17)
        choices.append(choice18)
        choices.append(choice19)
        choices.append(choice20)
        choices.append(choice21)
        choices.append(choice22)
        choices.append(choice23)
        choices.append(choice24)

        len_choice = 0
        for i in choices:
            if i:
                len_choice+=1

        '''
            "patience", "communication", "mathematics", "creativity", "open-minded",
            "innovative", "artistic-talent", "curiosity", "resilient", "sleeping",
            "socializing", "watching", "cooking", "eating", "dressing", "cleaning",
            "travelling", "photography", "budgeting", "shopping", "crafting", "technical-skills",
            "adaptability", "music"

        '''
        Animator = ["creativity", "open-minded", "artistic-talent", "innovative", ]
        #Banker holds the certain attributes for this career
        Banker = ["mathematics", "resilient", "communication", "budgeting",
                  "resilient"]
        #Software holds the certain attributes for this career
        Software = ["communication", "technical-skills", "innovative", "resilient",
                    "curiosity", "mathematics"]
        #Doctor holds the certain attributes for this career
        Doctor = ["communication", "patience", "resilient"]
        #Designer holds the certain attributes for this career
        Designer = ["open-minded", "curiosity", "innovative", "artistic-talent",
                    "dressing", "music"],
        #Journalist holds the certain attributes for this career
        Journalist = ["writing", "curiosity", "open-minded", "adaptability",
                      "artistic-talent", "travelling", "adaptability",
                      "socializing and communicating"]
        #Photograph holds the certain attributes for this career
        Photographer = ["travelling", "photography", "adaptability","creativity",]

        Chief= ["cooking", "creativity", "patience", "shopping", "eating", "cleaning"]

        animator_count=0
        banker_count=0
        doctor_count=0
        software_count=0
        designer_count=0
        journalist_count=0
        photographer_count=0
        chief_count = 0

        for i in choices:
            if i in Animator:
                animator_count+=1
            if i in Banker:
                banker_count+=1
            if i in Software:
                software_count+=1
            if i in Doctor:
                doctor_count+=1
            if i in Designer:
                designer_count+=1
            if i in Journalist:
                journalist_count+=1
            if i in Photographer:
                photographer_count+=1
            if i in Chief:
                chief_count+=1
        results = {'Animator': animator_count, 'Banker': banker_count, 'Doctor': doctor_count, 'Software': software_count,
                   'Designer': designer_count, 'Journalist': journalist_count, 'Photographer': photographer_count,
                   'Chef': chief_count}
        animator_perc = animator_count *100/len_choice
        banker_perc = banker_count * 100 /len_choice
        software_perc =  software_count*100/len_choice

        doctor_perc = doctor_count * 100 /len_choice
        designer_perc = designer_count *100/len_choice
        journalist_perc = journalist_count * 100 /len_choice
        photographer_perc = photographer_count *100/len_choice
        chief_perc = chief_count * 100 /len_choice

        result_perc = {'Animator': animator_perc, 'Banker': banker_perc, 'Doctor': doctor_perc, 'Software': software_perc,
                   'Designer': designer_perc, 'Journalist': journalist_perc, 'Photographer': photographer_perc,
                   'Chef': chief_perc}
        sorted_results = sorted(results.items(), key=operator.itemgetter(1))
        sorted_results = sorted_results[::-1]
        '''
        self.response.out.write('We have the following jobs matched to you:')
        self.response.out.write('</br>')
        for i in range(3):
            self.response.out.write(sorted_results[i][0])
            self.response.out.write('</br>')
        '''
        template_values = {
            'matching': sorted_results,
            'perc': result_perc
        }
        template = JINJA_ENVIRONMENT.get_template('matching.html')
        self.response.write(template.render(template_values))


class SoftwareHandler(webapp2.RequestHandler):
    def get(self):
        self.redirect("http://www.collegequest.com/how-to-become-a-software-engineer.aspx")
class AnimatorHandler(webapp2.RequestHandler):
    def get(self):
        self.redirect("http://study.com/how_to_become_an_animator.html")
class BankerHandler(webapp2.RequestHandler):
    def get(self):
        self.redirect("http://study.com/articles/How_to_Be_a_Banker_Education_and_Career_Roadmap.html")
class DesignerHandler(webapp2.RequestHandler):
    def get(self):
        self.redirect("https://www.asid.org/content/becoming-interior-designer#.ViOKQXUVhBc")
class JournalistHandler(webapp2.RequestHandler):
    def get(self):
        self.redirect("http://work.chron.com/requirements-necessary-become-journalist-12514.html")
class PhotographerHandler(webapp2.RequestHandler):
    def get(self):
        self.redirect("http://www.digitalcameraworld.com/2015/02/02/become-professional-photographer/")
class ChiefHandler(webapp2.RequestHandler):
    def get(self):
        self.redirect("http://study.com/how_to_become_a_chef.html")


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/Software', SoftwareHandler),
    ('/Animator', AnimatorHandler),
    ('/Banker', BankerHandler),
    ('/Designer', DesignerHandler),
    ('/Journalist', JournalistHandler),
    ('/Photographer', PhotographerHandler),
    ('/Chef', ChiefHandler)
], debug=True)
