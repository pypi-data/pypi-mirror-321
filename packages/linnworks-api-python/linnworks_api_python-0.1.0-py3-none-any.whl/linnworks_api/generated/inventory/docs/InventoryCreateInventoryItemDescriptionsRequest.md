# InventoryCreateInventoryItemDescriptionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inventory_item_descriptions** | [**List[StockItemDescription]**](StockItemDescription.md) | list of stockitem Descriptions | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_create_inventory_item_descriptions_request import InventoryCreateInventoryItemDescriptionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryCreateInventoryItemDescriptionsRequest from a JSON string
inventory_create_inventory_item_descriptions_request_instance = InventoryCreateInventoryItemDescriptionsRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryCreateInventoryItemDescriptionsRequest.to_json())

# convert the object into a dict
inventory_create_inventory_item_descriptions_request_dict = inventory_create_inventory_item_descriptions_request_instance.to_dict()
# create an instance of InventoryCreateInventoryItemDescriptionsRequest from a dict
inventory_create_inventory_item_descriptions_request_from_dict = InventoryCreateInventoryItemDescriptionsRequest.from_dict(inventory_create_inventory_item_descriptions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


