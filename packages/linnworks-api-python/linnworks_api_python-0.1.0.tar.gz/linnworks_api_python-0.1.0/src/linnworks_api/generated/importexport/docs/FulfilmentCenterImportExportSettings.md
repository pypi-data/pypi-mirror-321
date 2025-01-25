# FulfilmentCenterImportExportSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fk_stock_location_id** | **str** |  | [optional] 
**fk_orders_export_id** | **int** |  | [optional] 
**fk_orders_import_id** | **int** |  | [optional] 
**fk_inventory_import_id** | **int** |  | [optional] 
**orders_export_enabled** | **bool** |  | [optional] 
**orders_import_enabled** | **bool** |  | [optional] 
**inventory_import_enabled** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.importexport.models.fulfilment_center_import_export_settings import FulfilmentCenterImportExportSettings

# TODO update the JSON string below
json = "{}"
# create an instance of FulfilmentCenterImportExportSettings from a JSON string
fulfilment_center_import_export_settings_instance = FulfilmentCenterImportExportSettings.from_json(json)
# print the JSON string representation of the object
print(FulfilmentCenterImportExportSettings.to_json())

# convert the object into a dict
fulfilment_center_import_export_settings_dict = fulfilment_center_import_export_settings_instance.to_dict()
# create an instance of FulfilmentCenterImportExportSettings from a dict
fulfilment_center_import_export_settings_from_dict = FulfilmentCenterImportExportSettings.from_dict(fulfilment_center_import_export_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


