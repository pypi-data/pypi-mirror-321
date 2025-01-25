# ListingsProcessBigcommerceListingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[BigCommerceListing]**](BigCommerceListing.md) | Bigcommerce templates | [optional] 
**force** | **bool** | force | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.listings_process_bigcommerce_listings_request import ListingsProcessBigcommerceListingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListingsProcessBigcommerceListingsRequest from a JSON string
listings_process_bigcommerce_listings_request_instance = ListingsProcessBigcommerceListingsRequest.from_json(json)
# print the JSON string representation of the object
print(ListingsProcessBigcommerceListingsRequest.to_json())

# convert the object into a dict
listings_process_bigcommerce_listings_request_dict = listings_process_bigcommerce_listings_request_instance.to_dict()
# create an instance of ListingsProcessBigcommerceListingsRequest from a dict
listings_process_bigcommerce_listings_request_from_dict = ListingsProcessBigcommerceListingsRequest.from_dict(listings_process_bigcommerce_listings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


