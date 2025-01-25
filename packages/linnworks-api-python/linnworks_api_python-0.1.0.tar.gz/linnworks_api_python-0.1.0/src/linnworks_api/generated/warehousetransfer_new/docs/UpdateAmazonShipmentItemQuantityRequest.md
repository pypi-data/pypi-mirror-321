# UpdateAmazonShipmentItemQuantityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_location_id** | **str** |  | 
**quantity_to_ship** | **int** |  | 
**shipment_id** | **int** |  | 
**stock_item_int_id** | **int** |  | 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.update_amazon_shipment_item_quantity_request import UpdateAmazonShipmentItemQuantityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAmazonShipmentItemQuantityRequest from a JSON string
update_amazon_shipment_item_quantity_request_instance = UpdateAmazonShipmentItemQuantityRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAmazonShipmentItemQuantityRequest.to_json())

# convert the object into a dict
update_amazon_shipment_item_quantity_request_dict = update_amazon_shipment_item_quantity_request_instance.to_dict()
# create an instance of UpdateAmazonShipmentItemQuantityRequest from a dict
update_amazon_shipment_item_quantity_request_from_dict = UpdateAmazonShipmentItemQuantityRequest.from_dict(update_amazon_shipment_item_quantity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


