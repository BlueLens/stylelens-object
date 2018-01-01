from __future__ import print_function
from stylelens_object.objects import Objects
from pprint import pprint
# create an instance of the API class
api_instance = Objects()

try:
  api_response = api_instance.get_objects("5a49b8e54dfd7d90b8786df8", is_indexed=False)
  pprint(api_response)
except Exception as e:
  print("Exception when calling get_objects: %s\n" % e)
