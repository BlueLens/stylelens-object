from __future__ import print_function
from stylelens_object.objects import Objects
from pprint import pprint
# create an instance of the API class
api_instance = Objects()

try:
  api_response = api_instance.delete_all()
  pprint(api_response)
except Exception as e:
  print("Exception when calling ProductApi->update_objects: %s\n" % e)
