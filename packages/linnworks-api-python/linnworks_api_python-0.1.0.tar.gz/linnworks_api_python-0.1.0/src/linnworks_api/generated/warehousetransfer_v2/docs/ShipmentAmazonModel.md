# ShipmentAmazonModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**placement_option_id** | **str** |  | [optional] 
**shipment_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**shipping_items** | [**List[ItemModel]**](ItemModel.md) |  | [optional] 
**warehouse_id** | **str** |  | [optional] 
**warehouse_address** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.shipment_amazon_model import ShipmentAmazonModel

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentAmazonModel from a JSON string
shipment_amazon_model_instance = ShipmentAmazonModel.from_json(json)
# print the JSON string representation of the object
print(ShipmentAmazonModel.to_json())

# convert the object into a dict
shipment_amazon_model_dict = shipment_amazon_model_instance.to_dict()
# create an instance of ShipmentAmazonModel from a dict
shipment_amazon_model_from_dict = ShipmentAmazonModel.from_dict(shipment_amazon_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


