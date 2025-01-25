# ListingsCreateTemplatesFromViewInBulkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | [**CreateTemplatesInBulkParameters**](CreateTemplatesInBulkParameters.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.listings_create_templates_from_view_in_bulk_request import ListingsCreateTemplatesFromViewInBulkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListingsCreateTemplatesFromViewInBulkRequest from a JSON string
listings_create_templates_from_view_in_bulk_request_instance = ListingsCreateTemplatesFromViewInBulkRequest.from_json(json)
# print the JSON string representation of the object
print(ListingsCreateTemplatesFromViewInBulkRequest.to_json())

# convert the object into a dict
listings_create_templates_from_view_in_bulk_request_dict = listings_create_templates_from_view_in_bulk_request_instance.to_dict()
# create an instance of ListingsCreateTemplatesFromViewInBulkRequest from a dict
listings_create_templates_from_view_in_bulk_request_from_dict = ListingsCreateTemplatesFromViewInBulkRequest.from_dict(listings_create_templates_from_view_in_bulk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


