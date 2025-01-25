# BulkScrapBatchedItemsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_id** | **str** |  | [optional] 
**scrap_items** | [**List[ScrapItemExtended]**](ScrapItemExtended.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.bulk_scrap_batched_items_request import BulkScrapBatchedItemsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkScrapBatchedItemsRequest from a JSON string
bulk_scrap_batched_items_request_instance = BulkScrapBatchedItemsRequest.from_json(json)
# print the JSON string representation of the object
print(BulkScrapBatchedItemsRequest.to_json())

# convert the object into a dict
bulk_scrap_batched_items_request_dict = bulk_scrap_batched_items_request_instance.to_dict()
# create an instance of BulkScrapBatchedItemsRequest from a dict
bulk_scrap_batched_items_request_from_dict = BulkScrapBatchedItemsRequest.from_dict(bulk_scrap_batched_items_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


