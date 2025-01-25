# StockItemAuditTrail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audit_type** | **str** |  | [optional] 
**audit_trail_date** | **datetime** |  | [optional] 
**audit_text** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**stock_item_int_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.stock_item_audit_trail import StockItemAuditTrail

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemAuditTrail from a JSON string
stock_item_audit_trail_instance = StockItemAuditTrail.from_json(json)
# print the JSON string representation of the object
print(StockItemAuditTrail.to_json())

# convert the object into a dict
stock_item_audit_trail_dict = stock_item_audit_trail_instance.to_dict()
# create an instance of StockItemAuditTrail from a dict
stock_item_audit_trail_from_dict = StockItemAuditTrail.from_dict(stock_item_audit_trail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


