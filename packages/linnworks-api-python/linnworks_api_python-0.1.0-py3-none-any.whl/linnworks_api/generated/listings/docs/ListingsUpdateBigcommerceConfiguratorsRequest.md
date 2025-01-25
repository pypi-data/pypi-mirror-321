# ListingsUpdateBigcommerceConfiguratorsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configs** | [**List[BigCommerceConfigurator]**](BigCommerceConfigurator.md) | Configs to update | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.listings_update_bigcommerce_configurators_request import ListingsUpdateBigcommerceConfiguratorsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListingsUpdateBigcommerceConfiguratorsRequest from a JSON string
listings_update_bigcommerce_configurators_request_instance = ListingsUpdateBigcommerceConfiguratorsRequest.from_json(json)
# print the JSON string representation of the object
print(ListingsUpdateBigcommerceConfiguratorsRequest.to_json())

# convert the object into a dict
listings_update_bigcommerce_configurators_request_dict = listings_update_bigcommerce_configurators_request_instance.to_dict()
# create an instance of ListingsUpdateBigcommerceConfiguratorsRequest from a dict
listings_update_bigcommerce_configurators_request_from_dict = ListingsUpdateBigcommerceConfiguratorsRequest.from_dict(listings_update_bigcommerce_configurators_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


