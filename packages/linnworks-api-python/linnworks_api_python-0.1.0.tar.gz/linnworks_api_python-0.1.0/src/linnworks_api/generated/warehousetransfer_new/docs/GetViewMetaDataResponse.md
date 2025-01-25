# GetViewMetaDataResponse

This model contains metadata which used by fba and warehouse transfers views

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**packing_types** | [**List[Int32StringKeyValuePair]**](Int32StringKeyValuePair.md) |  | [optional] 
**shipment_statuses** | [**List[Int32StringKeyValuePair]**](Int32StringKeyValuePair.md) |  | [optional] 
**shipping_plan_statuses** | [**List[Int32StringKeyValuePair]**](Int32StringKeyValuePair.md) |  | [optional] 
**prep_owners** | [**List[Int32StringKeyValuePair]**](Int32StringKeyValuePair.md) |  | [optional] 
**who_prepares** | [**List[Int32StringKeyValuePair]**](Int32StringKeyValuePair.md) |  | [optional] 
**import_meta_fields** | [**ShipmentItemsImportMetaFields**](ShipmentItemsImportMetaFields.md) |  | [optional] 
**amazon_shipment_types** | [**List[ShipmentTypeModel]**](ShipmentTypeModel.md) |  | [optional] 
**amazon_shipment_carriers** | [**List[ShipmentCarrierModel]**](ShipmentCarrierModel.md) |  | [optional] 
**amazon_shipment_seller_freights** | [**List[ShipmentSellerFreightModel]**](ShipmentSellerFreightModel.md) |  | [optional] 
**amazon_shipment_package_label_types** | [**List[ShipmentPackageLabelTypeModel]**](ShipmentPackageLabelTypeModel.md) |  | [optional] 
**amazon_partnered_carrier_supported_countries** | **List[str]** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.get_view_meta_data_response import GetViewMetaDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetViewMetaDataResponse from a JSON string
get_view_meta_data_response_instance = GetViewMetaDataResponse.from_json(json)
# print the JSON string representation of the object
print(GetViewMetaDataResponse.to_json())

# convert the object into a dict
get_view_meta_data_response_dict = get_view_meta_data_response_instance.to_dict()
# create an instance of GetViewMetaDataResponse from a dict
get_view_meta_data_response_from_dict = GetViewMetaDataResponse.from_dict(get_view_meta_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


