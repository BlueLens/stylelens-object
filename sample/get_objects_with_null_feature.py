from __future__ import print_function
from stylelens_object.objects import Objects
from pprint import pprint
# create an instance of the API class
api_instance = Objects()

version_id = "5a47ccfe4dfd7d90b84eb710"

try:
  api_response = api_instance.get_objects_with_null_feature()
  pprint(api_response)
except Exception as e:
  print("Exception when calling get_objects_with_null_feature: %s\n" % e)
