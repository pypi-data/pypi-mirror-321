# GetPurchaseOrderExtendedPropertyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purchase_id** | **str** | Purchase Order unique identifier | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.get_purchase_order_extended_property_request import GetPurchaseOrderExtendedPropertyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetPurchaseOrderExtendedPropertyRequest from a JSON string
get_purchase_order_extended_property_request_instance = GetPurchaseOrderExtendedPropertyRequest.from_json(json)
# print the JSON string representation of the object
print(GetPurchaseOrderExtendedPropertyRequest.to_json())

# convert the object into a dict
get_purchase_order_extended_property_request_dict = get_purchase_order_extended_property_request_instance.to_dict()
# create an instance of GetPurchaseOrderExtendedPropertyRequest from a dict
get_purchase_order_extended_property_request_from_dict = GetPurchaseOrderExtendedPropertyRequest.from_dict(get_purchase_order_extended_property_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


