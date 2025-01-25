# MagentoImageData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | **bool** |  | [optional] 
**small** | **bool** |  | [optional] 
**thumb** | **bool** |  | [optional] 
**is_child** | **bool** |  | [optional] 
**image_id** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**show** | **bool** |  | [optional] 
**is_native** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.magento_image_data import MagentoImageData

# TODO update the JSON string below
json = "{}"
# create an instance of MagentoImageData from a JSON string
magento_image_data_instance = MagentoImageData.from_json(json)
# print the JSON string representation of the object
print(MagentoImageData.to_json())

# convert the object into a dict
magento_image_data_dict = magento_image_data_instance.to_dict()
# create an instance of MagentoImageData from a dict
magento_image_data_from_dict = MagentoImageData.from_dict(magento_image_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


