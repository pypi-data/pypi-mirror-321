# CommonPurchaseOrderDeliveredRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_delivery_record_id** | **int** |  | [optional] 
**fk_purchase_item_id** | **str** |  | [optional] 
**fk_stock_location_id** | **str** |  | [optional] 
**unit_cost** | **float** |  | [optional] 
**delivered_quantity** | **int** |  | [optional] 
**created_date_time** | **datetime** |  | [optional] 
**modified_date_time** | **datetime** |  | [optional] 
**fk_batch_inventory_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.common_purchase_order_delivered_record import CommonPurchaseOrderDeliveredRecord

# TODO update the JSON string below
json = "{}"
# create an instance of CommonPurchaseOrderDeliveredRecord from a JSON string
common_purchase_order_delivered_record_instance = CommonPurchaseOrderDeliveredRecord.from_json(json)
# print the JSON string representation of the object
print(CommonPurchaseOrderDeliveredRecord.to_json())

# convert the object into a dict
common_purchase_order_delivered_record_dict = common_purchase_order_delivered_record_instance.to_dict()
# create an instance of CommonPurchaseOrderDeliveredRecord from a dict
common_purchase_order_delivered_record_from_dict = CommonPurchaseOrderDeliveredRecord.from_dict(common_purchase_order_delivered_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


