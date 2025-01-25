# GetPurchaseOrderExtendedPropertyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[PurchaseOrderExtendedProperty]**](PurchaseOrderExtendedProperty.md) | Purchase order extended properties | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.get_purchase_order_extended_property_response import GetPurchaseOrderExtendedPropertyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPurchaseOrderExtendedPropertyResponse from a JSON string
get_purchase_order_extended_property_response_instance = GetPurchaseOrderExtendedPropertyResponse.from_json(json)
# print the JSON string representation of the object
print(GetPurchaseOrderExtendedPropertyResponse.to_json())

# convert the object into a dict
get_purchase_order_extended_property_response_dict = get_purchase_order_extended_property_response_instance.to_dict()
# create an instance of GetPurchaseOrderExtendedPropertyResponse from a dict
get_purchase_order_extended_property_response_from_dict = GetPurchaseOrderExtendedPropertyResponse.from_dict(get_purchase_order_extended_property_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


