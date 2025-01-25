# PagedResultStockItemAuditTrail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[StockItemAuditTrail]**](StockItemAuditTrail.md) |  | [optional] 
**total_items** | **int** |  | [optional] 
**current_page** | **int** |  | [optional] 
**entries_per_page** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.paged_result_stock_item_audit_trail import PagedResultStockItemAuditTrail

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResultStockItemAuditTrail from a JSON string
paged_result_stock_item_audit_trail_instance = PagedResultStockItemAuditTrail.from_json(json)
# print the JSON string representation of the object
print(PagedResultStockItemAuditTrail.to_json())

# convert the object into a dict
paged_result_stock_item_audit_trail_dict = paged_result_stock_item_audit_trail_instance.to_dict()
# create an instance of PagedResultStockItemAuditTrail from a dict
paged_result_stock_item_audit_trail_from_dict = PagedResultStockItemAuditTrail.from_dict(paged_result_stock_item_audit_trail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


