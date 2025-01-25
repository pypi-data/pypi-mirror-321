# ShipmentBoxItemExtendedModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**shipping_plan_id** | **int** |  | [optional] 
**shipment_id** | **int** |  | [optional] 
**packing_group_id** | **int** |  | [optional] 
**stock_item_int_id** | **int** |  | [optional] 
**stock_item_id** | **str** |  | [optional] 
**seller_sku** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 
**weight** | **float** |  | [optional] 
**length** | **float** |  | [optional] 
**height** | **float** |  | [optional] 
**width** | **float** |  | [optional] 
**quantity_to_ship** | **int** |  | [optional] 
**thumbnail_source** | **str** |  | [optional] 
**type** | [**ShipmentBoxRecordType**](ShipmentBoxRecordType.md) |  | [optional] 
**data_path** | **List[str]** |  | [optional] 
**shipment_box_id** | **int** |  | [optional] 
**shipment_box_item_id** | **int** |  | [optional] 
**shipment_box_name** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.shipment_box_item_extended_model import ShipmentBoxItemExtendedModel

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentBoxItemExtendedModel from a JSON string
shipment_box_item_extended_model_instance = ShipmentBoxItemExtendedModel.from_json(json)
# print the JSON string representation of the object
print(ShipmentBoxItemExtendedModel.to_json())

# convert the object into a dict
shipment_box_item_extended_model_dict = shipment_box_item_extended_model_instance.to_dict()
# create an instance of ShipmentBoxItemExtendedModel from a dict
shipment_box_item_extended_model_from_dict = ShipmentBoxItemExtendedModel.from_dict(shipment_box_item_extended_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


