# UpdateShipmentItemPrepInstructionOwnerModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_item_id** | **int** |  | [optional] 
**prep_instruction_list** | [**List[AmazonPrepInstructionItem]**](AmazonPrepInstructionItem.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.update_shipment_item_prep_instruction_owner_model import UpdateShipmentItemPrepInstructionOwnerModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateShipmentItemPrepInstructionOwnerModel from a JSON string
update_shipment_item_prep_instruction_owner_model_instance = UpdateShipmentItemPrepInstructionOwnerModel.from_json(json)
# print the JSON string representation of the object
print(UpdateShipmentItemPrepInstructionOwnerModel.to_json())

# convert the object into a dict
update_shipment_item_prep_instruction_owner_model_dict = update_shipment_item_prep_instruction_owner_model_instance.to_dict()
# create an instance of UpdateShipmentItemPrepInstructionOwnerModel from a dict
update_shipment_item_prep_instruction_owner_model_from_dict = UpdateShipmentItemPrepInstructionOwnerModel.from_dict(update_shipment_item_prep_instruction_owner_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


