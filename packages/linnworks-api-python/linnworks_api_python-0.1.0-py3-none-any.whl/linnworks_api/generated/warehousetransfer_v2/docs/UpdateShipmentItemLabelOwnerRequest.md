# UpdateShipmentItemLabelOwnerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipping_plan_id** | **int** |  | [optional] 
**shipment_item_id** | **int** |  | [optional] 
**label_owner** | [**LabelOwner**](LabelOwner.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.update_shipment_item_label_owner_request import UpdateShipmentItemLabelOwnerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateShipmentItemLabelOwnerRequest from a JSON string
update_shipment_item_label_owner_request_instance = UpdateShipmentItemLabelOwnerRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateShipmentItemLabelOwnerRequest.to_json())

# convert the object into a dict
update_shipment_item_label_owner_request_dict = update_shipment_item_label_owner_request_instance.to_dict()
# create an instance of UpdateShipmentItemLabelOwnerRequest from a dict
update_shipment_item_label_owner_request_from_dict = UpdateShipmentItemLabelOwnerRequest.from_dict(update_shipment_item_label_owner_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


