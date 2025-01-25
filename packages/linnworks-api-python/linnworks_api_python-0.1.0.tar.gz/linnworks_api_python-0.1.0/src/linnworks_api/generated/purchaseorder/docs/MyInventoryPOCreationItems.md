# MyInventoryPOCreationItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_new** | **bool** |  | [optional] 
**purchase_order_id** | **str** |  | [optional] 
**open_order_items_bound** | **List[str]** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**supplier_id** | **str** |  | [optional] 
**supplier_name** | **str** |  | [optional] 
**oustanding_po_quantity** | **int** |  | [optional] 
**suggested_reorder_amount** | **int** |  | [optional] 
**quantity_in_draft_pos** | **int** |  | [optional] 
**item_title** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**supplier_assigned** | **bool** |  | [optional] 
**calculation_method** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**can_be_ordered** | **bool** |  | [optional] 
**error_code** | **str** |  | [optional] 
**supplier_pack_size** | **int** |  | [optional] 
**minimum_order_quantity** | **int** |  | [optional] 
**requested_supplier_id** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.my_inventory_po_creation_items import MyInventoryPOCreationItems

# TODO update the JSON string below
json = "{}"
# create an instance of MyInventoryPOCreationItems from a JSON string
my_inventory_po_creation_items_instance = MyInventoryPOCreationItems.from_json(json)
# print the JSON string representation of the object
print(MyInventoryPOCreationItems.to_json())

# convert the object into a dict
my_inventory_po_creation_items_dict = my_inventory_po_creation_items_instance.to_dict()
# create an instance of MyInventoryPOCreationItems from a dict
my_inventory_po_creation_items_from_dict = MyInventoryPOCreationItems.from_dict(my_inventory_po_creation_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


