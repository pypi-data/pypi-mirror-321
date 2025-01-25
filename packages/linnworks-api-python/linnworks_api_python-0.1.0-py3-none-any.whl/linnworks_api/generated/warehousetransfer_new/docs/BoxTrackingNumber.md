# BoxTrackingNumber


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**box_id** | **int** |  | [optional] 
**tracking_number** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.box_tracking_number import BoxTrackingNumber

# TODO update the JSON string below
json = "{}"
# create an instance of BoxTrackingNumber from a JSON string
box_tracking_number_instance = BoxTrackingNumber.from_json(json)
# print the JSON string representation of the object
print(BoxTrackingNumber.to_json())

# convert the object into a dict
box_tracking_number_dict = box_tracking_number_instance.to_dict()
# create an instance of BoxTrackingNumber from a dict
box_tracking_number_from_dict = BoxTrackingNumber.from_dict(box_tracking_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


