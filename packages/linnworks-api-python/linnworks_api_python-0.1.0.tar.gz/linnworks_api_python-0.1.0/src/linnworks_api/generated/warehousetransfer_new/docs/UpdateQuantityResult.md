# UpdateQuantityResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_id** | **int** |  | [optional] 
**is_stock_level_changed** | **bool** |  | [optional] 
**quantity_diff** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_new.models.update_quantity_result import UpdateQuantityResult

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateQuantityResult from a JSON string
update_quantity_result_instance = UpdateQuantityResult.from_json(json)
# print the JSON string representation of the object
print(UpdateQuantityResult.to_json())

# convert the object into a dict
update_quantity_result_dict = update_quantity_result_instance.to_dict()
# create an instance of UpdateQuantityResult from a dict
update_quantity_result_from_dict = UpdateQuantityResult.from_dict(update_quantity_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


