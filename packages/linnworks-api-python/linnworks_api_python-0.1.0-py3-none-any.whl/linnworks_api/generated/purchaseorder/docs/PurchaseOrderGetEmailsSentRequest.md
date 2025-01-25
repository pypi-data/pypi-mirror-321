# PurchaseOrderGetEmailsSentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**GetEmailsSentRequest**](GetEmailsSentRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_get_emails_sent_request import PurchaseOrderGetEmailsSentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderGetEmailsSentRequest from a JSON string
purchase_order_get_emails_sent_request_instance = PurchaseOrderGetEmailsSentRequest.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderGetEmailsSentRequest.to_json())

# convert the object into a dict
purchase_order_get_emails_sent_request_dict = purchase_order_get_emails_sent_request_instance.to_dict()
# create an instance of PurchaseOrderGetEmailsSentRequest from a dict
purchase_order_get_emails_sent_request_from_dict = PurchaseOrderGetEmailsSentRequest.from_dict(purchase_order_get_emails_sent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


