# PurchaseOrderCreatePOsFromInventoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**CreatePOsFromInventoryRequest**](CreatePOsFromInventoryRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_create_pos_from_inventory_request import PurchaseOrderCreatePOsFromInventoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderCreatePOsFromInventoryRequest from a JSON string
purchase_order_create_pos_from_inventory_request_instance = PurchaseOrderCreatePOsFromInventoryRequest.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderCreatePOsFromInventoryRequest.to_json())

# convert the object into a dict
purchase_order_create_pos_from_inventory_request_dict = purchase_order_create_pos_from_inventory_request_instance.to_dict()
# create an instance of PurchaseOrderCreatePOsFromInventoryRequest from a dict
purchase_order_create_pos_from_inventory_request_from_dict = PurchaseOrderCreatePOsFromInventoryRequest.from_dict(purchase_order_create_pos_from_inventory_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


