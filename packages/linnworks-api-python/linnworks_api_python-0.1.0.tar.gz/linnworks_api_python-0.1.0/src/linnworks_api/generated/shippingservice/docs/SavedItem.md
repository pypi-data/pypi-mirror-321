# SavedItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**unit_value** | **float** |  | [optional] 
**unit_value_currency** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.shippingservice.models.saved_item import SavedItem

# TODO update the JSON string below
json = "{}"
# create an instance of SavedItem from a JSON string
saved_item_instance = SavedItem.from_json(json)
# print the JSON string representation of the object
print(SavedItem.to_json())

# convert the object into a dict
saved_item_dict = saved_item_instance.to_dict()
# create an instance of SavedItem from a dict
saved_item_from_dict = SavedItem.from_dict(saved_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


