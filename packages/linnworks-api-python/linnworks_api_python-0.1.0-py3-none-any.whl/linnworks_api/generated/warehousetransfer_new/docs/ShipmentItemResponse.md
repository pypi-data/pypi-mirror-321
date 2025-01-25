# ShipmentItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **int** |  | [optional] 
**batches** | [**List[ShipmentItemBatchResponse]**](ShipmentItemBatchResponse.md) |  | [optional] 
**batch_type** | **int** |  | [optional] 
**fba_available** | **int** |  | [optional] 
**fba_stock_level** | **int** |  | [optional] 
**fba_total_stock** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**pack_quantity** | **int** |  | [optional] 
**pack_size** | **int** |  | [optional] 
**quantity_to_ship** | **int** |  | [optional] 
**received_qty** | **int** |  | [optional] 
**asin** | **str** |  | [optional] 
**seller_sku** | **str** |  | [optional] 
**shipment_id** | **int** |  | [optional] 
**shipped_qty** | **int** |  | [optional] 
**sku** | **str** |  | [optional] 
**stock_item_id** | **int** |  | [optional] 
**stock_item_id_guid** | **str** |  | [optional] 
**thumbnail_source** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**prep_instructions** | [**List[AmazonPrepInstructionItem]**](AmazonPrepInstructionItem.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.shipment_item_response import ShipmentItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentItemResponse from a JSON string
shipment_item_response_instance = ShipmentItemResponse.from_json(json)
# print the JSON string representation of the object
print(ShipmentItemResponse.to_json())

# convert the object into a dict
shipment_item_response_dict = shipment_item_response_instance.to_dict()
# create an instance of ShipmentItemResponse from a dict
shipment_item_response_from_dict = ShipmentItemResponse.from_dict(shipment_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


