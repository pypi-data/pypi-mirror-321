# GeoPosition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x** | **float** |  | [optional] 
**y** | **float** |  | [optional] 
**z** | **float** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.geo_position import GeoPosition

# TODO update the JSON string below
json = "{}"
# create an instance of GeoPosition from a JSON string
geo_position_instance = GeoPosition.from_json(json)
# print the JSON string representation of the object
print(GeoPosition.to_json())

# convert the object into a dict
geo_position_dict = geo_position_instance.to_dict()
# create an instance of GeoPosition from a dict
geo_position_from_dict = GeoPosition.from_dict(geo_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


