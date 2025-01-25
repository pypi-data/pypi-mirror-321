# ClearStockAssignmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_ids** | **List[int]** |  | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.clear_stock_assignment_request import ClearStockAssignmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClearStockAssignmentRequest from a JSON string
clear_stock_assignment_request_instance = ClearStockAssignmentRequest.from_json(json)
# print the JSON string representation of the object
print(ClearStockAssignmentRequest.to_json())

# convert the object into a dict
clear_stock_assignment_request_dict = clear_stock_assignment_request_instance.to_dict()
# create an instance of ClearStockAssignmentRequest from a dict
clear_stock_assignment_request_from_dict = ClearStockAssignmentRequest.from_dict(clear_stock_assignment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


