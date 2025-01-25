# MarkReadyForCollectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_ids** | **List[str]** |  | [optional] 

## Example

```python
from linnworks_api.generated.openorders.models.mark_ready_for_collection_request import MarkReadyForCollectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MarkReadyForCollectionRequest from a JSON string
mark_ready_for_collection_request_instance = MarkReadyForCollectionRequest.from_json(json)
# print the JSON string representation of the object
print(MarkReadyForCollectionRequest.to_json())

# convert the object into a dict
mark_ready_for_collection_request_dict = mark_ready_for_collection_request_instance.to_dict()
# create an instance of MarkReadyForCollectionRequest from a dict
mark_ready_for_collection_request_from_dict = MarkReadyForCollectionRequest.from_dict(mark_ready_for_collection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


