# UpdateShipmentBoxItemModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_box_item_id** | **int** |  | [optional] 
**quantity** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.update_shipment_box_item_model import UpdateShipmentBoxItemModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateShipmentBoxItemModel from a JSON string
update_shipment_box_item_model_instance = UpdateShipmentBoxItemModel.from_json(json)
# print the JSON string representation of the object
print(UpdateShipmentBoxItemModel.to_json())

# convert the object into a dict
update_shipment_box_item_model_dict = update_shipment_box_item_model_instance.to_dict()
# create an instance of UpdateShipmentBoxItemModel from a dict
update_shipment_box_item_model_from_dict = UpdateShipmentBoxItemModel.from_dict(update_shipment_box_item_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


