# ListingsProcessAmazonListingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AmazonListing]**](AmazonListing.md) | Amazon listings | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.listings_process_amazon_listings_request import ListingsProcessAmazonListingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListingsProcessAmazonListingsRequest from a JSON string
listings_process_amazon_listings_request_instance = ListingsProcessAmazonListingsRequest.from_json(json)
# print the JSON string representation of the object
print(ListingsProcessAmazonListingsRequest.to_json())

# convert the object into a dict
listings_process_amazon_listings_request_dict = listings_process_amazon_listings_request_instance.to_dict()
# create an instance of ListingsProcessAmazonListingsRequest from a dict
listings_process_amazon_listings_request_from_dict = ListingsProcessAmazonListingsRequest.from_dict(listings_process_amazon_listings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


