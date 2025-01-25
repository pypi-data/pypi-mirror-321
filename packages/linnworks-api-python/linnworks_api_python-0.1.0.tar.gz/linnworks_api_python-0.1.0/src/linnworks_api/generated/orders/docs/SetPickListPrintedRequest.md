# SetPickListPrintedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_ids** | **List[str]** | A list of orders that should be assigned the IsPrinted value | [optional] 
**batch_assignment_mode** | **str** | If stock batches needs to be assigned this defines how they should be assigned | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.set_pick_list_printed_request import SetPickListPrintedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetPickListPrintedRequest from a JSON string
set_pick_list_printed_request_instance = SetPickListPrintedRequest.from_json(json)
# print the JSON string representation of the object
print(SetPickListPrintedRequest.to_json())

# convert the object into a dict
set_pick_list_printed_request_dict = set_pick_list_printed_request_instance.to_dict()
# create an instance of SetPickListPrintedRequest from a dict
set_pick_list_printed_request_from_dict = SetPickListPrintedRequest.from_dict(set_pick_list_printed_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


