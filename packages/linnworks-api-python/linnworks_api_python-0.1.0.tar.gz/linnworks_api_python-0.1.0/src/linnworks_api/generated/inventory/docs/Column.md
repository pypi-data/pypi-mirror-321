# Column


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] [readonly] 
**export_name** | **str** |  | [optional] [readonly] 
**group** | **str** |  | [optional] [readonly] 
**var_field** | **str** |  | [optional] [readonly] 
**sort_direction** | **str** |  | [optional] 
**width** | **float** |  | [optional] 
**is_editable** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.column import Column

# TODO update the JSON string below
json = "{}"
# create an instance of Column from a JSON string
column_instance = Column.from_json(json)
# print the JSON string representation of the object
print(Column.to_json())

# convert the object into a dict
column_dict = column_instance.to_dict()
# create an instance of Column from a dict
column_from_dict = Column.from_dict(column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


