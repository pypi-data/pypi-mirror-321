# ProcessedOrdersCreateExchangeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_order_id** | **str** | The order id | [optional] 
**exchange_items** | [**List[RowQty]**](RowQty.md) | A list of items to be exchanged, including quantity, scrap, refund, etc. | [optional] 
**despatch_location** | **str** | The id of the location to despatch replacement items from | [optional] 
**return_location** | **str** | The id of the location to return stock to | [optional] 
**channel_reason** | **str** | Channel reason - required if a refund on the channel is required | [optional] 
**channel_sub_reason** | **str** | Channel subreason - required if a refund on the channel is required. | [optional] 
**category** | **str** | The refund category | [optional] 
**reason** | **str** | The reason for the reason | [optional] 
**is_booking** | **bool** | True if it is a exchange booking, False if it is a new exchange | [optional] 
**ignored_validation** | **bool** | True if failed validation has been ignored (see IsRefundValid). Otherwise, false. When set to true, refunds will not be automatically actioned on the channel. Ignored if creating a booking as a refund is not created at this stage. | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.processed_orders_create_exchange_request import ProcessedOrdersCreateExchangeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessedOrdersCreateExchangeRequest from a JSON string
processed_orders_create_exchange_request_instance = ProcessedOrdersCreateExchangeRequest.from_json(json)
# print the JSON string representation of the object
print(ProcessedOrdersCreateExchangeRequest.to_json())

# convert the object into a dict
processed_orders_create_exchange_request_dict = processed_orders_create_exchange_request_instance.to_dict()
# create an instance of ProcessedOrdersCreateExchangeRequest from a dict
processed_orders_create_exchange_request_from_dict = ProcessedOrdersCreateExchangeRequest.from_dict(processed_orders_create_exchange_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


