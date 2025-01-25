# ProcessedOrdersRenameReturnCategoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_item_id** | **int** | The id of the category to be renamed. | [optional] 
**new_name** | **str** | The new name for the category. | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.processed_orders_rename_return_category_request import ProcessedOrdersRenameReturnCategoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessedOrdersRenameReturnCategoryRequest from a JSON string
processed_orders_rename_return_category_request_instance = ProcessedOrdersRenameReturnCategoryRequest.from_json(json)
# print the JSON string representation of the object
print(ProcessedOrdersRenameReturnCategoryRequest.to_json())

# convert the object into a dict
processed_orders_rename_return_category_request_dict = processed_orders_rename_return_category_request_instance.to_dict()
# create an instance of ProcessedOrdersRenameReturnCategoryRequest from a dict
processed_orders_rename_return_category_request_from_dict = ProcessedOrdersRenameReturnCategoryRequest.from_dict(processed_orders_rename_return_category_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


