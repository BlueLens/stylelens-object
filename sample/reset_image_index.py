from __future__ import print_function
from stylelens_object.objects import Objects
from pprint import pprint
# create an instance of the API class
api_instance = Objects()

try:
  api_response = api_instance.reset_image_index()
  pprint(api_response)
except Exception as e:
  print("Exception when calling reset_image_index: %s\n" % e)
