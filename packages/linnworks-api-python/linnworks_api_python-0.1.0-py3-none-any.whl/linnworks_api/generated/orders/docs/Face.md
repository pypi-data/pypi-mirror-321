# Face


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**top_left** | [**PointF**](PointF.md) |  | [optional] 
**bottom_left** | [**PointF**](PointF.md) |  | [optional] 
**top_right** | [**PointF**](PointF.md) |  | [optional] 
**bottom_right** | [**PointF**](PointF.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.face import Face

# TODO update the JSON string below
json = "{}"
# create an instance of Face from a JSON string
face_instance = Face.from_json(json)
# print the JSON string representation of the object
print(Face.to_json())

# convert the object into a dict
face_dict = face_instance.to_dict()
# create an instance of Face from a dict
face_from_dict = Face.from_dict(face_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


