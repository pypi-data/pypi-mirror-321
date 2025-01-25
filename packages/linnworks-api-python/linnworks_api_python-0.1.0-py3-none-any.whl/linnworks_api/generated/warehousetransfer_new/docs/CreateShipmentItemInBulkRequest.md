# CreateShipmentItemInBulkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ShippingItem]**](ShippingItem.md) |  | 
**shipping_plan_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.create_shipment_item_in_bulk_request import CreateShipmentItemInBulkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateShipmentItemInBulkRequest from a JSON string
create_shipment_item_in_bulk_request_instance = CreateShipmentItemInBulkRequest.from_json(json)
# print the JSON string representation of the object
print(CreateShipmentItemInBulkRequest.to_json())

# convert the object into a dict
create_shipment_item_in_bulk_request_dict = create_shipment_item_in_bulk_request_instance.to_dict()
# create an instance of CreateShipmentItemInBulkRequest from a dict
create_shipment_item_in_bulk_request_from_dict = CreateShipmentItemInBulkRequest.from_dict(create_shipment_item_in_bulk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


