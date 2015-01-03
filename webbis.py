#!/usr/local/bin/python
# Webbis class definition

class Webbis:
    'Class containing all data for a Webbis'

    def __init__(self, webid, parents, gender, name, birthdate, birthtime, weight, length, city, comment):
        self.webid = webid
        self.parents = parents
        self.gender = gender
        self.name = name
        self.birthdate = birthdate
        self.birthtime = birthtime
        self.weight = weight
        self.length = length
        self.city = city
        self.comment = comment

    def displayWebbis(self):
        print "Webid: ", self.webid, ", Parents: ", self.parents, ", Gender: ", self.gender, ", Name: ", self.name, ", Birthdate", self.birthdate, ", Birthtime ", self.birthtime, ", Weight ", self.weight, ", Length ", self.length, ", City ", self.city, ", Comment ", self.comment

        
