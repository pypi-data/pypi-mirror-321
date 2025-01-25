# OptionValueData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.option_value_data import OptionValueData

# TODO update the JSON string below
json = "{}"
# create an instance of OptionValueData from a JSON string
option_value_data_instance = OptionValueData.from_json(json)
# print the JSON string representation of the object
print(OptionValueData.to_json())

# convert the object into a dict
option_value_data_dict = option_value_data_instance.to_dict()
# create an instance of OptionValueData from a dict
option_value_data_from_dict = OptionValueData.from_dict(option_value_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


