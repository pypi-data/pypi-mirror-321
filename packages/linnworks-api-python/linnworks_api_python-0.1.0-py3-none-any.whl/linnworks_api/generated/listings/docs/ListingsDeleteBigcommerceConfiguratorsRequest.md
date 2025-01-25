# ListingsDeleteBigcommerceConfiguratorsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configs** | **List[str]** | Configs to delete | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.listings_delete_bigcommerce_configurators_request import ListingsDeleteBigcommerceConfiguratorsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListingsDeleteBigcommerceConfiguratorsRequest from a JSON string
listings_delete_bigcommerce_configurators_request_instance = ListingsDeleteBigcommerceConfiguratorsRequest.from_json(json)
# print the JSON string representation of the object
print(ListingsDeleteBigcommerceConfiguratorsRequest.to_json())

# convert the object into a dict
listings_delete_bigcommerce_configurators_request_dict = listings_delete_bigcommerce_configurators_request_instance.to_dict()
# create an instance of ListingsDeleteBigcommerceConfiguratorsRequest from a dict
listings_delete_bigcommerce_configurators_request_from_dict = ListingsDeleteBigcommerceConfiguratorsRequest.from_dict(listings_delete_bigcommerce_configurators_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


