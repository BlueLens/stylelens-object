from __future__ import print_function
from stylelens_object.objects import Objects
from pprint import pprint
# create an instance of the API class
api_instance = Objects()

object = {}
object['name'] = 'unique_name'
object['product_id'] = '9sfdf876'

try:
  # Added a new Object
  api_response = api_instance.update_object(object)
  pprint(api_response)
except Exception as e:
  print("Exception when calling ProductApi->update_object: %s\n" % e)
