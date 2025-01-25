# PagedResultMagentoListing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[MagentoListing]**](MagentoListing.md) |  | [optional] 
**total_items** | **int** |  | [optional] 
**current_page** | **int** |  | [optional] 
**entries_per_page** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.paged_result_magento_listing import PagedResultMagentoListing

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResultMagentoListing from a JSON string
paged_result_magento_listing_instance = PagedResultMagentoListing.from_json(json)
# print the JSON string representation of the object
print(PagedResultMagentoListing.to_json())

# convert the object into a dict
paged_result_magento_listing_dict = paged_result_magento_listing_instance.to_dict()
# create an instance of PagedResultMagentoListing from a dict
paged_result_magento_listing_from_dict = PagedResultMagentoListing.from_dict(paged_result_magento_listing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


