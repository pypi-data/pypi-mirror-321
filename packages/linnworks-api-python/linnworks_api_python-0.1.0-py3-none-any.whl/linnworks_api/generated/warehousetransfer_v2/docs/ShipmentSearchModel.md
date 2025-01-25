# ShipmentSearchModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amazon_shipment_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.shipment_search_model import ShipmentSearchModel

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentSearchModel from a JSON string
shipment_search_model_instance = ShipmentSearchModel.from_json(json)
# print the JSON string representation of the object
print(ShipmentSearchModel.to_json())

# convert the object into a dict
shipment_search_model_dict = shipment_search_model_instance.to_dict()
# create an instance of ShipmentSearchModel from a dict
shipment_search_model_from_dict = ShipmentSearchModel.from_dict(shipment_search_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


