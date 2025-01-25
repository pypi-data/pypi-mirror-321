# CreateCountryRegionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**regions** | [**List[CountryRegion]**](CountryRegion.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.create_country_regions_response import CreateCountryRegionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCountryRegionsResponse from a JSON string
create_country_regions_response_instance = CreateCountryRegionsResponse.from_json(json)
# print the JSON string representation of the object
print(CreateCountryRegionsResponse.to_json())

# convert the object into a dict
create_country_regions_response_dict = create_country_regions_response_instance.to_dict()
# create an instance of CreateCountryRegionsResponse from a dict
create_country_regions_response_from_dict = CreateCountryRegionsResponse.from_dict(create_country_regions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


