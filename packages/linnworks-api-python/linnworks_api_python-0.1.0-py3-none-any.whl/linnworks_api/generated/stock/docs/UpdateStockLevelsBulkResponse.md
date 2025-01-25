# UpdateStockLevelsBulkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[UpdateStockLevelsBulkResponseItem]**](UpdateStockLevelsBulkResponseItem.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.update_stock_levels_bulk_response import UpdateStockLevelsBulkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStockLevelsBulkResponse from a JSON string
update_stock_levels_bulk_response_instance = UpdateStockLevelsBulkResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateStockLevelsBulkResponse.to_json())

# convert the object into a dict
update_stock_levels_bulk_response_dict = update_stock_levels_bulk_response_instance.to_dict()
# create an instance of UpdateStockLevelsBulkResponse from a dict
update_stock_levels_bulk_response_from_dict = UpdateStockLevelsBulkResponse.from_dict(update_stock_levels_bulk_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


