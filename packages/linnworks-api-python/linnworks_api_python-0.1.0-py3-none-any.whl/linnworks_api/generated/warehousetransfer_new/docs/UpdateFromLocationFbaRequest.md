# UpdateFromLocationFbaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_location_id** | **str** |  | [optional] 
**shipping_plan_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.update_from_location_fba_request import UpdateFromLocationFbaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFromLocationFbaRequest from a JSON string
update_from_location_fba_request_instance = UpdateFromLocationFbaRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateFromLocationFbaRequest.to_json())

# convert the object into a dict
update_from_location_fba_request_dict = update_from_location_fba_request_instance.to_dict()
# create an instance of UpdateFromLocationFbaRequest from a dict
update_from_location_fba_request_from_dict = UpdateFromLocationFbaRequest.from_dict(update_from_location_fba_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


