# FiledManifest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manifest_id** | **int** |  | [optional] 
**var_date** | **datetime** |  | [optional] 
**external_manifest_id** | **str** |  | [optional] 
**reference** | **str** |  | [optional] 
**is_error** | **bool** |  | [optional] 
**vendor** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 
**num_consignments** | **int** |  | [optional] 
**fk_shipping_api_config_id** | **int** |  | [optional] 
**is_complete** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.shippingservice.models.filed_manifest import FiledManifest

# TODO update the JSON string below
json = "{}"
# create an instance of FiledManifest from a JSON string
filed_manifest_instance = FiledManifest.from_json(json)
# print the JSON string representation of the object
print(FiledManifest.to_json())

# convert the object into a dict
filed_manifest_dict = filed_manifest_instance.to_dict()
# create an instance of FiledManifest from a dict
filed_manifest_from_dict = FiledManifest.from_dict(filed_manifest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


