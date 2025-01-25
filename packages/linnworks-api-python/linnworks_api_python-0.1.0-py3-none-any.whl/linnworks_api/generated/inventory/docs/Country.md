# Country


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_id** | **str** |  | [optional] 
**country_name** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**continent** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**customs_required** | **bool** |  | [optional] 
**tax_rate** | **float** |  | [optional] 
**address_format** | **str** |  | [optional] 
**regions** | [**List[CountryRegion]**](CountryRegion.md) |  | [optional] 
**regions_count** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.country import Country

# TODO update the JSON string below
json = "{}"
# create an instance of Country from a JSON string
country_instance = Country.from_json(json)
# print the JSON string representation of the object
print(Country.to_json())

# convert the object into a dict
country_dict = country_instance.to_dict()
# create an instance of Country from a dict
country_from_dict = Country.from_dict(country_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


