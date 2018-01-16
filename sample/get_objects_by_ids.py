from __future__ import print_function
from stylelens_object.objects import Objects
from pprint import pprint
# create an instance of the API class
api_instance = Objects()

version_id = "5a50d4ba4dfd7d90b8b9369a"
ids = ["5a5aebb1ca4ad59194b698b2", "5a5aebb2ca4ad59194b698e2"]

try:
  api_response = api_instance.get_objects_by_ids(ids=ids, version_id=version_id)
  pprint(api_response)
except Exception as e:
  print("Exception when calling get_objects_by_ids: %s\n" % e)
