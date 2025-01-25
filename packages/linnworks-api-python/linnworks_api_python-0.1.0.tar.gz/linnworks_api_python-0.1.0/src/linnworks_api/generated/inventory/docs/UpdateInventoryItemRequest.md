# UpdateInventoryItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variation_group_name** | **str** |  | [optional] 
**stock_item_id** | **str** | Stock Item Id. If not provided, it will be retrieved using the Item Number | [optional] 
**item_description** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**in_order** | **int** |  | [optional] 
**due** | **int** |  | [optional] 
**minimum_level** | **int** |  | [optional] 
**available** | **int** |  | [optional] [readonly] 
**is_composite_parent** | **bool** |  | [optional] 
**shipped_separately** | **bool** |  | [optional] 
**item_number** | **str** |  | [optional] 
**item_title** | **str** |  | [optional] 
**barcode_number** | **str** |  | [optional] 
**meta_data** | **str** |  | [optional] 
**is_variation_parent** | **bool** |  | [optional] 
**is_batched_stock_type** | **bool** |  | [optional] [readonly] 
**purchase_price** | **float** |  | [optional] 
**retail_price** | **float** |  | [optional] 
**tax_rate** | **float** |  | [optional] 
**postal_service_id** | **str** |  | [optional] 
**postal_service_name** | **str** |  | [optional] 
**category_id** | **str** |  | [optional] 
**category_name** | **str** |  | [optional] 
**package_group_id** | **str** |  | [optional] 
**package_group_name** | **str** |  | [optional] 
**height** | **float** |  | [optional] 
**width** | **float** |  | [optional] 
**depth** | **float** |  | [optional] 
**weight** | **float** |  | [optional] 
**creation_date** | **datetime** |  | [optional] 
**inventory_tracking_type** | **int** |  | [optional] 
**batch_number_scan_required** | **bool** |  | [optional] 
**serial_number_scan_required** | **bool** |  | [optional] 
**stock_item_int_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.update_inventory_item_request import UpdateInventoryItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInventoryItemRequest from a JSON string
update_inventory_item_request_instance = UpdateInventoryItemRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateInventoryItemRequest.to_json())

# convert the object into a dict
update_inventory_item_request_dict = update_inventory_item_request_instance.to_dict()
# create an instance of UpdateInventoryItemRequest from a dict
update_inventory_item_request_from_dict = UpdateInventoryItemRequest.from_dict(update_inventory_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


