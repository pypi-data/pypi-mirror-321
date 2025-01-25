# GetStockItemBatchesByLocationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_item_id** | **str** |  | [optional] 
**location_id** | **str** |  | [optional] 
**only_available** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.get_stock_item_batches_by_location_request import GetStockItemBatchesByLocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetStockItemBatchesByLocationRequest from a JSON string
get_stock_item_batches_by_location_request_instance = GetStockItemBatchesByLocationRequest.from_json(json)
# print the JSON string representation of the object
print(GetStockItemBatchesByLocationRequest.to_json())

# convert the object into a dict
get_stock_item_batches_by_location_request_dict = get_stock_item_batches_by_location_request_instance.to_dict()
# create an instance of GetStockItemBatchesByLocationRequest from a dict
get_stock_item_batches_by_location_request_from_dict = GetStockItemBatchesByLocationRequest.from_dict(get_stock_item_batches_by_location_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


