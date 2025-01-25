# ShipmentCardModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | **int** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**update_date** | **datetime** |  | [optional] 
**from_location** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**amazon_shipment_id** | **str** |  | [optional] 
**shipping_plan_id** | **int** |  | [optional] 
**packing_type** | **int** |  | [optional] 
**plan_id** | **str** |  | [optional] 
**shipment_items_count** | **int** |  | [optional] 
**shipment_received** | **int** |  | [optional] 
**shipment_shipped** | **int** |  | [optional] 
**status** | [**ShipmentStatus**](ShipmentStatus.md) |  | [optional] 
**to_location** | **str** |  | [optional] 
**type** | [**TransferCard**](TransferCard.md) |  | [optional] 
**items** | [**List[StockItemSearchModel]**](StockItemSearchModel.md) |  | [optional] 
**shipments** | [**List[ShipmentSearchModel]**](ShipmentSearchModel.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.shipment_card_model import ShipmentCardModel

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentCardModel from a JSON string
shipment_card_model_instance = ShipmentCardModel.from_json(json)
# print the JSON string representation of the object
print(ShipmentCardModel.to_json())

# convert the object into a dict
shipment_card_model_dict = shipment_card_model_instance.to_dict()
# create an instance of ShipmentCardModel from a dict
shipment_card_model_from_dict = ShipmentCardModel.from_dict(shipment_card_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


