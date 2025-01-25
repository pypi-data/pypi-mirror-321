# ColumnPurchaseOrderMappingModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csv_field** | **str** |  | [optional] 
**index** | **int** |  | [optional] 
**linnworks_field_type** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.column_purchase_order_mapping_model import ColumnPurchaseOrderMappingModel

# TODO update the JSON string below
json = "{}"
# create an instance of ColumnPurchaseOrderMappingModel from a JSON string
column_purchase_order_mapping_model_instance = ColumnPurchaseOrderMappingModel.from_json(json)
# print the JSON string representation of the object
print(ColumnPurchaseOrderMappingModel.to_json())

# convert the object into a dict
column_purchase_order_mapping_model_dict = column_purchase_order_mapping_model_instance.to_dict()
# create an instance of ColumnPurchaseOrderMappingModel from a dict
column_purchase_order_mapping_model_from_dict = ColumnPurchaseOrderMappingModel.from_dict(column_purchase_order_mapping_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


