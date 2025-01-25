# AddShipmentBoxItemModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipping_plan_id** | **int** |  | [optional] 
**shipment_box_id** | **int** |  | [optional] 
**shipment_id** | **int** |  | [optional] 
**packing_group_id** | **int** |  | [optional] 
**stock_item_id** | **int** |  | [optional] 
**quantity** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.add_shipment_box_item_model import AddShipmentBoxItemModel

# TODO update the JSON string below
json = "{}"
# create an instance of AddShipmentBoxItemModel from a JSON string
add_shipment_box_item_model_instance = AddShipmentBoxItemModel.from_json(json)
# print the JSON string representation of the object
print(AddShipmentBoxItemModel.to_json())

# convert the object into a dict
add_shipment_box_item_model_dict = add_shipment_box_item_model_instance.to_dict()
# create an instance of AddShipmentBoxItemModel from a dict
add_shipment_box_item_model_from_dict = AddShipmentBoxItemModel.from_dict(add_shipment_box_item_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


