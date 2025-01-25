# GetInventoryItemBatchInformationByIdsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_item_batch_information** | [**List[BatchInformation]**](BatchInformation.md) | A list of stock item batch data | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.get_inventory_item_batch_information_by_ids_response import GetInventoryItemBatchInformationByIdsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetInventoryItemBatchInformationByIdsResponse from a JSON string
get_inventory_item_batch_information_by_ids_response_instance = GetInventoryItemBatchInformationByIdsResponse.from_json(json)
# print the JSON string representation of the object
print(GetInventoryItemBatchInformationByIdsResponse.to_json())

# convert the object into a dict
get_inventory_item_batch_information_by_ids_response_dict = get_inventory_item_batch_information_by_ids_response_instance.to_dict()
# create an instance of GetInventoryItemBatchInformationByIdsResponse from a dict
get_inventory_item_batch_information_by_ids_response_from_dict = GetInventoryItemBatchInformationByIdsResponse.from_dict(get_inventory_item_batch_information_by_ids_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


