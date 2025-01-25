# CreateCountryRegionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**regions** | [**List[CountryRegion]**](CountryRegion.md) | List of country regions | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.create_country_regions_request import CreateCountryRegionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCountryRegionsRequest from a JSON string
create_country_regions_request_instance = CreateCountryRegionsRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCountryRegionsRequest.to_json())

# convert the object into a dict
create_country_regions_request_dict = create_country_regions_request_instance.to_dict()
# create an instance of CreateCountryRegionsRequest from a dict
create_country_regions_request_from_dict = CreateCountryRegionsRequest.from_dict(create_country_regions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


