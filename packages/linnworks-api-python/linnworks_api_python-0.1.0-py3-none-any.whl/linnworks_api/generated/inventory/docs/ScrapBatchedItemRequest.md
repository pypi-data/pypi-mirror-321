# ScrapBatchedItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scrap_item** | [**ScrapItem**](ScrapItem.md) |  | [optional] 
**location_id** | **str** |  | [optional] 
**batch_inventory_id** | **int** |  | [optional] 
**ignore_consumption** | **bool** | Consumption should not be recorded for this scrap request | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.scrap_batched_item_request import ScrapBatchedItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ScrapBatchedItemRequest from a JSON string
scrap_batched_item_request_instance = ScrapBatchedItemRequest.from_json(json)
# print the JSON string representation of the object
print(ScrapBatchedItemRequest.to_json())

# convert the object into a dict
scrap_batched_item_request_dict = scrap_batched_item_request_instance.to_dict()
# create an instance of ScrapBatchedItemRequest from a dict
scrap_batched_item_request_from_dict = ScrapBatchedItemRequest.from_dict(scrap_batched_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


