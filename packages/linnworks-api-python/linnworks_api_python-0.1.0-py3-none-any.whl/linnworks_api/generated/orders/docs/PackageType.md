# PackageType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_type_id** | **str** |  | [optional] 
**package_group_id** | **str** |  | [optional] 
**package_title** | **str** |  | [optional] 
**from_gramms** | **float** |  | [optional] 
**to_gramms** | **float** |  | [optional] 
**packaging_weight** | **float** |  | [optional] 
**packaging_capacity** | **float** |  | [optional] 
**rowguid** | **str** |  | [optional] 
**width** | **float** |  | [optional] 
**height** | **float** |  | [optional] 
**depth** | **float** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.package_type import PackageType

# TODO update the JSON string below
json = "{}"
# create an instance of PackageType from a JSON string
package_type_instance = PackageType.from_json(json)
# print the JSON string representation of the object
print(PackageType.to_json())

# convert the object into a dict
package_type_dict = package_type_instance.to_dict()
# create an instance of PackageType from a dict
package_type_from_dict = PackageType.from_dict(package_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


