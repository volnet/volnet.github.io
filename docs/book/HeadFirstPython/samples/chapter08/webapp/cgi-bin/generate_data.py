#! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import cgi
import json
import athletemodel
import yate
import sys

athletes = athletemodel.get_from_store()
form_data = cgi.FieldStorage()
athlete_name = form_data["which_athlete"].value

print("athlete_name:" + athlete_name)

print(yate.start_response('application/json'))
print(json.dumps(athletes[athlete_name].as_dict))