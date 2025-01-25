# UpdatePurchaseOrderExtendedPropertyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purchase_id** | **str** | Purchase order uniqueidentifier | [optional] 
**extended_property_items** | [**List[UpdatePurchaseOrderExtendedPropertyItem]**](UpdatePurchaseOrderExtendedPropertyItem.md) | items to update | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.update_purchase_order_extended_property_request import UpdatePurchaseOrderExtendedPropertyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePurchaseOrderExtendedPropertyRequest from a JSON string
update_purchase_order_extended_property_request_instance = UpdatePurchaseOrderExtendedPropertyRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePurchaseOrderExtendedPropertyRequest.to_json())

# convert the object into a dict
update_purchase_order_extended_property_request_dict = update_purchase_order_extended_property_request_instance.to_dict()
# create an instance of UpdatePurchaseOrderExtendedPropertyRequest from a dict
update_purchase_order_extended_property_request_from_dict = UpdatePurchaseOrderExtendedPropertyRequest.from_dict(update_purchase_order_extended_property_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


