# InventoryAddSupplierRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supplier** | [**Supplier**](Supplier.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_add_supplier_request import InventoryAddSupplierRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryAddSupplierRequest from a JSON string
inventory_add_supplier_request_instance = InventoryAddSupplierRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryAddSupplierRequest.to_json())

# convert the object into a dict
inventory_add_supplier_request_dict = inventory_add_supplier_request_instance.to_dict()
# create an instance of InventoryAddSupplierRequest from a dict
inventory_add_supplier_request_from_dict = InventoryAddSupplierRequest.from_dict(inventory_add_supplier_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


