# PurchaseOrderExportPurchaseOrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**ExportPurchaseOrderSettingModel**](ExportPurchaseOrderSettingModel.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_export_purchase_order_request import PurchaseOrderExportPurchaseOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderExportPurchaseOrderRequest from a JSON string
purchase_order_export_purchase_order_request_instance = PurchaseOrderExportPurchaseOrderRequest.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderExportPurchaseOrderRequest.to_json())

# convert the object into a dict
purchase_order_export_purchase_order_request_dict = purchase_order_export_purchase_order_request_instance.to_dict()
# create an instance of PurchaseOrderExportPurchaseOrderRequest from a dict
purchase_order_export_purchase_order_request_from_dict = PurchaseOrderExportPurchaseOrderRequest.from_dict(purchase_order_export_purchase_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


