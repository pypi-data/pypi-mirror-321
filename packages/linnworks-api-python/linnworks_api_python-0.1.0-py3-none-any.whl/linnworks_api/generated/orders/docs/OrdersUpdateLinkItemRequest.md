# OrdersUpdateLinkItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_stock_id** | **str** | Stock id | [optional] 
**pk_stock_item_id** | **str** | Stock item id | [optional] 
**source** | **str** | Source | [optional] 
**sub_source** | **str** | Subsource | [optional] 
**channel_sku** | **str** | Channel SKU | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_update_link_item_request import OrdersUpdateLinkItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersUpdateLinkItemRequest from a JSON string
orders_update_link_item_request_instance = OrdersUpdateLinkItemRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersUpdateLinkItemRequest.to_json())

# convert the object into a dict
orders_update_link_item_request_dict = orders_update_link_item_request_instance.to_dict()
# create an instance of OrdersUpdateLinkItemRequest from a dict
orders_update_link_item_request_from_dict = OrdersUpdateLinkItemRequest.from_dict(orders_update_link_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


