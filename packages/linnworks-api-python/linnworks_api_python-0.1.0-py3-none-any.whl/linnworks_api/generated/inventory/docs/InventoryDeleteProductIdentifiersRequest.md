# InventoryDeleteProductIdentifiersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**DeleteProductIdentifiersRequest**](DeleteProductIdentifiersRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_delete_product_identifiers_request import InventoryDeleteProductIdentifiersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryDeleteProductIdentifiersRequest from a JSON string
inventory_delete_product_identifiers_request_instance = InventoryDeleteProductIdentifiersRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryDeleteProductIdentifiersRequest.to_json())

# convert the object into a dict
inventory_delete_product_identifiers_request_dict = inventory_delete_product_identifiers_request_instance.to_dict()
# create an instance of InventoryDeleteProductIdentifiersRequest from a dict
inventory_delete_product_identifiers_request_from_dict = InventoryDeleteProductIdentifiersRequest.from_dict(inventory_delete_product_identifiers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


