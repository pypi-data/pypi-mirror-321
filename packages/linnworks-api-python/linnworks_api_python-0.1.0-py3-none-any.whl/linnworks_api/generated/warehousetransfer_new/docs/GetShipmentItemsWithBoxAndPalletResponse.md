# GetShipmentItemsWithBoxAndPalletResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ShipmentItemWithBoxAndPalletViewModel]**](ShipmentItemWithBoxAndPalletViewModel.md) |  | [optional] 
**weight_unit** | [**ShipmentWeightUnit**](ShipmentWeightUnit.md) |  | [optional] 
**dimension_unit** | [**ShipmentDimensionUnit**](ShipmentDimensionUnit.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.get_shipment_items_with_box_and_pallet_response import GetShipmentItemsWithBoxAndPalletResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetShipmentItemsWithBoxAndPalletResponse from a JSON string
get_shipment_items_with_box_and_pallet_response_instance = GetShipmentItemsWithBoxAndPalletResponse.from_json(json)
# print the JSON string representation of the object
print(GetShipmentItemsWithBoxAndPalletResponse.to_json())

# convert the object into a dict
get_shipment_items_with_box_and_pallet_response_dict = get_shipment_items_with_box_and_pallet_response_instance.to_dict()
# create an instance of GetShipmentItemsWithBoxAndPalletResponse from a dict
get_shipment_items_with_box_and_pallet_response_from_dict = GetShipmentItemsWithBoxAndPalletResponse.from_dict(get_shipment_items_with_box_and_pallet_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


