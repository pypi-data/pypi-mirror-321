# GetShipmentBoxItemsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**box_items** | [**List[ShipmentBoxItemExtendedModel]**](ShipmentBoxItemExtendedModel.md) |  | [optional] 
**weight_unit** | [**UnitOfWeight**](UnitOfWeight.md) |  | [optional] 
**dimension_unit** | [**UnitOfMeasurement**](UnitOfMeasurement.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.get_shipment_box_items_response import GetShipmentBoxItemsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetShipmentBoxItemsResponse from a JSON string
get_shipment_box_items_response_instance = GetShipmentBoxItemsResponse.from_json(json)
# print the JSON string representation of the object
print(GetShipmentBoxItemsResponse.to_json())

# convert the object into a dict
get_shipment_box_items_response_dict = get_shipment_box_items_response_instance.to_dict()
# create an instance of GetShipmentBoxItemsResponse from a dict
get_shipment_box_items_response_from_dict = GetShipmentBoxItemsResponse.from_dict(get_shipment_box_items_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


