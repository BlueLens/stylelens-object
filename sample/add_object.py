from __future__ import print_function
from stylelens_object.objects import Objects
from pprint import pprint
# create an instance of the API class
api_instance = Objects()

object = {}
object['name'] = 'a4'

try:
  # Added a new Object
  api_response = api_instance.add_object(object)
  pprint(api_response)
except Exception as e:
  print("Exception when calling ProductApi->add_object: %s\n" % e)
