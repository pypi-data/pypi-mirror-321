# DeletePurchaseOrderExtendedPropertyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purchase_id** | **str** | Purchase order unique identifier | [optional] 
**row_ids** | **List[int]** | List of ids to delete | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.delete_purchase_order_extended_property_request import DeletePurchaseOrderExtendedPropertyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeletePurchaseOrderExtendedPropertyRequest from a JSON string
delete_purchase_order_extended_property_request_instance = DeletePurchaseOrderExtendedPropertyRequest.from_json(json)
# print the JSON string representation of the object
print(DeletePurchaseOrderExtendedPropertyRequest.to_json())

# convert the object into a dict
delete_purchase_order_extended_property_request_dict = delete_purchase_order_extended_property_request_instance.to_dict()
# create an instance of DeletePurchaseOrderExtendedPropertyRequest from a dict
delete_purchase_order_extended_property_request_from_dict = DeletePurchaseOrderExtendedPropertyRequest.from_dict(delete_purchase_order_extended_property_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


