# GetInventoryItemsCompositionByIdsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_items_composition_by_ids** | **Dict[str, List[StockItemComposition]]** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.get_inventory_items_composition_by_ids_response import GetInventoryItemsCompositionByIdsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetInventoryItemsCompositionByIdsResponse from a JSON string
get_inventory_items_composition_by_ids_response_instance = GetInventoryItemsCompositionByIdsResponse.from_json(json)
# print the JSON string representation of the object
print(GetInventoryItemsCompositionByIdsResponse.to_json())

# convert the object into a dict
get_inventory_items_composition_by_ids_response_dict = get_inventory_items_composition_by_ids_response_instance.to_dict()
# create an instance of GetInventoryItemsCompositionByIdsResponse from a dict
get_inventory_items_composition_by_ids_response_from_dict = GetInventoryItemsCompositionByIdsResponse.from_dict(get_inventory_items_composition_by_ids_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


