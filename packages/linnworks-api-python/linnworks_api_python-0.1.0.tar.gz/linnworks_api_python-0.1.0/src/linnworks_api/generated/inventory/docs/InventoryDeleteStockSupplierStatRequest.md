# InventoryDeleteStockSupplierStatRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_item_id** | **str** | Id of StockItem | [optional] 
**item_supplier_ids** | **List[str]** | List of StockItemSupplierStat | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_delete_stock_supplier_stat_request import InventoryDeleteStockSupplierStatRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryDeleteStockSupplierStatRequest from a JSON string
inventory_delete_stock_supplier_stat_request_instance = InventoryDeleteStockSupplierStatRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryDeleteStockSupplierStatRequest.to_json())

# convert the object into a dict
inventory_delete_stock_supplier_stat_request_dict = inventory_delete_stock_supplier_stat_request_instance.to_dict()
# create an instance of InventoryDeleteStockSupplierStatRequest from a dict
inventory_delete_stock_supplier_stat_request_from_dict = InventoryDeleteStockSupplierStatRequest.from_dict(inventory_delete_stock_supplier_stat_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


