# ProcessOrderByOrderIdOrReferenceResponse

A response class used when processing an order by order id or reference

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**processed_state** | **str** | The processed state | [optional] 
**message** | **str** | A message - Provided if there have been errors | [optional] 
**response** | **object** | A response object used if further action is required | [optional] 
**order_id** | **str** | The ID of the order - Guid empty if not found | [optional] 
**order_summary** | [**OrderSummary**](OrderSummary.md) |  | [optional] 
**items** | [**List[OrderItem]**](OrderItem.md) | The items that need to be scanned - If any | [optional] 
**batch_information** | [**List[StockItemBatch]**](StockItemBatch.md) | The batched items | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.process_order_by_order_id_or_reference_response import ProcessOrderByOrderIdOrReferenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessOrderByOrderIdOrReferenceResponse from a JSON string
process_order_by_order_id_or_reference_response_instance = ProcessOrderByOrderIdOrReferenceResponse.from_json(json)
# print the JSON string representation of the object
print(ProcessOrderByOrderIdOrReferenceResponse.to_json())

# convert the object into a dict
process_order_by_order_id_or_reference_response_dict = process_order_by_order_id_or_reference_response_instance.to_dict()
# create an instance of ProcessOrderByOrderIdOrReferenceResponse from a dict
process_order_by_order_id_or_reference_response_from_dict = ProcessOrderByOrderIdOrReferenceResponse.from_dict(process_order_by_order_id_or_reference_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


