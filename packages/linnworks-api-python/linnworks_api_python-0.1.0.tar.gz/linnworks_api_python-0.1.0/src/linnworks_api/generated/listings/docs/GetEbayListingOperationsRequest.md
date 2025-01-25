# GetEbayListingOperationsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_id** | **str** |  | [optional] 
**page_number** | **int** |  | [optional] 
**entries_per_page** | **int** |  | [optional] 
**channel_ids** | **List[int]** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.get_ebay_listing_operations_request import GetEbayListingOperationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetEbayListingOperationsRequest from a JSON string
get_ebay_listing_operations_request_instance = GetEbayListingOperationsRequest.from_json(json)
# print the JSON string representation of the object
print(GetEbayListingOperationsRequest.to_json())

# convert the object into a dict
get_ebay_listing_operations_request_dict = get_ebay_listing_operations_request_instance.to_dict()
# create an instance of GetEbayListingOperationsRequest from a dict
get_ebay_listing_operations_request_from_dict = GetEbayListingOperationsRequest.from_dict(get_ebay_listing_operations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


