# GetBinRackSkusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bin_rack_id** | **int** | WMS BinRack Id | [optional] 
**detail_level** | **List[str]** | Detail level required in the response | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.get_bin_rack_skus_request import GetBinRackSkusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetBinRackSkusRequest from a JSON string
get_bin_rack_skus_request_instance = GetBinRackSkusRequest.from_json(json)
# print the JSON string representation of the object
print(GetBinRackSkusRequest.to_json())

# convert the object into a dict
get_bin_rack_skus_request_dict = get_bin_rack_skus_request_instance.to_dict()
# create an instance of GetBinRackSkusRequest from a dict
get_bin_rack_skus_request_from_dict = GetBinRackSkusRequest.from_dict(get_bin_rack_skus_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


