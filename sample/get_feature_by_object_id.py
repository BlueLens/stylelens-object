from __future__ import print_function
from stylelens_object.features import Features
from pprint import pprint
# create an instance of the API class
api_instance = Features()

try:
  api_response = api_instance.get_feature_by_object_id('a2')
  pprint(api_response)
except Exception as e:
  print("Exception when calling get_feature_by_object_id: %s\n" % e)
