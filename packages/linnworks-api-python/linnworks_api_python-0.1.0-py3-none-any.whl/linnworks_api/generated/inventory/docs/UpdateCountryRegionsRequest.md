# UpdateCountryRegionsRequest

Country region information to update

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**regions** | [**List[CountryRegion]**](CountryRegion.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.update_country_regions_request import UpdateCountryRegionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCountryRegionsRequest from a JSON string
update_country_regions_request_instance = UpdateCountryRegionsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateCountryRegionsRequest.to_json())

# convert the object into a dict
update_country_regions_request_dict = update_country_regions_request_instance.to_dict()
# create an instance of UpdateCountryRegionsRequest from a dict
update_country_regions_request_from_dict = UpdateCountryRegionsRequest.from_dict(update_country_regions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


