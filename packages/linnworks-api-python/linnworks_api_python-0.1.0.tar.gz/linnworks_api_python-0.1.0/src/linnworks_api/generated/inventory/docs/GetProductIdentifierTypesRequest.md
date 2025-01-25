# GetProductIdentifierTypesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**types** | **Dict[str, str]** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.get_product_identifier_types_request import GetProductIdentifierTypesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetProductIdentifierTypesRequest from a JSON string
get_product_identifier_types_request_instance = GetProductIdentifierTypesRequest.from_json(json)
# print the JSON string representation of the object
print(GetProductIdentifierTypesRequest.to_json())

# convert the object into a dict
get_product_identifier_types_request_dict = get_product_identifier_types_request_instance.to_dict()
# create an instance of GetProductIdentifierTypesRequest from a dict
get_product_identifier_types_request_from_dict = GetProductIdentifierTypesRequest.from_dict(get_product_identifier_types_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


