# GetRMAHeadersByOrderIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rma_headers** | [**List[OrderRMAHeader]**](OrderRMAHeader.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.get_rma_headers_by_order_id_response import GetRMAHeadersByOrderIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRMAHeadersByOrderIdResponse from a JSON string
get_rma_headers_by_order_id_response_instance = GetRMAHeadersByOrderIdResponse.from_json(json)
# print the JSON string representation of the object
print(GetRMAHeadersByOrderIdResponse.to_json())

# convert the object into a dict
get_rma_headers_by_order_id_response_dict = get_rma_headers_by_order_id_response_instance.to_dict()
# create an instance of GetRMAHeadersByOrderIdResponse from a dict
get_rma_headers_by_order_id_response_from_dict = GetRMAHeadersByOrderIdResponse.from_dict(get_rma_headers_by_order_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


