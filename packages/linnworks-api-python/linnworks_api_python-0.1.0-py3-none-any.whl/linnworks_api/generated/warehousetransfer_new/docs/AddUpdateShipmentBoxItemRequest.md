# AddUpdateShipmentBoxItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_id** | **int** |  | [optional] 
**stock_item_int_id** | **int** |  | [optional] 
**shipment_box_id** | **int** |  | [optional] 
**quantity_to_ship** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.add_update_shipment_box_item_request import AddUpdateShipmentBoxItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddUpdateShipmentBoxItemRequest from a JSON string
add_update_shipment_box_item_request_instance = AddUpdateShipmentBoxItemRequest.from_json(json)
# print the JSON string representation of the object
print(AddUpdateShipmentBoxItemRequest.to_json())

# convert the object into a dict
add_update_shipment_box_item_request_dict = add_update_shipment_box_item_request_instance.to_dict()
# create an instance of AddUpdateShipmentBoxItemRequest from a dict
add_update_shipment_box_item_request_from_dict = AddUpdateShipmentBoxItemRequest.from_dict(add_update_shipment_box_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


