# PackingResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_packages** | **int** |  | [optional] [readonly] 
**packages** | [**List[PackageResult]**](PackageResult.md) |  | [optional] 
**unpacked_items** | **Dict[str, int]** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.packing_result import PackingResult

# TODO update the JSON string below
json = "{}"
# create an instance of PackingResult from a JSON string
packing_result_instance = PackingResult.from_json(json)
# print the JSON string representation of the object
print(PackingResult.to_json())

# convert the object into a dict
packing_result_dict = packing_result_instance.to_dict()
# create an instance of PackingResult from a dict
packing_result_from_dict = PackingResult.from_dict(packing_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


