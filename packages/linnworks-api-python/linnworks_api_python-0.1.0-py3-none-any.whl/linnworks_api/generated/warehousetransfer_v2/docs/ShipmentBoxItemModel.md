# ShipmentBoxItemModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_box_item_id** | **int** |  | [optional] 
**shipment_id** | **int** |  | [optional] 
**packing_group_id** | **int** |  | [optional] 
**stock_item_id** | **int** |  | [optional] 
**quantity** | **int** |  | [optional] 
**shipment_box_id** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.shipment_box_item_model import ShipmentBoxItemModel

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentBoxItemModel from a JSON string
shipment_box_item_model_instance = ShipmentBoxItemModel.from_json(json)
# print the JSON string representation of the object
print(ShipmentBoxItemModel.to_json())

# convert the object into a dict
shipment_box_item_model_dict = shipment_box_item_model_instance.to_dict()
# create an instance of ShipmentBoxItemModel from a dict
shipment_box_item_model_from_dict = ShipmentBoxItemModel.from_dict(shipment_box_item_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


