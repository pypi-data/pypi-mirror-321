# ChildImagesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**child_id** | **str** |  | [optional] 
**images** | [**List[ChildImage]**](ChildImage.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.child_images_list import ChildImagesList

# TODO update the JSON string below
json = "{}"
# create an instance of ChildImagesList from a JSON string
child_images_list_instance = ChildImagesList.from_json(json)
# print the JSON string representation of the object
print(ChildImagesList.to_json())

# convert the object into a dict
child_images_list_dict = child_images_list_instance.to_dict()
# create an instance of ChildImagesList from a dict
child_images_list_from_dict = ChildImagesList.from_dict(child_images_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


