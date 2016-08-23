#! /Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import json
import athletemodel
import yate

names = athletemodel.get_names_from_store()

print(yate.start_response('application/json'))
print(json.dumps(sorted(names)))