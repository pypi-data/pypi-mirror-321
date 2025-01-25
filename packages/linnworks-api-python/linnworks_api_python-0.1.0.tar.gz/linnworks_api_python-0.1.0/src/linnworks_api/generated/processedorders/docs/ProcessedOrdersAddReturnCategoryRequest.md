# ProcessedOrdersAddReturnCategoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_name** | **str** | The name of the category to add. | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.processed_orders_add_return_category_request import ProcessedOrdersAddReturnCategoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessedOrdersAddReturnCategoryRequest from a JSON string
processed_orders_add_return_category_request_instance = ProcessedOrdersAddReturnCategoryRequest.from_json(json)
# print the JSON string representation of the object
print(ProcessedOrdersAddReturnCategoryRequest.to_json())

# convert the object into a dict
processed_orders_add_return_category_request_dict = processed_orders_add_return_category_request_instance.to_dict()
# create an instance of ProcessedOrdersAddReturnCategoryRequest from a dict
processed_orders_add_return_category_request_from_dict = ProcessedOrdersAddReturnCategoryRequest.from_dict(processed_orders_add_return_category_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


