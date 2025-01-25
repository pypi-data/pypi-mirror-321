# ProcessedOrdersDeleteReturnCategoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_item_id** | **int** | The id of the category to delete. | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.processed_orders_delete_return_category_request import ProcessedOrdersDeleteReturnCategoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessedOrdersDeleteReturnCategoryRequest from a JSON string
processed_orders_delete_return_category_request_instance = ProcessedOrdersDeleteReturnCategoryRequest.from_json(json)
# print the JSON string representation of the object
print(ProcessedOrdersDeleteReturnCategoryRequest.to_json())

# convert the object into a dict
processed_orders_delete_return_category_request_dict = processed_orders_delete_return_category_request_instance.to_dict()
# create an instance of ProcessedOrdersDeleteReturnCategoryRequest from a dict
processed_orders_delete_return_category_request_from_dict = ProcessedOrdersDeleteReturnCategoryRequest.from_dict(processed_orders_delete_return_category_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


