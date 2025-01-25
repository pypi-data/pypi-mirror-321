# GetScannableProductIdentifiersByOrderIdsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scannable_product_identifiers_for_stock_items_by_order_id** | **Dict[str, Dict[str, List[ProductIdentifierInformation]]]** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.get_scannable_product_identifiers_by_order_ids_response import GetScannableProductIdentifiersByOrderIdsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetScannableProductIdentifiersByOrderIdsResponse from a JSON string
get_scannable_product_identifiers_by_order_ids_response_instance = GetScannableProductIdentifiersByOrderIdsResponse.from_json(json)
# print the JSON string representation of the object
print(GetScannableProductIdentifiersByOrderIdsResponse.to_json())

# convert the object into a dict
get_scannable_product_identifiers_by_order_ids_response_dict = get_scannable_product_identifiers_by_order_ids_response_instance.to_dict()
# create an instance of GetScannableProductIdentifiersByOrderIdsResponse from a dict
get_scannable_product_identifiers_by_order_ids_response_from_dict = GetScannableProductIdentifiersByOrderIdsResponse.from_dict(get_scannable_product_identifiers_by_order_ids_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


