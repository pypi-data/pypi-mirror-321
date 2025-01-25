# InventoryParametersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_item_ids** | **List[str]** | List of stock item ids | [optional] 
**selected_regions** | [**List[TupleInt32Int32]**](TupleInt32Int32.md) | A list of row numbers for items selected in the my inventory grid.   For instance if the first entry in the list is 4, 4; the selection was from the fourth row, to the fourth row. | [optional] 
**token** | **str** | An internal token used to identify the list of inventory items within a certain view.  From this, the inventory item ids can be extracted with the selected regions. | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_parameters_request import InventoryParametersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryParametersRequest from a JSON string
inventory_parameters_request_instance = InventoryParametersRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryParametersRequest.to_json())

# convert the object into a dict
inventory_parameters_request_dict = inventory_parameters_request_instance.to_dict()
# create an instance of InventoryParametersRequest from a dict
inventory_parameters_request_from_dict = InventoryParametersRequest.from_dict(inventory_parameters_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


