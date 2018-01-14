from __future__ import print_function
from stylelens_object.features import Features
from pprint import pprint
# create an instance of the API class
api_instance = Features()

try:
  offset = 0
  limit = 10
  api_response = api_instance.get_features(offset=offset, limit=limit)
  pprint(api_response)
except Exception as e:
  print("Exception when calling get_features: %s\n" % e)
