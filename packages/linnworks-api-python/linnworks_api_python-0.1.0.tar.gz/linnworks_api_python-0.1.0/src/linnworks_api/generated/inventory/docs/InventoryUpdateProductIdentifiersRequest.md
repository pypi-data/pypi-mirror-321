# InventoryUpdateProductIdentifiersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**UpdateProductIdentifiersRequest**](UpdateProductIdentifiersRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_update_product_identifiers_request import InventoryUpdateProductIdentifiersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryUpdateProductIdentifiersRequest from a JSON string
inventory_update_product_identifiers_request_instance = InventoryUpdateProductIdentifiersRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryUpdateProductIdentifiersRequest.to_json())

# convert the object into a dict
inventory_update_product_identifiers_request_dict = inventory_update_product_identifiers_request_instance.to_dict()
# create an instance of InventoryUpdateProductIdentifiersRequest from a dict
inventory_update_product_identifiers_request_from_dict = InventoryUpdateProductIdentifiersRequest.from_dict(inventory_update_product_identifiers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


