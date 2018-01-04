from __future__ import print_function
from stylelens_object.objects import Objects
from pprint import pprint
# create an instance of the API class
api_instance = Objects()

id = "5a4df4c299866d4ecfd0091d"
object = {}
object['image_id'] = 'bok'

try:
  api_response = api_instance.update_object_by_id(id, object)
  pprint(api_response)
except Exception as e:
  print("Exception when calling ProductApi->update_object_by_id: %s\n" % e)
