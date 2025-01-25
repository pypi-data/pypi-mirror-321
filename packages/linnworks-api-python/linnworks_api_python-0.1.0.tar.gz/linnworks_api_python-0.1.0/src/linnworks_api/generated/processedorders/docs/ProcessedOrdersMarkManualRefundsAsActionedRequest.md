# ProcessedOrdersMarkManualRefundsAsActionedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_order_id** | **str** | The id of the order to action refunds on. | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.processed_orders_mark_manual_refunds_as_actioned_request import ProcessedOrdersMarkManualRefundsAsActionedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessedOrdersMarkManualRefundsAsActionedRequest from a JSON string
processed_orders_mark_manual_refunds_as_actioned_request_instance = ProcessedOrdersMarkManualRefundsAsActionedRequest.from_json(json)
# print the JSON string representation of the object
print(ProcessedOrdersMarkManualRefundsAsActionedRequest.to_json())

# convert the object into a dict
processed_orders_mark_manual_refunds_as_actioned_request_dict = processed_orders_mark_manual_refunds_as_actioned_request_instance.to_dict()
# create an instance of ProcessedOrdersMarkManualRefundsAsActionedRequest from a dict
processed_orders_mark_manual_refunds_as_actioned_request_from_dict = ProcessedOrdersMarkManualRefundsAsActionedRequest.from_dict(processed_orders_mark_manual_refunds_as_actioned_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


