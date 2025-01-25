# ProcessOrderByOrderIdOrReferenceRequest

A request used to process an order by id or reference

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_or_reference_id** | **str** | The order id or reference id | [optional] 
**location_id** | **str** | The location to process the order from | [optional] 
**scans_performed** | **bool** | Defines if the batches have been scanned | [optional] 
**order_processing_notes_acknowledged** | **bool** | Have the processing notes been acknowledged | [optional] 
**workflow_job_id** | **int** | Workflow job id that the order is supposed to belong to | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.process_order_by_order_id_or_reference_request import ProcessOrderByOrderIdOrReferenceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessOrderByOrderIdOrReferenceRequest from a JSON string
process_order_by_order_id_or_reference_request_instance = ProcessOrderByOrderIdOrReferenceRequest.from_json(json)
# print the JSON string representation of the object
print(ProcessOrderByOrderIdOrReferenceRequest.to_json())

# convert the object into a dict
process_order_by_order_id_or_reference_request_dict = process_order_by_order_id_or_reference_request_instance.to_dict()
# create an instance of ProcessOrderByOrderIdOrReferenceRequest from a dict
process_order_by_order_id_or_reference_request_from_dict = ProcessOrderByOrderIdOrReferenceRequest.from_dict(process_order_by_order_id_or_reference_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


