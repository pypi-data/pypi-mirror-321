# ChildImage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_name** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**image_id** | **str** |  | [optional] 
**parent_image_id** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.child_image import ChildImage

# TODO update the JSON string below
json = "{}"
# create an instance of ChildImage from a JSON string
child_image_instance = ChildImage.from_json(json)
# print the JSON string representation of the object
print(ChildImage.to_json())

# convert the object into a dict
child_image_dict = child_image_instance.to_dict()
# create an instance of ChildImage from a dict
child_image_from_dict = ChildImage.from_dict(child_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


