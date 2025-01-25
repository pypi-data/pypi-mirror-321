# UpdateShipmentItemPrepInstructionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[UpdateShipmentItemPrepInstructionRequestItem]**](UpdateShipmentItemPrepInstructionRequestItem.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.update_shipment_item_prep_instruction_request import UpdateShipmentItemPrepInstructionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateShipmentItemPrepInstructionRequest from a JSON string
update_shipment_item_prep_instruction_request_instance = UpdateShipmentItemPrepInstructionRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateShipmentItemPrepInstructionRequest.to_json())

# convert the object into a dict
update_shipment_item_prep_instruction_request_dict = update_shipment_item_prep_instruction_request_instance.to_dict()
# create an instance of UpdateShipmentItemPrepInstructionRequest from a dict
update_shipment_item_prep_instruction_request_from_dict = UpdateShipmentItemPrepInstructionRequest.from_dict(update_shipment_item_prep_instruction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


