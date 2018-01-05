from __future__ import print_function
from stylelens_object.objects import Objects
from pprint import pprint
# create an instance of the API class
api_instance = Objects()

try:
  api_response = api_instance.get_objects("5a4e3dc74dfd7d90b8885411",
                                          is_indexed=True,
                                          image_indexed=True)
  pprint(api_response)
except Exception as e:
  print("Exception when calling get_objects: %s\n" % e)
