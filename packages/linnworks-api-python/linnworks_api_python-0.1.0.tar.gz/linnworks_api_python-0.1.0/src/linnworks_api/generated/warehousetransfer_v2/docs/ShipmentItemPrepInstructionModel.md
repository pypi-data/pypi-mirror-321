# ShipmentItemPrepInstructionModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_item_id** | **int** |  | [optional] 
**barcode_instruction** | [**SkuPrepBarcodeInstruction**](SkuPrepBarcodeInstruction.md) |  | [optional] 
**prep_guidance** | [**SkuPrepGuidance**](SkuPrepGuidance.md) |  | [optional] 
**prep_instruction_list** | [**List[AmazonPrepInstructionItem]**](AmazonPrepInstructionItem.md) |  | [optional] 
**fee_amount_per_unit** | **Dict[str, float]** |  | [optional] 
**total_fee_amount** | **Dict[str, float]** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.shipment_item_prep_instruction_model import ShipmentItemPrepInstructionModel

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentItemPrepInstructionModel from a JSON string
shipment_item_prep_instruction_model_instance = ShipmentItemPrepInstructionModel.from_json(json)
# print the JSON string representation of the object
print(ShipmentItemPrepInstructionModel.to_json())

# convert the object into a dict
shipment_item_prep_instruction_model_dict = shipment_item_prep_instruction_model_instance.to_dict()
# create an instance of ShipmentItemPrepInstructionModel from a dict
shipment_item_prep_instruction_model_from_dict = ShipmentItemPrepInstructionModel.from_dict(shipment_item_prep_instruction_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


