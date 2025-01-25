# PagedResultBigCommerceListing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[BigCommerceListing]**](BigCommerceListing.md) |  | [optional] 
**total_items** | **int** |  | [optional] 
**current_page** | **int** |  | [optional] 
**entries_per_page** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.paged_result_big_commerce_listing import PagedResultBigCommerceListing

# TODO update the JSON string below
json = "{}"
# create an instance of PagedResultBigCommerceListing from a JSON string
paged_result_big_commerce_listing_instance = PagedResultBigCommerceListing.from_json(json)
# print the JSON string representation of the object
print(PagedResultBigCommerceListing.to_json())

# convert the object into a dict
paged_result_big_commerce_listing_dict = paged_result_big_commerce_listing_instance.to_dict()
# create an instance of PagedResultBigCommerceListing from a dict
paged_result_big_commerce_listing_from_dict = PagedResultBigCommerceListing.from_dict(paged_result_big_commerce_listing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


