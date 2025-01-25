# PerfomanceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**price** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.dashboards.models.perfomance_data import PerfomanceData

# TODO update the JSON string below
json = "{}"
# create an instance of PerfomanceData from a JSON string
perfomance_data_instance = PerfomanceData.from_json(json)
# print the JSON string representation of the object
print(PerfomanceData.to_json())

# convert the object into a dict
perfomance_data_dict = perfomance_data_instance.to_dict()
# create an instance of PerfomanceData from a dict
perfomance_data_from_dict = PerfomanceData.from_dict(perfomance_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


