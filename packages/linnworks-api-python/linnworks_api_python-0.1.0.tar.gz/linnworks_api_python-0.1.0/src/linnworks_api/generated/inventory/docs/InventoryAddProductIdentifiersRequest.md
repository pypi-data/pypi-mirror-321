# InventoryAddProductIdentifiersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**AddProductIdentifiersRequest**](AddProductIdentifiersRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_add_product_identifiers_request import InventoryAddProductIdentifiersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryAddProductIdentifiersRequest from a JSON string
inventory_add_product_identifiers_request_instance = InventoryAddProductIdentifiersRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryAddProductIdentifiersRequest.to_json())

# convert the object into a dict
inventory_add_product_identifiers_request_dict = inventory_add_product_identifiers_request_instance.to_dict()
# create an instance of InventoryAddProductIdentifiersRequest from a dict
inventory_add_product_identifiers_request_from_dict = InventoryAddProductIdentifiersRequest.from_dict(inventory_add_product_identifiers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


