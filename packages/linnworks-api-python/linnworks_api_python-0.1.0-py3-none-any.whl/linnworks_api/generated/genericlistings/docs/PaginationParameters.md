# PaginationParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_number** | **int** |  | [optional] 
**entries_per_page** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.genericlistings.models.pagination_parameters import PaginationParameters

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationParameters from a JSON string
pagination_parameters_instance = PaginationParameters.from_json(json)
# print the JSON string representation of the object
print(PaginationParameters.to_json())

# convert the object into a dict
pagination_parameters_dict = pagination_parameters_instance.to_dict()
# create an instance of PaginationParameters from a dict
pagination_parameters_from_dict = PaginationParameters.from_dict(pagination_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


