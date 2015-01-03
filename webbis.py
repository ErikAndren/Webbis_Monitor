#!/usr/local/bin/python
# Webbis class definition

class Webbis:
    'Class containing all data for a Webbis'
    webid = -1
    parents = ""
    gender = ""
    name = ""
    birthdate = ""
    birthtime = ""
    weight = "" 
    length = ""
    city = ""
    comment = ""

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
        print "Webid: ", self.webid, ", Parents: ", self.parents, ", gender ", self.gender, ", name: ", self.name, ", birthdate", self.birthdate, ", birthtime ", self.birthtime, ", weight ", self.weight, ", length ", self.length, ", city ", self.city, ", comment ", self.comment

        
