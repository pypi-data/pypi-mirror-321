# AddInventoryItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_items** | [**List[StockItemHeader]**](StockItemHeader.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.add_inventory_item_request import AddInventoryItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddInventoryItemRequest from a JSON string
add_inventory_item_request_instance = AddInventoryItemRequest.from_json(json)
# print the JSON string representation of the object
print(AddInventoryItemRequest.to_json())

# convert the object into a dict
add_inventory_item_request_dict = add_inventory_item_request_instance.to_dict()
# create an instance of AddInventoryItemRequest from a dict
add_inventory_item_request_from_dict = AddInventoryItemRequest.from_dict(add_inventory_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


