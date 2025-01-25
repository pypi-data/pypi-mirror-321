# UpdateToLocationFbaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to_location_id** | **str** |  | [optional] 
**to_location_tag** | **str** |  | [optional] 
**shipping_plan_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.update_to_location_fba_request import UpdateToLocationFbaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateToLocationFbaRequest from a JSON string
update_to_location_fba_request_instance = UpdateToLocationFbaRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateToLocationFbaRequest.to_json())

# convert the object into a dict
update_to_location_fba_request_dict = update_to_location_fba_request_instance.to_dict()
# create an instance of UpdateToLocationFbaRequest from a dict
update_to_location_fba_request_from_dict = UpdateToLocationFbaRequest.from_dict(update_to_location_fba_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


