# UpdateStockLevelsBulkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[UpdateStockLevelsBulkRequestItem]**](UpdateStockLevelsBulkRequestItem.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.update_stock_levels_bulk_request import UpdateStockLevelsBulkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStockLevelsBulkRequest from a JSON string
update_stock_levels_bulk_request_instance = UpdateStockLevelsBulkRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateStockLevelsBulkRequest.to_json())

# convert the object into a dict
update_stock_levels_bulk_request_dict = update_stock_levels_bulk_request_instance.to_dict()
# create an instance of UpdateStockLevelsBulkRequest from a dict
update_stock_levels_bulk_request_from_dict = UpdateStockLevelsBulkRequest.from_dict(update_stock_levels_bulk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


