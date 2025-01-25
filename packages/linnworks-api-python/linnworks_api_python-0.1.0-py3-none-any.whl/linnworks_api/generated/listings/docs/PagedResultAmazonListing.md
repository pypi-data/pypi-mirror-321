# PagedResultAmazonListing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AmazonListing]**](AmazonListing.md) |  | [optional] 
**total_items** | **int** |  | [optional] 
**current_page** | **int** |  | [optional] 
**entries_per_page** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.paged_result_amazon_listing import PagedResultAmazonListing

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResultAmazonListing from a JSON string
paged_result_amazon_listing_instance = PagedResultAmazonListing.from_json(json)
# print the JSON string representation of the object
print(PagedResultAmazonListing.to_json())

# convert the object into a dict
paged_result_amazon_listing_dict = paged_result_amazon_listing_instance.to_dict()
# create an instance of PagedResultAmazonListing from a dict
paged_result_amazon_listing_from_dict = PagedResultAmazonListing.from_dict(paged_result_amazon_listing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


