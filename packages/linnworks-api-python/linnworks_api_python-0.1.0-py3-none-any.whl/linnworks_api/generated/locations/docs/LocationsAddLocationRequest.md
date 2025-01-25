# LocationsAddLocationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | [**StockLocation**](StockLocation.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.locations.models.locations_add_location_request import LocationsAddLocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LocationsAddLocationRequest from a JSON string
locations_add_location_request_instance = LocationsAddLocationRequest.from_json(json)
# print the JSON string representation of the object
print(LocationsAddLocationRequest.to_json())

# convert the object into a dict
locations_add_location_request_dict = locations_add_location_request_instance.to_dict()
# create an instance of LocationsAddLocationRequest from a dict
locations_add_location_request_from_dict = LocationsAddLocationRequest.from_dict(locations_add_location_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


