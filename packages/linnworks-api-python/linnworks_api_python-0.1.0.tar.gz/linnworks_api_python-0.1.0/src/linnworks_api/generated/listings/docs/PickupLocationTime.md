# PickupLocationTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e_bay_location** | **str** |  | [optional] 
**fulfillment_value** | **int** |  | [optional] 
**fulfillment_type** | **str** |  | [optional] 
**extended_property_value** | **str** |  | [optional] 
**extended_property_type** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.pickup_location_time import PickupLocationTime

# TODO update the JSON string below
json = "{}"
# create an instance of PickupLocationTime from a JSON string
pickup_location_time_instance = PickupLocationTime.from_json(json)
# print the JSON string representation of the object
print(PickupLocationTime.to_json())

# convert the object into a dict
pickup_location_time_dict = pickup_location_time_instance.to_dict()
# create an instance of PickupLocationTime from a dict
pickup_location_time_from_dict = PickupLocationTime.from_dict(pickup_location_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


