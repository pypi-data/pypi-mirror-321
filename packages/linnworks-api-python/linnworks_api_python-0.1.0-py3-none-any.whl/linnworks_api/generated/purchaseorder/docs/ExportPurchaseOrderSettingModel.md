# ExportPurchaseOrderSettingModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_mappings** | [**List[ColumnPurchaseOrderMappingModel]**](ColumnPurchaseOrderMappingModel.md) |  | [optional] 
**delimiter** | **str** |  | [optional] 
**encoding** | **str** |  | [optional] 
**purchase_id** | **str** |  | [optional] 
**string_delimiter** | **str** |  | [optional] 
**file_name** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.export_purchase_order_setting_model import ExportPurchaseOrderSettingModel

# TODO update the JSON string below
json = "{}"
# create an instance of ExportPurchaseOrderSettingModel from a JSON string
export_purchase_order_setting_model_instance = ExportPurchaseOrderSettingModel.from_json(json)
# print the JSON string representation of the object
print(ExportPurchaseOrderSettingModel.to_json())

# convert the object into a dict
export_purchase_order_setting_model_dict = export_purchase_order_setting_model_instance.to_dict()
# create an instance of ExportPurchaseOrderSettingModel from a dict
export_purchase_order_setting_model_from_dict = ExportPurchaseOrderSettingModel.from_dict(export_purchase_order_setting_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


