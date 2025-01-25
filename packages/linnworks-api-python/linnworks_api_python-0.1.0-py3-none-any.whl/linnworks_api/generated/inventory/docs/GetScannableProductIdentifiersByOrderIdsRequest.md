# GetScannableProductIdentifiersByOrderIdsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_ids** | **List[str]** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.get_scannable_product_identifiers_by_order_ids_request import GetScannableProductIdentifiersByOrderIdsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetScannableProductIdentifiersByOrderIdsRequest from a JSON string
get_scannable_product_identifiers_by_order_ids_request_instance = GetScannableProductIdentifiersByOrderIdsRequest.from_json(json)
# print the JSON string representation of the object
print(GetScannableProductIdentifiersByOrderIdsRequest.to_json())

# convert the object into a dict
get_scannable_product_identifiers_by_order_ids_request_dict = get_scannable_product_identifiers_by_order_ids_request_instance.to_dict()
# create an instance of GetScannableProductIdentifiersByOrderIdsRequest from a dict
get_scannable_product_identifiers_by_order_ids_request_from_dict = GetScannableProductIdentifiersByOrderIdsRequest.from_dict(get_scannable_product_identifiers_by_order_ids_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


