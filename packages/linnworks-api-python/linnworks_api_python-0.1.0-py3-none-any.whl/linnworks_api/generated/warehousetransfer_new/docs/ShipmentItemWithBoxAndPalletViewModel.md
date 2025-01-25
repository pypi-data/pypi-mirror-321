# ShipmentItemWithBoxAndPalletViewModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | shipmentId + palletId + boxId + stockItemId&lt;br&gt;we need this id in UI for ngrx store | [optional] [readonly] 
**name** | **str** |  | [optional] 
**shipment_item_id** | **int** |  | [optional] 
**shipment_id** | **int** |  | [optional] 
**shipment_pallet_id** | **int** |  | [optional] 
**shipment_box_id** | **int** |  | [optional] 
**shipment_box_item_id** | **int** |  | [optional] 
**seller_sku** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**stock_item_int_id** | **int** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**weight** | **float** |  | [optional] 
**depth** | **float** |  | [optional] 
**height** | **float** |  | [optional] 
**width** | **float** |  | [optional] 
**quantity_to_ship** | **int** |  | [optional] 
**thumbnail_source** | **str** |  | [optional] 
**batch_bin_racks** | **str** |  | [optional] 
**type** | [**ShipmentBoxRecordType**](ShipmentBoxRecordType.md) |  | [optional] 
**pallet_box_hierarchy** | **List[str]** |  | [optional] 
**pack_size** | **int** |  | [optional] 
**tracking_number** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.shipment_item_with_box_and_pallet_view_model import ShipmentItemWithBoxAndPalletViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentItemWithBoxAndPalletViewModel from a JSON string
shipment_item_with_box_and_pallet_view_model_instance = ShipmentItemWithBoxAndPalletViewModel.from_json(json)
# print the JSON string representation of the object
print(ShipmentItemWithBoxAndPalletViewModel.to_json())

# convert the object into a dict
shipment_item_with_box_and_pallet_view_model_dict = shipment_item_with_box_and_pallet_view_model_instance.to_dict()
# create an instance of ShipmentItemWithBoxAndPalletViewModel from a dict
shipment_item_with_box_and_pallet_view_model_from_dict = ShipmentItemWithBoxAndPalletViewModel.from_dict(shipment_item_with_box_and_pallet_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


