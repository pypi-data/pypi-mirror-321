# PagedResultEbayListing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[EbayListing]**](EbayListing.md) |  | [optional] 
**total_items** | **int** |  | [optional] 
**current_page** | **int** |  | [optional] 
**entries_per_page** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.paged_result_ebay_listing import PagedResultEbayListing

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResultEbayListing from a JSON string
paged_result_ebay_listing_instance = PagedResultEbayListing.from_json(json)
# print the JSON string representation of the object
print(PagedResultEbayListing.to_json())

# convert the object into a dict
paged_result_ebay_listing_dict = paged_result_ebay_listing_instance.to_dict()
# create an instance of PagedResultEbayListing from a dict
paged_result_ebay_listing_from_dict = PagedResultEbayListing.from_dict(paged_result_ebay_listing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


