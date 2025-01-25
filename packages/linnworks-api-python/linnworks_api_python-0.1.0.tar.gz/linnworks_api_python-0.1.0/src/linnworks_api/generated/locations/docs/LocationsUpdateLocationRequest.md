# LocationsUpdateLocationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | [**StockLocation**](StockLocation.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.locations.models.locations_update_location_request import LocationsUpdateLocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LocationsUpdateLocationRequest from a JSON string
locations_update_location_request_instance = LocationsUpdateLocationRequest.from_json(json)
# print the JSON string representation of the object
print(LocationsUpdateLocationRequest.to_json())

# convert the object into a dict
locations_update_location_request_dict = locations_update_location_request_instance.to_dict()
# create an instance of LocationsUpdateLocationRequest from a dict
locations_update_location_request_from_dict = LocationsUpdateLocationRequest.from_dict(locations_update_location_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


