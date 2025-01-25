# WarehouseTransferItemQuantity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fk_stock_item_id** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**pk_transfer_item_id** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer.models.warehouse_transfer_item_quantity import WarehouseTransferItemQuantity

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseTransferItemQuantity from a JSON string
warehouse_transfer_item_quantity_instance = WarehouseTransferItemQuantity.from_json(json)
# print the JSON string representation of the object
print(WarehouseTransferItemQuantity.to_json())

# convert the object into a dict
warehouse_transfer_item_quantity_dict = warehouse_transfer_item_quantity_instance.to_dict()
# create an instance of WarehouseTransferItemQuantity from a dict
warehouse_transfer_item_quantity_from_dict = WarehouseTransferItemQuantity.from_dict(warehouse_transfer_item_quantity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


