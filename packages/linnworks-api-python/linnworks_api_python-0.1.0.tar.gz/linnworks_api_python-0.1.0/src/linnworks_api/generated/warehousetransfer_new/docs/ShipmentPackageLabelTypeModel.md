# ShipmentPackageLabelTypeModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amazon_page_type** | **str** |  | [optional] 
**countries** | **List[str]** |  | [optional] 
**carrier_types** | [**List[AmazonShipmentCarrierType]**](AmazonShipmentCarrierType.md) |  | [optional] 
**shipment_carrier** | **str** |  | [optional] 
**paper_size_info** | **str** |  | [optional] 
**is_visible_for_pallet** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.shipment_package_label_type_model import ShipmentPackageLabelTypeModel

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentPackageLabelTypeModel from a JSON string
shipment_package_label_type_model_instance = ShipmentPackageLabelTypeModel.from_json(json)
# print the JSON string representation of the object
print(ShipmentPackageLabelTypeModel.to_json())

# convert the object into a dict
shipment_package_label_type_model_dict = shipment_package_label_type_model_instance.to_dict()
# create an instance of ShipmentPackageLabelTypeModel from a dict
shipment_package_label_type_model_from_dict = ShipmentPackageLabelTypeModel.from_dict(shipment_package_label_type_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


