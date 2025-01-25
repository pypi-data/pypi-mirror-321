# OrderItemBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_identifiers** | [**List[ProductIdentifier]**](ProductIdentifier.md) |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**barcode_number** | **str** |  | [optional] 
**item_title** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.order_item_base import OrderItemBase

# TODO update the JSON string below
json = "{}"
# create an instance of OrderItemBase from a JSON string
order_item_base_instance = OrderItemBase.from_json(json)
# print the JSON string representation of the object
print(OrderItemBase.to_json())

# convert the object into a dict
order_item_base_dict = order_item_base_instance.to_dict()
# create an instance of OrderItemBase from a dict
order_item_base_from_dict = OrderItemBase.from_dict(order_item_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


