# PackageResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**packaging_id** | **str** |  | [optional] 
**width** | **float** |  | [optional] 
**height** | **float** |  | [optional] 
**depth** | **float** |  | [optional] 
**item_weight** | **float** |  | [optional] 
**packaging_weight** | **float** |  | [optional] 
**faces** | [**List[Face]**](Face.md) |  | [optional] 
**items** | [**List[PackedItem]**](PackedItem.md) |  | [optional] 
**layer_count** | **int** |  | [optional] 
**layer_face** | [**Dict[str, Face]**](Face.md) |  | [optional] 
**is_manual_package** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.package_result import PackageResult

# TODO update the JSON string below
json = "{}"
# create an instance of PackageResult from a JSON string
package_result_instance = PackageResult.from_json(json)
# print the JSON string representation of the object
print(PackageResult.to_json())

# convert the object into a dict
package_result_dict = package_result_instance.to_dict()
# create an instance of PackageResult from a dict
package_result_from_dict = PackageResult.from_dict(package_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


