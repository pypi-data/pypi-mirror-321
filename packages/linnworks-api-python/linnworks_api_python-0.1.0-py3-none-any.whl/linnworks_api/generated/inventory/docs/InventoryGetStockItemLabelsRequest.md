# InventoryGetStockItemLabelsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_regions** | [**List[TupleInt32Int32]**](TupleInt32Int32.md) | Row numbers to retrieve item ids for | [optional] 
**token** | **str** | Search Token | [optional] 
**location** | **str** | Location id | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.inventory_get_stock_item_labels_request import InventoryGetStockItemLabelsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryGetStockItemLabelsRequest from a JSON string
inventory_get_stock_item_labels_request_instance = InventoryGetStockItemLabelsRequest.from_json(json)
# print the JSON string representation of the object
print(InventoryGetStockItemLabelsRequest.to_json())

# convert the object into a dict
inventory_get_stock_item_labels_request_dict = inventory_get_stock_item_labels_request_instance.to_dict()
# create an instance of InventoryGetStockItemLabelsRequest from a dict
inventory_get_stock_item_labels_request_from_dict = InventoryGetStockItemLabelsRequest.from_dict(inventory_get_stock_item_labels_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


