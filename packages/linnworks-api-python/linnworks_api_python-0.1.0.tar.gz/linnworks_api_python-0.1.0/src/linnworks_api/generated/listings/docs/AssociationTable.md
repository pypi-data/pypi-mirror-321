# AssociationTable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table_name** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**destination** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.association_table import AssociationTable

# TODO update the JSON string below
json = "{}"
# create an instance of AssociationTable from a JSON string
association_table_instance = AssociationTable.from_json(json)
# print the JSON string representation of the object
print(AssociationTable.to_json())

# convert the object into a dict
association_table_dict = association_table_instance.to_dict()
# create an instance of AssociationTable from a dict
association_table_from_dict = AssociationTable.from_dict(association_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


