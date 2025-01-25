# MagentoVariationsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**prices** | [**List[VariationsAttributesPrices]**](VariationsAttributesPrices.md) |  | [optional] 
**id** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**extended_property** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**requirement** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.magento_variations_attributes import MagentoVariationsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of MagentoVariationsAttributes from a JSON string
magento_variations_attributes_instance = MagentoVariationsAttributes.from_json(json)
# print the JSON string representation of the object
print(MagentoVariationsAttributes.to_json())

# convert the object into a dict
magento_variations_attributes_dict = magento_variations_attributes_instance.to_dict()
# create an instance of MagentoVariationsAttributes from a dict
magento_variations_attributes_from_dict = MagentoVariationsAttributes.from_dict(magento_variations_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


