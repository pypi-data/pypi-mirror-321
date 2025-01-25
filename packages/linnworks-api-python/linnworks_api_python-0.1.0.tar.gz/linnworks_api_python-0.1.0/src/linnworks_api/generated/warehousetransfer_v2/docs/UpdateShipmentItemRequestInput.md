# UpdateShipmentItemRequestInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stock_item_id** | **int** |  | 
**quantity_to_ship** | **int** |  | 
**received_qty** | **int** |  | [optional] 
**shipment_id** | **int** |  | 
**shipped_qty** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.update_shipment_item_request_input import UpdateShipmentItemRequestInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateShipmentItemRequestInput from a JSON string
update_shipment_item_request_input_instance = UpdateShipmentItemRequestInput.from_json(json)
# print the JSON string representation of the object
print(UpdateShipmentItemRequestInput.to_json())

# convert the object into a dict
update_shipment_item_request_input_dict = update_shipment_item_request_input_instance.to_dict()
# create an instance of UpdateShipmentItemRequestInput from a dict
update_shipment_item_request_input_from_dict = UpdateShipmentItemRequestInput.from_dict(update_shipment_item_request_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


