# ListingsDeleteAmazonTemplatesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_ids** | **List[str]** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.listings_delete_amazon_templates_request import ListingsDeleteAmazonTemplatesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListingsDeleteAmazonTemplatesRequest from a JSON string
listings_delete_amazon_templates_request_instance = ListingsDeleteAmazonTemplatesRequest.from_json(json)
# print the JSON string representation of the object
print(ListingsDeleteAmazonTemplatesRequest.to_json())

# convert the object into a dict
listings_delete_amazon_templates_request_dict = listings_delete_amazon_templates_request_instance.to_dict()
# create an instance of ListingsDeleteAmazonTemplatesRequest from a dict
listings_delete_amazon_templates_request_from_dict = ListingsDeleteAmazonTemplatesRequest.from_dict(listings_delete_amazon_templates_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


