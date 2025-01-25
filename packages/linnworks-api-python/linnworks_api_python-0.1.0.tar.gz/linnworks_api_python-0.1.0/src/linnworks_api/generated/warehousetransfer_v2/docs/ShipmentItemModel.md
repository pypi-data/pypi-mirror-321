# ShipmentItemModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_item_id** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**quantity_to_ship** | **int** |  | [optional] 
**received_qty** | **int** |  | [optional] 
**shipment_id** | **int** |  | [optional] 
**shipped_qty** | **int** |  | [optional] 
**seller_sku** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**barcode_instruction_id** | [**SkuPrepBarcodeInstruction**](SkuPrepBarcodeInstruction.md) |  | [optional] 
**prep_guidance_id** | [**SkuPrepGuidance**](SkuPrepGuidance.md) |  | [optional] 
**unit_cost** | **float** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.shipment_item_model import ShipmentItemModel

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentItemModel from a JSON string
shipment_item_model_instance = ShipmentItemModel.from_json(json)
# print the JSON string representation of the object
print(ShipmentItemModel.to_json())

# convert the object into a dict
shipment_item_model_dict = shipment_item_model_instance.to_dict()
# create an instance of ShipmentItemModel from a dict
shipment_item_model_from_dict = ShipmentItemModel.from_dict(shipment_item_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


