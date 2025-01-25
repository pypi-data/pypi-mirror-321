# UpdateShipmentItemPrepInstructionRequestItem


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
from linnworks_api.generated.warehousetransfer_v2.models.update_shipment_item_prep_instruction_request_item import UpdateShipmentItemPrepInstructionRequestItem

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateShipmentItemPrepInstructionRequestItem from a JSON string
update_shipment_item_prep_instruction_request_item_instance = UpdateShipmentItemPrepInstructionRequestItem.from_json(json)
# print the JSON string representation of the object
print(UpdateShipmentItemPrepInstructionRequestItem.to_json())

# convert the object into a dict
update_shipment_item_prep_instruction_request_item_dict = update_shipment_item_prep_instruction_request_item_instance.to_dict()
# create an instance of UpdateShipmentItemPrepInstructionRequestItem from a dict
update_shipment_item_prep_instruction_request_item_from_dict = UpdateShipmentItemPrepInstructionRequestItem.from_dict(update_shipment_item_prep_instruction_request_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


