# ImageData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**is_enabled** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.image_data import ImageData

# TODO update the JSON string below
json = "{}"
# create an instance of ImageData from a JSON string
image_data_instance = ImageData.from_json(json)
# print the JSON string representation of the object
print(ImageData.to_json())

# convert the object into a dict
image_data_dict = image_data_instance.to_dict()
# create an instance of ImageData from a dict
image_data_from_dict = ImageData.from_dict(image_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


