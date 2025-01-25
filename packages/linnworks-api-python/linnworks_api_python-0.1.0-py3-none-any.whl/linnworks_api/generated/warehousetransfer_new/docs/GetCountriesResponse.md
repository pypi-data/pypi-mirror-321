# GetCountriesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.get_countries_response import GetCountriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCountriesResponse from a JSON string
get_countries_response_instance = GetCountriesResponse.from_json(json)
# print the JSON string representation of the object
print(GetCountriesResponse.to_json())

# convert the object into a dict
get_countries_response_dict = get_countries_response_instance.to_dict()
# create an instance of GetCountriesResponse from a dict
get_countries_response_from_dict = GetCountriesResponse.from_dict(get_countries_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


