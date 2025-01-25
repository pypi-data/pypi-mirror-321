# HasStockItemStockLevelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_item_id** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.has_stock_item_stock_level_request import HasStockItemStockLevelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HasStockItemStockLevelRequest from a JSON string
has_stock_item_stock_level_request_instance = HasStockItemStockLevelRequest.from_json(json)
# print the JSON string representation of the object
print(HasStockItemStockLevelRequest.to_json())

# convert the object into a dict
has_stock_item_stock_level_request_dict = has_stock_item_stock_level_request_instance.to_dict()
# create an instance of HasStockItemStockLevelRequest from a dict
has_stock_item_stock_level_request_from_dict = HasStockItemStockLevelRequest.from_dict(has_stock_item_stock_level_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


