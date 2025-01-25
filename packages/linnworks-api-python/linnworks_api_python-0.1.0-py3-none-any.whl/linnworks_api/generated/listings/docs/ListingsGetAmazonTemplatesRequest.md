# ListingsGetAmazonTemplatesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | [**GetTemplatesParameters**](GetTemplatesParameters.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.listings_get_amazon_templates_request import ListingsGetAmazonTemplatesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListingsGetAmazonTemplatesRequest from a JSON string
listings_get_amazon_templates_request_instance = ListingsGetAmazonTemplatesRequest.from_json(json)
# print the JSON string representation of the object
print(ListingsGetAmazonTemplatesRequest.to_json())

# convert the object into a dict
listings_get_amazon_templates_request_dict = listings_get_amazon_templates_request_instance.to_dict()
# create an instance of ListingsGetAmazonTemplatesRequest from a dict
listings_get_amazon_templates_request_from_dict = ListingsGetAmazonTemplatesRequest.from_dict(listings_get_amazon_templates_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


