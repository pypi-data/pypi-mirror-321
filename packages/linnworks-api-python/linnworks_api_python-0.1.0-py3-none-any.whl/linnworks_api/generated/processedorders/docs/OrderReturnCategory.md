# OrderReturnCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_item_id** | **int** |  | [optional] 
**category_name** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.order_return_category import OrderReturnCategory

# TODO update the JSON string below
json = "{}"
# create an instance of OrderReturnCategory from a JSON string
order_return_category_instance = OrderReturnCategory.from_json(json)
# print the JSON string representation of the object
print(OrderReturnCategory.to_json())

# convert the object into a dict
order_return_category_dict = order_return_category_instance.to_dict()
# create an instance of OrderReturnCategory from a dict
order_return_category_from_dict = OrderReturnCategory.from_dict(order_return_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


