# MagentoConfigAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**extended_property** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**requirement** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.magento_config_attributes import MagentoConfigAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of MagentoConfigAttributes from a JSON string
magento_config_attributes_instance = MagentoConfigAttributes.from_json(json)
# print the JSON string representation of the object
print(MagentoConfigAttributes.to_json())

# convert the object into a dict
magento_config_attributes_dict = magento_config_attributes_instance.to_dict()
# create an instance of MagentoConfigAttributes from a dict
magento_config_attributes_from_dict = MagentoConfigAttributes.from_dict(magento_config_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


