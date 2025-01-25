# UpdateAmazonShipmentItemPackQuantityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_location_id** | **str** |  | 
**pack_quantity** | **int** |  | 
**pack_size** | **int** |  | 
**shipment_id** | **int** |  | 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.update_amazon_shipment_item_pack_quantity_request import UpdateAmazonShipmentItemPackQuantityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAmazonShipmentItemPackQuantityRequest from a JSON string
update_amazon_shipment_item_pack_quantity_request_instance = UpdateAmazonShipmentItemPackQuantityRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAmazonShipmentItemPackQuantityRequest.to_json())

# convert the object into a dict
update_amazon_shipment_item_pack_quantity_request_dict = update_amazon_shipment_item_pack_quantity_request_instance.to_dict()
# create an instance of UpdateAmazonShipmentItemPackQuantityRequest from a dict
update_amazon_shipment_item_pack_quantity_request_from_dict = UpdateAmazonShipmentItemPackQuantityRequest.from_dict(update_amazon_shipment_item_pack_quantity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


