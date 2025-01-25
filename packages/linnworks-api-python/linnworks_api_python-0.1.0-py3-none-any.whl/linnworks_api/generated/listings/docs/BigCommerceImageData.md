# BigCommerceImageData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thumb** | **bool** |  | [optional] 
**sort_order** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**is_child** | **bool** |  | [optional] 
**image_id** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**show** | **bool** |  | [optional] 
**is_native** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.big_commerce_image_data import BigCommerceImageData

# TODO update the JSON string below
json = "{}"
# create an instance of BigCommerceImageData from a JSON string
big_commerce_image_data_instance = BigCommerceImageData.from_json(json)
# print the JSON string representation of the object
print(BigCommerceImageData.to_json())

# convert the object into a dict
big_commerce_image_data_dict = big_commerce_image_data_instance.to_dict()
# create an instance of BigCommerceImageData from a dict
big_commerce_image_data_from_dict = BigCommerceImageData.from_dict(big_commerce_image_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


