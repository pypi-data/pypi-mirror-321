# OpenOrderItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**composite_child** | [**List[OrderItemBase]**](OrderItemBase.md) |  | [optional] 
**product_identifiers** | [**List[ProductIdentifier]**](ProductIdentifier.md) |  | [optional] 
**contains_composites** | **bool** |  | [optional] [readonly] 
**stock_item_id** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**barcode_number** | **str** |  | [optional] 
**item_title** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.open_order_item import OpenOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of OpenOrderItem from a JSON string
open_order_item_instance = OpenOrderItem.from_json(json)
# print the JSON string representation of the object
print(OpenOrderItem.to_json())

# convert the object into a dict
open_order_item_dict = open_order_item_instance.to_dict()
# create an instance of OpenOrderItem from a dict
open_order_item_from_dict = OpenOrderItem.from_dict(open_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


