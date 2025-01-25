# InventoryDeleteSuppliersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**suppliers_ids** | **List[str]** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_delete_suppliers_request import InventoryDeleteSuppliersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryDeleteSuppliersRequest from a JSON string
inventory_delete_suppliers_request_instance = InventoryDeleteSuppliersRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryDeleteSuppliersRequest.to_json())

# convert the object into a dict
inventory_delete_suppliers_request_dict = inventory_delete_suppliers_request_instance.to_dict()
# create an instance of InventoryDeleteSuppliersRequest from a dict
inventory_delete_suppliers_request_from_dict = InventoryDeleteSuppliersRequest.from_dict(inventory_delete_suppliers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


