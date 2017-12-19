from __future__ import print_function
from stylelens_object.objects import Objects
from pprint import pprint
# create an instance of the API class
api_instance = Objects()

objects = []
object = {}
object['name'] = 'a1'
object['index'] = 1

object2 = {}
object2['name'] = 'a2'
object2['index'] = 2

object3 = {}
object3['name'] = 'a3'
object3['index'] = 3


objects.append(object)
objects.append(object2)
objects.append(object3)

try:
  api_response = api_instance.update_objects(objects)
  pprint(api_response)
except Exception as e:
  print("Exception when calling ProductApi->update_objects: %s\n" % e)
