from __future__ import print_function
from stylelens_object.objects import Objects
from pprint import pprint
# create an instance of the API class
api_instance = Objects()

try:
  api_response = api_instance.get_object("5a38b61799866d4ecf9fc596")
  pprint(api_response)
except Exception as e:
  print("Exception when calling ProductApi->add_object: %s\n" % e)
