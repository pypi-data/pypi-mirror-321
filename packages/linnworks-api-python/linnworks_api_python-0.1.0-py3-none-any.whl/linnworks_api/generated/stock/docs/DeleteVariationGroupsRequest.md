# DeleteVariationGroupsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variation_groups_id_list** | **List[str]** | A list of VariationsGroups Guids | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.delete_variation_groups_request import DeleteVariationGroupsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteVariationGroupsRequest from a JSON string
delete_variation_groups_request_instance = DeleteVariationGroupsRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteVariationGroupsRequest.to_json())

# convert the object into a dict
delete_variation_groups_request_dict = delete_variation_groups_request_instance.to_dict()
# create an instance of DeleteVariationGroupsRequest from a dict
delete_variation_groups_request_from_dict = DeleteVariationGroupsRequest.from_dict(delete_variation_groups_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


