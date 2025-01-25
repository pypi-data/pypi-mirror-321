# MoveToLocationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **List[str]** | List of errors | [optional] 
**orders_moved** | **List[str]** | List of orders that were moved | [optional] 
**keyed_errors** | **Dict[str, str]** | Dictionary of keyed errors. These are the same errors as per the Errors property, but indexable by orderId | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.move_to_location_result import MoveToLocationResult

# TODO update the JSON string below
json = "{}"
# create an instance of MoveToLocationResult from a JSON string
move_to_location_result_instance = MoveToLocationResult.from_json(json)
# print the JSON string representation of the object
print(MoveToLocationResult.to_json())

# convert the object into a dict
move_to_location_result_dict = move_to_location_result_instance.to_dict()
# create an instance of MoveToLocationResult from a dict
move_to_location_result_from_dict = MoveToLocationResult.from_dict(move_to_location_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


