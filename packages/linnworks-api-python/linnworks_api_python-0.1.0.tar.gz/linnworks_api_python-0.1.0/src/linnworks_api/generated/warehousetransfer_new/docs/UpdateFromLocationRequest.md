# UpdateFromLocationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_location_id** | **str** |  | [optional] 
**pk_transfer_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.update_from_location_request import UpdateFromLocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFromLocationRequest from a JSON string
update_from_location_request_instance = UpdateFromLocationRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateFromLocationRequest.to_json())

# convert the object into a dict
update_from_location_request_dict = update_from_location_request_instance.to_dict()
# create an instance of UpdateFromLocationRequest from a dict
update_from_location_request_from_dict = UpdateFromLocationRequest.from_dict(update_from_location_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


