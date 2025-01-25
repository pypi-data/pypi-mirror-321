# GetRMAHeadersByOrderIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.get_rma_headers_by_order_id_request import GetRMAHeadersByOrderIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetRMAHeadersByOrderIdRequest from a JSON string
get_rma_headers_by_order_id_request_instance = GetRMAHeadersByOrderIdRequest.from_json(json)
# print the JSON string representation of the object
print(GetRMAHeadersByOrderIdRequest.to_json())

# convert the object into a dict
get_rma_headers_by_order_id_request_dict = get_rma_headers_by_order_id_request_instance.to_dict()
# create an instance of GetRMAHeadersByOrderIdRequest from a dict
get_rma_headers_by_order_id_request_from_dict = GetRMAHeadersByOrderIdRequest.from_dict(get_rma_headers_by_order_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


