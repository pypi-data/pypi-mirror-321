# UpdateShipmentItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition_id** | **int** |  | [optional] 
**stock_item_id** | **int** |  | 
**pack_quantity** | **int** |  | [optional] 
**pack_size** | **int** |  | [optional] 
**quantity_to_ship** | **int** |  | [optional] 
**received_qty** | **int** |  | [optional] 
**shipment_id** | **int** |  | 
**shipped_qty** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.update_shipment_item_request import UpdateShipmentItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateShipmentItemRequest from a JSON string
update_shipment_item_request_instance = UpdateShipmentItemRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateShipmentItemRequest.to_json())

# convert the object into a dict
update_shipment_item_request_dict = update_shipment_item_request_instance.to_dict()
# create an instance of UpdateShipmentItemRequest from a dict
update_shipment_item_request_from_dict = UpdateShipmentItemRequest.from_dict(update_shipment_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


