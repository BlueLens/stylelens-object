from __future__ import print_function
from stylelens_object.objects import Objects
from pprint import pprint
# create an instance of the API class
api_instance = Objects()

version_id = "5a49b8e54dfd7d90b8786df8"

try:
  api_response = api_instance.get_size_objects(version_id=version_id)
  pprint('total objects: ' + str(api_response))
  api_response = api_instance.get_size_objects(version_id=version_id, is_indexed=True)
  pprint('indexed objects: ' + str(api_response))
  api_response = api_instance.get_size_objects(version_id=version_id, is_indexed=False)
  pprint('Not indexed objects: ' + str(api_response))
except Exception as e:
  print("Exception when calling get_objects_with_null_index: %s\n" % e)
