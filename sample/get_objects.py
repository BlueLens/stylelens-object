from __future__ import print_function
from stylelens_object.objects import Objects
from pprint import pprint
# create an instance of the API class
api_instance = Objects()

try:
  # api_response = api_instance.get_objects("5a50d4ba4dfd7d90b8b9369a",
  #                                         is_indexed=True,
  #                                         image_indexed=True)
  api_response = api_instance.get_objects("5a50d4ba4dfd7d90b8b9369a",
                                          is_indexed=True,
                                          sort_key='index',
                                          sort_order=1
                                          )
  pprint(api_response)
except Exception as e:
  print("Exception when calling get_objects: %s\n" % e)
