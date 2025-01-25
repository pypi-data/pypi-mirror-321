# ListingsDeleteEbayTemplatesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_ids** | **List[str]** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.listings_delete_ebay_templates_request import ListingsDeleteEbayTemplatesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListingsDeleteEbayTemplatesRequest from a JSON string
listings_delete_ebay_templates_request_instance = ListingsDeleteEbayTemplatesRequest.from_json(json)
# print the JSON string representation of the object
print(ListingsDeleteEbayTemplatesRequest.to_json())

# convert the object into a dict
listings_delete_ebay_templates_request_dict = listings_delete_ebay_templates_request_instance.to_dict()
# create an instance of ListingsDeleteEbayTemplatesRequest from a dict
listings_delete_ebay_templates_request_from_dict = ListingsDeleteEbayTemplatesRequest.from_dict(listings_delete_ebay_templates_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


