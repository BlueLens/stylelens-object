from __future__ import print_function
from stylelens_object.features import Features
from pprint import pprint
# create an instance of the API class
api_instance = Features()

feature = {}
feature['object_id'] = 'a2'
feature['vector'] = 'xxx'

try:
  api_response = api_instance.add_feature(feature)
  pprint(api_response)
except Exception as e:
  print("Exception when calling add_feature: %s\n" % e)
