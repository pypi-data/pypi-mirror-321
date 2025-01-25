# DeleteShipmentItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipping_plan_id** | **int** |  | 
**shipment_item_ids** | **List[int]** |  | 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.delete_shipment_item_request import DeleteShipmentItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteShipmentItemRequest from a JSON string
delete_shipment_item_request_instance = DeleteShipmentItemRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteShipmentItemRequest.to_json())

# convert the object into a dict
delete_shipment_item_request_dict = delete_shipment_item_request_instance.to_dict()
# create an instance of DeleteShipmentItemRequest from a dict
delete_shipment_item_request_from_dict = DeleteShipmentItemRequest.from_dict(delete_shipment_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


