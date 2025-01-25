# BigCommerceConfigAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**max_length** | **int** |  | [optional] 
**label** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**extended_property** | **str** |  | [optional] 
**default** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.big_commerce_config_attributes import BigCommerceConfigAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of BigCommerceConfigAttributes from a JSON string
big_commerce_config_attributes_instance = BigCommerceConfigAttributes.from_json(json)
# print the JSON string representation of the object
print(BigCommerceConfigAttributes.to_json())

# convert the object into a dict
big_commerce_config_attributes_dict = big_commerce_config_attributes_instance.to_dict()
# create an instance of BigCommerceConfigAttributes from a dict
big_commerce_config_attributes_from_dict = BigCommerceConfigAttributes.from_dict(big_commerce_config_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


