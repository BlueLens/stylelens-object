from __future__ import print_function
from stylelens_object.features import Features
from pprint import pprint
# create an instance of the API class
api_instance = Features()

try:
  api_response = api_instance.delete_all()
  pprint(api_response)
except Exception as e:
  print("Exception when calling ProductApi->update_objects: %s\n" % e)
