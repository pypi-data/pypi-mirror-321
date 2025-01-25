# BatchDatesUpdateItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row_index** | **int** |  | [optional] 
**batch_number** | **str** |  | [optional] 
**sell_by** | **datetime** |  | [optional] 
**expiry** | **datetime** |  | [optional] 
**sku** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.batch_dates_update_item import BatchDatesUpdateItem

# TODO update the JSON string below
json = "{}"
# create an instance of BatchDatesUpdateItem from a JSON string
batch_dates_update_item_instance = BatchDatesUpdateItem.from_json(json)
# print the JSON string representation of the object
print(BatchDatesUpdateItem.to_json())

# convert the object into a dict
batch_dates_update_item_dict = batch_dates_update_item_instance.to_dict()
# create an instance of BatchDatesUpdateItem from a dict
batch_dates_update_item_from_dict = BatchDatesUpdateItem.from_dict(batch_dates_update_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


