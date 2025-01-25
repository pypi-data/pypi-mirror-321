# EBayItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_number** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**mapped_by** | **str** |  | [optional] 
**relist_pending** | **bool** |  | [optional] 
**quantity** | **int** |  | [optional] 
**is_suggested_to_link** | **bool** |  | [optional] 
**is_linked** | **bool** |  | [optional] 
**channel_sku_row_id** | **str** |  | [optional] 
**linked_item_id** | **str** |  | [optional] 
**max_listed_quantity** | **int** |  | [optional] 
**end_when_stock** | **int** |  | [optional] 
**stock_percentage** | **float** |  | [optional] 
**linked_item_sku** | **str** |  | [optional] 
**linked_item_title** | **str** |  | [optional] 
**ignore_sync** | **bool** |  | [optional] 
**channel_reference_id** | **str** |  | [optional] [readonly] 
**stricken_off** | **bool** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**end_time** | **datetime** |  | [optional] 
**strike_off_date** | **datetime** |  | [optional] 
**strike_reason** | **str** |  | [optional] 
**linked_with** | **str** |  | [optional] 
**is_variation** | **bool** |  | [optional] 
**fixed_price** | **bool** |  | [optional] 
**reslisted_from** | **str** |  | [optional] 
**list_id** | **str** |  | [optional] 
**listing_price** | **float** |  | [optional] 
**variation_items** | [**List[EBayItem]**](EBayItem.md) |  | [optional] 
**is_gtc** | **bool** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**is_match_by_title** | **bool** |  | [optional] 
**total_rows** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.e_bay_item import EBayItem

# TODO update the JSON string below
json = "{}"
# create an instance of EBayItem from a JSON string
e_bay_item_instance = EBayItem.from_json(json)
# print the JSON string representation of the object
print(EBayItem.to_json())

# convert the object into a dict
e_bay_item_dict = e_bay_item_instance.to_dict()
# create an instance of EBayItem from a dict
e_bay_item_from_dict = EBayItem.from_dict(e_bay_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


