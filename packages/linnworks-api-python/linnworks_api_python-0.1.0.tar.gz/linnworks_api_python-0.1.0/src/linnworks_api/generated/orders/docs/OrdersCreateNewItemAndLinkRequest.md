# OrdersCreateNewItemAndLinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_stock_item_id** | **str** | Stock item id | [optional] 
**item_title** | **str** | Title | [optional] 
**source** | **str** | Source | [optional] 
**sub_source** | **str** | Subsource | [optional] 
**channel_sku** | **str** | Channel SKU | [optional] 
**location_id** | **str** | User location | [optional] 
**initial_quantity** | **int** | Initial quantity once the inventory item has been created | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_create_new_item_and_link_request import OrdersCreateNewItemAndLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersCreateNewItemAndLinkRequest from a JSON string
orders_create_new_item_and_link_request_instance = OrdersCreateNewItemAndLinkRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersCreateNewItemAndLinkRequest.to_json())

# convert the object into a dict
orders_create_new_item_and_link_request_dict = orders_create_new_item_and_link_request_instance.to_dict()
# create an instance of OrdersCreateNewItemAndLinkRequest from a dict
orders_create_new_item_and_link_request_from_dict = OrdersCreateNewItemAndLinkRequest.from_dict(orders_create_new_item_and_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


