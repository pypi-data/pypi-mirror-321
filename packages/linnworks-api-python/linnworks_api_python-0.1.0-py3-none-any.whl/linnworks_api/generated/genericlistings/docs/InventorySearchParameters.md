# InventorySearchParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_regions** | [**List[TupleInt32Int32]**](TupleInt32Int32.md) |  | [optional] 
**token** | **str** |  | [optional] 
**inventory_item_ids** | **List[str]** |  | [optional] 
**channel_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.genericlistings.models.inventory_search_parameters import InventorySearchParameters

# TODO update the JSON string below
json = "{}"
# create an instance of InventorySearchParameters from a JSON string
inventory_search_parameters_instance = InventorySearchParameters.from_json(json)
# print the JSON string representation of the object
print(InventorySearchParameters.to_json())

# convert the object into a dict
inventory_search_parameters_dict = inventory_search_parameters_instance.to_dict()
# create an instance of InventorySearchParameters from a dict
inventory_search_parameters_from_dict = InventorySearchParameters.from_dict(inventory_search_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


