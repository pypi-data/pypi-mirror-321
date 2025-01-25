# PictureSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**picture_id** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**is_main** | **bool** |  | [optional] 
**sort_order** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.picture_source import PictureSource

# TODO update the JSON string below
json = "{}"
# create an instance of PictureSource from a JSON string
picture_source_instance = PictureSource.from_json(json)
# print the JSON string representation of the object
print(PictureSource.to_json())

# convert the object into a dict
picture_source_dict = picture_source_instance.to_dict()
# create an instance of PictureSource from a dict
picture_source_from_dict = PictureSource.from_dict(picture_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


