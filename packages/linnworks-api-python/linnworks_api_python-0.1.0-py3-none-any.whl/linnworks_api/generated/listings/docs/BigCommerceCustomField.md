# BigCommerceCustomField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**big_commerce_id** | **int** |  | [optional] 
**flex_settings_item_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.big_commerce_custom_field import BigCommerceCustomField

# TODO update the JSON string below
json = "{}"
# create an instance of BigCommerceCustomField from a JSON string
big_commerce_custom_field_instance = BigCommerceCustomField.from_json(json)
# print the JSON string representation of the object
print(BigCommerceCustomField.to_json())

# convert the object into a dict
big_commerce_custom_field_dict = big_commerce_custom_field_instance.to_dict()
# create an instance of BigCommerceCustomField from a dict
big_commerce_custom_field_from_dict = BigCommerceCustomField.from_dict(big_commerce_custom_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


