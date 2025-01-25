# ListingsCreateBigcommerceConfiguratorsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configs** | [**List[BigCommerceConfigurator]**](BigCommerceConfigurator.md) | Configs to create | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.listings_create_bigcommerce_configurators_request import ListingsCreateBigcommerceConfiguratorsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListingsCreateBigcommerceConfiguratorsRequest from a JSON string
listings_create_bigcommerce_configurators_request_instance = ListingsCreateBigcommerceConfiguratorsRequest.from_json(json)
# print the JSON string representation of the object
print(ListingsCreateBigcommerceConfiguratorsRequest.to_json())

# convert the object into a dict
listings_create_bigcommerce_configurators_request_dict = listings_create_bigcommerce_configurators_request_instance.to_dict()
# create an instance of ListingsCreateBigcommerceConfiguratorsRequest from a dict
listings_create_bigcommerce_configurators_request_from_dict = ListingsCreateBigcommerceConfiguratorsRequest.from_dict(listings_create_bigcommerce_configurators_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


