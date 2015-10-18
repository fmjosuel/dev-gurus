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
import operator
import webapp2
import os #added
from google.appengine.ext.webapp import template #also added

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

        Animator = ["creativity", "open-minded", "artistic-talent", "innovative"]
        #Banker holds the certain attributes for this career
        Banker = ["mathematics", "resilient", "communication"]
        #Software holds the certain attributes for this career
        Software = ["communication", "technical-skills", "innovative"]
        #Doctor holds the certain attributes for this career
        Doctor = ["communication", "patience", "resilient"]
        #Designer holds the certain attributes for this career
        Designer = ["open-minded", "curiosity", "innovative", "artistic-talent"]
        animator_count=0
        banker_count=0
        doctor_count=0
        software_count=0
        designer_count=0

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
        results = {'Animator': animator_count, 'Banker': banker_count, 'Doctor': doctor_count, 'Software': software_count,
                   'Designer': designer_count}
        sorted_results = sorted(results.items(), key=operator.itemgetter(1))
        sorted_results = sorted_results[::-1]
        self.response.out.write('We have the following jobs matched to you:')
        self.response.out.write('</br>')
        for i in range(3):
            self.response.out.write(sorted_results[i][0])
            self.response.out.write('</br>')

app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
