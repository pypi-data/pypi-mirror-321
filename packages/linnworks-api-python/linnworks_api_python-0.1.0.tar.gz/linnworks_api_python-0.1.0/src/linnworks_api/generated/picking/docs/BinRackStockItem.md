# BinRackStockItem

Bin Rack

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bin_rack_id** | **int** | Unique id for the binrack | [optional] 
**standard_type** | **int** | Bin Rack type name | [optional] 
**batch_id** | **int** | Batch id | [optional] 
**batch_inventory_id** | **int** | Batch inventory id | [optional] 
**priority_sequence** | **int** | Consume priority sequence | [optional] 
**batch_status** | **str** | Batch status, \&quot;Available\&quot;, \&quot;Restricted\&quot;, \&quot;Damaged\&quot;, \&quot;Expired\&quot; | [optional] 
**bin_rack** | **str** | BinRack name | [optional] 
**current_full_percentage** | **float** | Maximum volumetric capacity of the location WxDxH &#x3D; volumetric | [optional] 
**quantity** | **int** | Quantity available in the location | [optional] 
**in_transit** | **int** | Quantity of items currently in transit | [optional] 
**picked_quantity** | **int** | Indicate how many units are now allocated in open orders | [optional] 
**inventory_tracking_type** | **int** | 0 - None, 1 - Order by sell by date, 2 - Ordered by priority sequence | [optional] 
**stock_item_id** | **str** | Product ID | [optional] 
**batch_number** | **str** | Batch number | [optional] 
**expires_on** | **datetime** | Batch expiry date | [optional] 
**sell_by** | **datetime** | Batch sell by date | [optional] 
**binrack_type_name** | **str** |  | [optional] 
**location_id** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.picking.models.bin_rack_stock_item import BinRackStockItem

# TODO update the JSON string below
json = "{}"
# create an instance of BinRackStockItem from a JSON string
bin_rack_stock_item_instance = BinRackStockItem.from_json(json)
# print the JSON string representation of the object
print(BinRackStockItem.to_json())

# convert the object into a dict
bin_rack_stock_item_dict = bin_rack_stock_item_instance.to_dict()
# create an instance of BinRackStockItem from a dict
bin_rack_stock_item_from_dict = BinRackStockItem.from_dict(bin_rack_stock_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


