# AddShipmentItemBatchesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batches** | [**List[ItemBatches]**](ItemBatches.md) |  | 
**from_location** | **str** |  | 
**pack_size** | **int** |  | 
**shipment_item_id** | **int** |  | 
**shipping_plan_id** | **int** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.add_shipment_item_batches_request import AddShipmentItemBatchesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddShipmentItemBatchesRequest from a JSON string
add_shipment_item_batches_request_instance = AddShipmentItemBatchesRequest.from_json(json)
# print the JSON string representation of the object
print(AddShipmentItemBatchesRequest.to_json())

# convert the object into a dict
add_shipment_item_batches_request_dict = add_shipment_item_batches_request_instance.to_dict()
# create an instance of AddShipmentItemBatchesRequest from a dict
add_shipment_item_batches_request_from_dict = AddShipmentItemBatchesRequest.from_dict(add_shipment_item_batches_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


