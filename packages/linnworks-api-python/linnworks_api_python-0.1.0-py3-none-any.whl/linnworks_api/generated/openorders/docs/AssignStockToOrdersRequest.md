# AssignStockToOrdersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_ids** | **List[str]** |  | [optional] 
**batch_assignment_mode** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.assign_stock_to_orders_request import AssignStockToOrdersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssignStockToOrdersRequest from a JSON string
assign_stock_to_orders_request_instance = AssignStockToOrdersRequest.from_json(json)
# print the JSON string representation of the object
print(AssignStockToOrdersRequest.to_json())

# convert the object into a dict
assign_stock_to_orders_request_dict = assign_stock_to_orders_request_instance.to_dict()
# create an instance of AssignStockToOrdersRequest from a dict
assign_stock_to_orders_request_from_dict = AssignStockToOrdersRequest.from_dict(assign_stock_to_orders_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


