# LocationsDeleteLocationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_stock_location_id** | **str** | Id of the location to delete | [optional] 

## Example

```python
from linnworks_api.generated.locations.models.locations_delete_location_request import LocationsDeleteLocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LocationsDeleteLocationRequest from a JSON string
locations_delete_location_request_instance = LocationsDeleteLocationRequest.from_json(json)
# print the JSON string representation of the object
print(LocationsDeleteLocationRequest.to_json())

# convert the object into a dict
locations_delete_location_request_dict = locations_delete_location_request_instance.to_dict()
# create an instance of LocationsDeleteLocationRequest from a dict
locations_delete_location_request_from_dict = LocationsDeleteLocationRequest.from_dict(locations_delete_location_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


