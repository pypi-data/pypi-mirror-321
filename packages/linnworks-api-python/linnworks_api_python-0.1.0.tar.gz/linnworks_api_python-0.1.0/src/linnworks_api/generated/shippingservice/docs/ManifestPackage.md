# ManifestPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_reference** | **str** |  | [optional] 
**package_seq_no** | **int** |  | [optional] 
**weight** | **float** |  | [optional] 
**depth** | **float** |  | [optional] 
**width** | **float** |  | [optional] 
**height** | **float** |  | [optional] 
**package_format** | **str** |  | [optional] 
**tracking_number** | **str** |  | [optional] 
**value** | **float** |  | [optional] 
**items** | [**List[SavedItem]**](SavedItem.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.shippingservice.models.manifest_package import ManifestPackage

# TODO update the JSON string below
json = "{}"
# create an instance of ManifestPackage from a JSON string
manifest_package_instance = ManifestPackage.from_json(json)
# print the JSON string representation of the object
print(ManifestPackage.to_json())

# convert the object into a dict
manifest_package_dict = manifest_package_instance.to_dict()
# create an instance of ManifestPackage from a dict
manifest_package_from_dict = ManifestPackage.from_dict(manifest_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


