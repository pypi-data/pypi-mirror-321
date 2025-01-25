# ChangePurchaseOrderStatusParameter

Change purchase order status. You can change from PENDING to OPEN, from OPEN to DELIVERED, from PARTIAL to DELIVERED

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_purchase_id** | **str** | Purchase order uniqueidentifier | [optional] 
**status** | **str** | Change purchase order status to the specified value | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.change_purchase_order_status_parameter import ChangePurchaseOrderStatusParameter

# TODO update the JSON string below
json = "{}"
# create an instance of ChangePurchaseOrderStatusParameter from a JSON string
change_purchase_order_status_parameter_instance = ChangePurchaseOrderStatusParameter.from_json(json)
# print the JSON string representation of the object
print(ChangePurchaseOrderStatusParameter.to_json())

# convert the object into a dict
change_purchase_order_status_parameter_dict = change_purchase_order_status_parameter_instance.to_dict()
# create an instance of ChangePurchaseOrderStatusParameter from a dict
change_purchase_order_status_parameter_from_dict = ChangePurchaseOrderStatusParameter.from_dict(change_purchase_order_status_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


