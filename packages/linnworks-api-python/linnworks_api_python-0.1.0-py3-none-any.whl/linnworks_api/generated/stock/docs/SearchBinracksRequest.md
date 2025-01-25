# SearchBinracksRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bin_rack** | **str** | Bin rack search term. For example for PUT1.2.3878, bin rack search term PUT1 will yeild the result | [optional] 
**location_id** | **str** | Specific location id. Location must be Warehouse Managed location | [optional] 
**stock_item_id** | **str** | Stock Item Id | [optional] 
**bin_rack_type_ids** | **List[int]** | List of types of bin racks, nullable. If not provided all binrack types will be searched | [optional] 
**page_number** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.search_binracks_request import SearchBinracksRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SearchBinracksRequest from a JSON string
search_binracks_request_instance = SearchBinracksRequest.from_json(json)
# print the JSON string representation of the object
print(SearchBinracksRequest.to_json())

# convert the object into a dict
search_binracks_request_dict = search_binracks_request_instance.to_dict()
# create an instance of SearchBinracksRequest from a dict
search_binracks_request_from_dict = SearchBinracksRequest.from_dict(search_binracks_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


