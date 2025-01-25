# OptionValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_v3** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**mapped_from_bc** | **bool** |  | [optional] 
**sort_order** | **int** |  | [optional] 
**label** | **str** |  | [optional] 
**option_value_data** | [**OptionValueData**](OptionValueData.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.option_value import OptionValue

# TODO update the JSON string below
json = "{}"
# create an instance of OptionValue from a JSON string
option_value_instance = OptionValue.from_json(json)
# print the JSON string representation of the object
print(OptionValue.to_json())

# convert the object into a dict
option_value_dict = option_value_instance.to_dict()
# create an instance of OptionValue from a dict
option_value_from_dict = OptionValue.from_dict(option_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


