# PurchaseOrderGetDeliveredRecordsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_purchase_id** | **str** | PO id | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_get_delivered_records_request import PurchaseOrderGetDeliveredRecordsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderGetDeliveredRecordsRequest from a JSON string
purchase_order_get_delivered_records_request_instance = PurchaseOrderGetDeliveredRecordsRequest.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderGetDeliveredRecordsRequest.to_json())

# convert the object into a dict
purchase_order_get_delivered_records_request_dict = purchase_order_get_delivered_records_request_instance.to_dict()
# create an instance of PurchaseOrderGetDeliveredRecordsRequest from a dict
purchase_order_get_delivered_records_request_from_dict = PurchaseOrderGetDeliveredRecordsRequest.from_dict(purchase_order_get_delivered_records_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


