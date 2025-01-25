# InventoryCreateStockSupplierStatRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_suppliers** | [**List[StockItemSupplierStat]**](StockItemSupplierStat.md) | List of StockItemSupplierStat | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_create_stock_supplier_stat_request import InventoryCreateStockSupplierStatRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryCreateStockSupplierStatRequest from a JSON string
inventory_create_stock_supplier_stat_request_instance = InventoryCreateStockSupplierStatRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryCreateStockSupplierStatRequest.to_json())

# convert the object into a dict
inventory_create_stock_supplier_stat_request_dict = inventory_create_stock_supplier_stat_request_instance.to_dict()
# create an instance of InventoryCreateStockSupplierStatRequest from a dict
inventory_create_stock_supplier_stat_request_from_dict = InventoryCreateStockSupplierStatRequest.from_dict(inventory_create_stock_supplier_stat_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


