# ListingAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**variation** | **bool** |  | [optional] 
**label** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**extended_property** | **str** |  | [optional] 
**default** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.listing_attributes import ListingAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ListingAttributes from a JSON string
listing_attributes_instance = ListingAttributes.from_json(json)
# print the JSON string representation of the object
print(ListingAttributes.to_json())

# convert the object into a dict
listing_attributes_dict = listing_attributes_instance.to_dict()
# create an instance of ListingAttributes from a dict
listing_attributes_from_dict = ListingAttributes.from_dict(listing_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


