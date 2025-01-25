# CountryRegion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_region_row_id** | **int** |  | [optional] 
**region_code** | **str** |  | [optional] 
**region_name** | **str** |  | [optional] 
**tax_rate** | **float** |  | [optional] 
**fk_country_id** | **str** |  | [optional] 
**replace_with** | **str** |  | [optional] 
**is_home_region** | **bool** |  | [optional] 
**tags_count** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.country_region import CountryRegion

# TODO update the JSON string below
json = "{}"
# create an instance of CountryRegion from a JSON string
country_region_instance = CountryRegion.from_json(json)
# print the JSON string representation of the object
print(CountryRegion.to_json())

# convert the object into a dict
country_region_dict = country_region_instance.to_dict()
# create an instance of CountryRegion from a dict
country_region_from_dict = CountryRegion.from_dict(country_region_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


