# ShipmentItemBatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_id** | **int** |  | [optional] 
**batch_inventory_id** | **int** |  | [optional] 
**batch_number** | **str** |  | [optional] 
**batch_status** | **str** |  | [optional] 
**available** | **int** |  | [optional] 
**quantity** | **int** |  | [optional] 
**quantity_to_ship** | **int** |  | [optional] 
**shipment_item_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.shipment_item_batch_response import ShipmentItemBatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentItemBatchResponse from a JSON string
shipment_item_batch_response_instance = ShipmentItemBatchResponse.from_json(json)
# print the JSON string representation of the object
print(ShipmentItemBatchResponse.to_json())

# convert the object into a dict
shipment_item_batch_response_dict = shipment_item_batch_response_instance.to_dict()
# create an instance of ShipmentItemBatchResponse from a dict
shipment_item_batch_response_from_dict = ShipmentItemBatchResponse.from_dict(shipment_item_batch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


