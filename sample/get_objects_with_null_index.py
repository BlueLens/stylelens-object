from __future__ import print_function
from stylelens_object.objects import Objects
from pprint import pprint
# create an instance of the API class
api_instance = Objects()

version_id = "5a50d4ba4dfd7d90b8b9369a"

try:
  api_response = api_instance.get_objects_with_null_index(version_id=version_id, offset=0, limit=100)
  pprint(api_response)
except Exception as e:
  print("Exception when calling get_objects_with_null_index: %s\n" % e)
