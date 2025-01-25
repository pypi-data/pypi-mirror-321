# GetInventoryItemsCompositionByIdsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_item_ids** | **List[str]** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.get_inventory_items_composition_by_ids_request import GetInventoryItemsCompositionByIdsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetInventoryItemsCompositionByIdsRequest from a JSON string
get_inventory_items_composition_by_ids_request_instance = GetInventoryItemsCompositionByIdsRequest.from_json(json)
# print the JSON string representation of the object
print(GetInventoryItemsCompositionByIdsRequest.to_json())

# convert the object into a dict
get_inventory_items_composition_by_ids_request_dict = get_inventory_items_composition_by_ids_request_instance.to_dict()
# create an instance of GetInventoryItemsCompositionByIdsRequest from a dict
get_inventory_items_composition_by_ids_request_from_dict = GetInventoryItemsCompositionByIdsRequest.from_dict(get_inventory_items_composition_by_ids_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


