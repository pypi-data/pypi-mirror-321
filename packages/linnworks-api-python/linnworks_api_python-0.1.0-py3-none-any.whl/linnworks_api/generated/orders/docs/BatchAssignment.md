# BatchAssignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_item_row_id** | **str** |  | [optional] 
**batch_inventory_id** | **int** |  | [optional] 
**quantity** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.batch_assignment import BatchAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of BatchAssignment from a JSON string
batch_assignment_instance = BatchAssignment.from_json(json)
# print the JSON string representation of the object
print(BatchAssignment.to_json())

# convert the object into a dict
batch_assignment_dict = batch_assignment_instance.to_dict()
# create an instance of BatchAssignment from a dict
batch_assignment_from_dict = BatchAssignment.from_dict(batch_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


