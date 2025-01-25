# SkuPrepInstructionItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_item_id** | **int** |  | [optional] 
**item_title** | **str** |  | [optional] 
**quantity_to_send** | **int** |  | [optional] 
**label_type** | **str** |  | [optional] 
**seller_sku** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**asin** | **str** |  | [optional] 
**thumbnail_source** | **str** |  | [optional] 
**stock_item_id_guid** | **str** |  | [optional] 
**barcode_instruction** | [**SkuPrepBarcodeInstruction**](SkuPrepBarcodeInstruction.md) |  | [optional] 
**prep_guidance** | [**SkuPrepGuidance**](SkuPrepGuidance.md) |  | [optional] 
**prep_instruction_list** | [**List[AmazonPrepInstructionItem]**](AmazonPrepInstructionItem.md) |  | [optional] 
**fee_amount_per_unit** | **Dict[str, float]** |  | [optional] 
**total_fee_amount** | **Dict[str, float]** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.sku_prep_instruction_item import SkuPrepInstructionItem

# TODO update the JSON string below
json = "{}"
# create an instance of SkuPrepInstructionItem from a JSON string
sku_prep_instruction_item_instance = SkuPrepInstructionItem.from_json(json)
# print the JSON string representation of the object
print(SkuPrepInstructionItem.to_json())

# convert the object into a dict
sku_prep_instruction_item_dict = sku_prep_instruction_item_instance.to_dict()
# create an instance of SkuPrepInstructionItem from a dict
sku_prep_instruction_item_from_dict = SkuPrepInstructionItem.from_dict(sku_prep_instruction_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


