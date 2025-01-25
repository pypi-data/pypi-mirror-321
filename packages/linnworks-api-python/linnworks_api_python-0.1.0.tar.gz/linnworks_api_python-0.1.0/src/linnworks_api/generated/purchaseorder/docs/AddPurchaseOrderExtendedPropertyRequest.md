# AddPurchaseOrderExtendedPropertyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purchase_id** | **str** | Purchase order uniqueidentifier | [optional] 
**extended_property_items** | [**List[AddPurchaseOrderExtendedPropertyItem]**](AddPurchaseOrderExtendedPropertyItem.md) | List of Extended Properties to be added to the purchase order | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.add_purchase_order_extended_property_request import AddPurchaseOrderExtendedPropertyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddPurchaseOrderExtendedPropertyRequest from a JSON string
add_purchase_order_extended_property_request_instance = AddPurchaseOrderExtendedPropertyRequest.from_json(json)
# print the JSON string representation of the object
print(AddPurchaseOrderExtendedPropertyRequest.to_json())

# convert the object into a dict
add_purchase_order_extended_property_request_dict = add_purchase_order_extended_property_request_instance.to_dict()
# create an instance of AddPurchaseOrderExtendedPropertyRequest from a dict
add_purchase_order_extended_property_request_from_dict = AddPurchaseOrderExtendedPropertyRequest.from_dict(add_purchase_order_extended_property_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


