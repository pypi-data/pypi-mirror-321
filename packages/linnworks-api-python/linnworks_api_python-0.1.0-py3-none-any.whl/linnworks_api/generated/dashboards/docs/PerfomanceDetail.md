# PerfomanceDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** |  | [optional] 
**value** | **float** |  | [optional] 

## Example

```python
from linnworks_api.generated.dashboards.models.perfomance_detail import PerfomanceDetail

# TODO update the JSON string below
json = "{}"
# create an instance of PerfomanceDetail from a JSON string
perfomance_detail_instance = PerfomanceDetail.from_json(json)
# print the JSON string representation of the object
print(PerfomanceDetail.to_json())

# convert the object into a dict
perfomance_detail_dict = perfomance_detail_instance.to_dict()
# create an instance of PerfomanceDetail from a dict
perfomance_detail_from_dict = PerfomanceDetail.from_dict(perfomance_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


