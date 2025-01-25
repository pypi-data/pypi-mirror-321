# GetInventoryItemBatchInformationRequest

Used to get inventory item batch information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_item_id** | **str** | The item id | [optional] 
**stock_location_id** | **str** | The location to get the batch information from | [optional] 
**available_only** | **bool** | Defines whether we should only return available items | [optional] 
**assignable_only** | **bool** | Only return warehouse locations that can have orders assigned to them for picking | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.get_inventory_item_batch_information_request import GetInventoryItemBatchInformationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetInventoryItemBatchInformationRequest from a JSON string
get_inventory_item_batch_information_request_instance = GetInventoryItemBatchInformationRequest.from_json(json)
# print the JSON string representation of the object
print(GetInventoryItemBatchInformationRequest.to_json())

# convert the object into a dict
get_inventory_item_batch_information_request_dict = get_inventory_item_batch_information_request_instance.to_dict()
# create an instance of GetInventoryItemBatchInformationRequest from a dict
get_inventory_item_batch_information_request_from_dict = GetInventoryItemBatchInformationRequest.from_dict(get_inventory_item_batch_information_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


