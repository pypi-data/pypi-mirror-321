# ListingsGeteBayTemplatesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | [**GetTemplatesParameters**](GetTemplatesParameters.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.listings_gete_bay_templates_request import ListingsGeteBayTemplatesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListingsGeteBayTemplatesRequest from a JSON string
listings_gete_bay_templates_request_instance = ListingsGeteBayTemplatesRequest.from_json(json)
# print the JSON string representation of the object
print(ListingsGeteBayTemplatesRequest.to_json())

# convert the object into a dict
listings_gete_bay_templates_request_dict = listings_gete_bay_templates_request_instance.to_dict()
# create an instance of ListingsGeteBayTemplatesRequest from a dict
listings_gete_bay_templates_request_from_dict = ListingsGeteBayTemplatesRequest.from_dict(listings_gete_bay_templates_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


