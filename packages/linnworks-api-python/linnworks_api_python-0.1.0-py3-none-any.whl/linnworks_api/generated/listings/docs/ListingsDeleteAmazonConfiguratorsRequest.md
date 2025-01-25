# ListingsDeleteAmazonConfiguratorsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configs** | **List[str]** | Configs guid | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.listings_delete_amazon_configurators_request import ListingsDeleteAmazonConfiguratorsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListingsDeleteAmazonConfiguratorsRequest from a JSON string
listings_delete_amazon_configurators_request_instance = ListingsDeleteAmazonConfiguratorsRequest.from_json(json)
# print the JSON string representation of the object
print(ListingsDeleteAmazonConfiguratorsRequest.to_json())

# convert the object into a dict
listings_delete_amazon_configurators_request_dict = listings_delete_amazon_configurators_request_instance.to_dict()
# create an instance of ListingsDeleteAmazonConfiguratorsRequest from a dict
listings_delete_amazon_configurators_request_from_dict = ListingsDeleteAmazonConfiguratorsRequest.from_dict(listings_delete_amazon_configurators_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


