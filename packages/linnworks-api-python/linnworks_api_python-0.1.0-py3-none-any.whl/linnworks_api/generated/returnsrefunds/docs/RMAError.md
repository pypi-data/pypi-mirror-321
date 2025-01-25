# RMAError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rma_row_id** | **int** |  | [optional] 
**error_message** | **str** |  | [optional] 
**date_stamp** | **datetime** |  | [optional] 
**acknowledged** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.rma_error import RMAError

# TODO update the JSON string below
json = "{}"
# create an instance of RMAError from a JSON string
rma_error_instance = RMAError.from_json(json)
# print the JSON string representation of the object
print(RMAError.to_json())

# convert the object into a dict
rma_error_dict = rma_error_instance.to_dict()
# create an instance of RMAError from a dict
rma_error_from_dict = RMAError.from_dict(rma_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


