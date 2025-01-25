# StockItemBatchAudit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_id** | **int** |  | [optional] [readonly] 
**batch_inventory_id** | **int** |  | [optional] [readonly] 
**quantity_delta** | **int** |  | [optional] [readonly] 
**stock_value_delta** | **float** |  | [optional] [readonly] 
**change_note** | **str** |  | [optional] [readonly] 
**username** | **str** |  | [optional] [readonly] 
**change_date** | **datetime** |  | [optional] [readonly] 
**bin_rack** | **str** |  | [optional] [readonly] 
**batch_number** | **str** |  | [optional] [readonly] 
**location** | **str** |  | [optional] [readonly] 
**fk_job_id** | **int** |  | [optional] [readonly] 
**order_id** | **int** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.inventory.models.stock_item_batch_audit import StockItemBatchAudit

# TODO update the JSON string below
json = "{}"
# create an instance of StockItemBatchAudit from a JSON string
stock_item_batch_audit_instance = StockItemBatchAudit.from_json(json)
# print the JSON string representation of the object
print(StockItemBatchAudit.to_json())

# convert the object into a dict
stock_item_batch_audit_dict = stock_item_batch_audit_instance.to_dict()
# create an instance of StockItemBatchAudit from a dict
stock_item_batch_audit_from_dict = StockItemBatchAudit.from_dict(stock_item_batch_audit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


