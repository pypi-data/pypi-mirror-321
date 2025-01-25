# PurchaseItemFound


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_stock_item_id** | **str** |  | [optional] 
**item_number** | **str** |  | [optional] 
**item_title** | **str** |  | [optional] 
**inventory_tracking_type** | **int** |  | [optional] 
**tax_rate** | **float** |  | [optional] 
**purchase_price** | **float** |  | [optional] 
**known_purchase_price** | **float** |  | [optional] 
**supplier_code** | **str** |  | [optional] 
**supplier_barcode** | **str** |  | [optional] 
**fk_supplier_id** | **str** |  | [optional] 
**supplier_min_order_qty** | **int** |  | [optional] 
**supplier_pack_size** | **int** |  | [optional] 
**contains_composites** | **bool** |  | [optional] 
**stock_item_int_id** | **int** |  | [optional] 
**fk_stock_location_id** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.purchase_item_found import PurchaseItemFound

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseItemFound from a JSON string
purchase_item_found_instance = PurchaseItemFound.from_json(json)
# print the JSON string representation of the object
print(PurchaseItemFound.to_json())

# convert the object into a dict
purchase_item_found_dict = purchase_item_found_instance.to_dict()
# create an instance of PurchaseItemFound from a dict
purchase_item_found_from_dict = PurchaseItemFound.from_dict(purchase_item_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


