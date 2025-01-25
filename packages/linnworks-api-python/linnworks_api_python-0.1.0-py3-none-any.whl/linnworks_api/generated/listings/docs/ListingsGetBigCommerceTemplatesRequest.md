# ListingsGetBigCommerceTemplatesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | [**GetTemplatesParameters**](GetTemplatesParameters.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.listings_get_big_commerce_templates_request import ListingsGetBigCommerceTemplatesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListingsGetBigCommerceTemplatesRequest from a JSON string
listings_get_big_commerce_templates_request_instance = ListingsGetBigCommerceTemplatesRequest.from_json(json)
# print the JSON string representation of the object
print(ListingsGetBigCommerceTemplatesRequest.to_json())

# convert the object into a dict
listings_get_big_commerce_templates_request_dict = listings_get_big_commerce_templates_request_instance.to_dict()
# create an instance of ListingsGetBigCommerceTemplatesRequest from a dict
listings_get_big_commerce_templates_request_from_dict = ListingsGetBigCommerceTemplatesRequest.from_dict(listings_get_big_commerce_templates_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


