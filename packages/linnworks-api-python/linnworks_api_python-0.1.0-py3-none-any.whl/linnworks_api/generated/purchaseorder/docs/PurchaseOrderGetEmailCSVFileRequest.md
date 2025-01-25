# PurchaseOrderGetEmailCSVFileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**GetEmailCSVFileRequest**](GetEmailCSVFileRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_get_email_csv_file_request import PurchaseOrderGetEmailCSVFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderGetEmailCSVFileRequest from a JSON string
purchase_order_get_email_csv_file_request_instance = PurchaseOrderGetEmailCSVFileRequest.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderGetEmailCSVFileRequest.to_json())

# convert the object into a dict
purchase_order_get_email_csv_file_request_dict = purchase_order_get_email_csv_file_request_instance.to_dict()
# create an instance of PurchaseOrderGetEmailCSVFileRequest from a dict
purchase_order_get_email_csv_file_request_from_dict = PurchaseOrderGetEmailCSVFileRequest.from_dict(purchase_order_get_email_csv_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


