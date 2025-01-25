# GetInventoryItemBatchInformationByIdsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_item_ids** | **List[str]** | A list of stock item ids | [optional] 
**stock_location_id** | **str** | The location to get the batch information from | [optional] 
**available_only** | **bool** | Defines whether we should only return available items | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.get_inventory_item_batch_information_by_ids_request import GetInventoryItemBatchInformationByIdsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetInventoryItemBatchInformationByIdsRequest from a JSON string
get_inventory_item_batch_information_by_ids_request_instance = GetInventoryItemBatchInformationByIdsRequest.from_json(json)
# print the JSON string representation of the object
print(GetInventoryItemBatchInformationByIdsRequest.to_json())

# convert the object into a dict
get_inventory_item_batch_information_by_ids_request_dict = get_inventory_item_batch_information_by_ids_request_instance.to_dict()
# create an instance of GetInventoryItemBatchInformationByIdsRequest from a dict
get_inventory_item_batch_information_by_ids_request_from_dict = GetInventoryItemBatchInformationByIdsRequest.from_dict(get_inventory_item_batch_information_by_ids_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


