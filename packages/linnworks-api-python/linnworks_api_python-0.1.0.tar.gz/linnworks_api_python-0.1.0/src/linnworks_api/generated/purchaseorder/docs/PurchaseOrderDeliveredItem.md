# PurchaseOrderDeliveredItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_purchase_item_id** | **str** |  | [optional] 
**quantity_delivered** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_order_delivered_item import PurchaseOrderDeliveredItem

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderDeliveredItem from a JSON string
purchase_order_delivered_item_instance = PurchaseOrderDeliveredItem.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderDeliveredItem.to_json())

# convert the object into a dict
purchase_order_delivered_item_dict = purchase_order_delivered_item_instance.to_dict()
# create an instance of PurchaseOrderDeliveredItem from a dict
purchase_order_delivered_item_from_dict = PurchaseOrderDeliveredItem.from_dict(purchase_order_delivered_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


