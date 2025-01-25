# Dimension


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**width** | **float** |  | [optional] 
**depth** | **float** |  | [optional] 
**height** | **float** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.dimension import Dimension

# TODO update the JSON string below
json = "{}"
# create an instance of Dimension from a JSON string
dimension_instance = Dimension.from_json(json)
# print the JSON string representation of the object
print(Dimension.to_json())

# convert the object into a dict
dimension_dict = dimension_instance.to_dict()
# create an instance of Dimension from a dict
dimension_from_dict = Dimension.from_dict(dimension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


