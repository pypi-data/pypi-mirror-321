# BatchedBookIn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sku** | **str** |  | [optional] 
**batch_number** | **str** |  | [optional] 
**location_id** | **str** |  | [optional] 
**bin_rack** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**stock_value** | **float** |  | [optional] 
**batch_status** | **str** |  | [optional] 
**priority_sequence** | **int** |  | [optional] 
**expires_on** | **datetime** |  | [optional] 
**sell_by** | **datetime** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.batched_book_in import BatchedBookIn

# TODO update the JSON string below
json = "{}"
# create an instance of BatchedBookIn from a JSON string
batched_book_in_instance = BatchedBookIn.from_json(json)
# print the JSON string representation of the object
print(BatchedBookIn.to_json())

# convert the object into a dict
batched_book_in_dict = batched_book_in_instance.to_dict()
# create an instance of BatchedBookIn from a dict
batched_book_in_from_dict = BatchedBookIn.from_dict(batched_book_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


