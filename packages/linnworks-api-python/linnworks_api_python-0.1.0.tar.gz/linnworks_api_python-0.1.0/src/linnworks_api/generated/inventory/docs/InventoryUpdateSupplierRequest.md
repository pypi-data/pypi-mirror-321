# InventoryUpdateSupplierRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supplier** | [**Supplier**](Supplier.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_update_supplier_request import InventoryUpdateSupplierRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryUpdateSupplierRequest from a JSON string
inventory_update_supplier_request_instance = InventoryUpdateSupplierRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryUpdateSupplierRequest.to_json())

# convert the object into a dict
inventory_update_supplier_request_dict = inventory_update_supplier_request_instance.to_dict()
# create an instance of InventoryUpdateSupplierRequest from a dict
inventory_update_supplier_request_from_dict = InventoryUpdateSupplierRequest.from_dict(inventory_update_supplier_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


