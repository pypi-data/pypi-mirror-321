# AssignStockToOrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** |  | [optional] 
**order_item_rows** | **List[str]** |  | [optional] 
**batch_assignment_mode** | **str** | The way in which batches should be assigned | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.assign_stock_to_order_request import AssignStockToOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssignStockToOrderRequest from a JSON string
assign_stock_to_order_request_instance = AssignStockToOrderRequest.from_json(json)
# print the JSON string representation of the object
print(AssignStockToOrderRequest.to_json())

# convert the object into a dict
assign_stock_to_order_request_dict = assign_stock_to_order_request_instance.to_dict()
# create an instance of AssignStockToOrderRequest from a dict
assign_stock_to_order_request_from_dict = AssignStockToOrderRequest.from_dict(assign_stock_to_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


