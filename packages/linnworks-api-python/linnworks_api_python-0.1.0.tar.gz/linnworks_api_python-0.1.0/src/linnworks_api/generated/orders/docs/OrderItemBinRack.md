# OrderItemBinRack


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **int** |  | [optional] 
**bin_rack** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**batch_id** | **int** |  | [optional] 
**order_item_batch_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.order_item_bin_rack import OrderItemBinRack

# TODO update the JSON string below
json = "{}"
# create an instance of OrderItemBinRack from a JSON string
order_item_bin_rack_instance = OrderItemBinRack.from_json(json)
# print the JSON string representation of the object
print(OrderItemBinRack.to_json())

# convert the object into a dict
order_item_bin_rack_dict = order_item_bin_rack_instance.to_dict()
# create an instance of OrderItemBinRack from a dict
order_item_bin_rack_from_dict = OrderItemBinRack.from_dict(order_item_bin_rack_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


