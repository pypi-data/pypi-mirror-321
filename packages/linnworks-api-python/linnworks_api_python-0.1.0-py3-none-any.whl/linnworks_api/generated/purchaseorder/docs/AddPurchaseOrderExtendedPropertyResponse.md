# AddPurchaseOrderExtendedPropertyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[PurchaseOrderExtendedProperty]**](PurchaseOrderExtendedProperty.md) | Added purchase order extended properties | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.add_purchase_order_extended_property_response import AddPurchaseOrderExtendedPropertyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddPurchaseOrderExtendedPropertyResponse from a JSON string
add_purchase_order_extended_property_response_instance = AddPurchaseOrderExtendedPropertyResponse.from_json(json)
# print the JSON string representation of the object
print(AddPurchaseOrderExtendedPropertyResponse.to_json())

# convert the object into a dict
add_purchase_order_extended_property_response_dict = add_purchase_order_extended_property_response_instance.to_dict()
# create an instance of AddPurchaseOrderExtendedPropertyResponse from a dict
add_purchase_order_extended_property_response_from_dict = AddPurchaseOrderExtendedPropertyResponse.from_dict(add_purchase_order_extended_property_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


