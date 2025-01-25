# BinRackResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bin_rack_id** | **int** |  | [optional] 
**bin_rack** | **str** |  | [optional] 
**bin_rack_type_id** | **int** |  | [optional] 
**bin_rack_type_name** | **str** |  | [optional] 
**routing_sequence** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.bin_rack_response import BinRackResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BinRackResponse from a JSON string
bin_rack_response_instance = BinRackResponse.from_json(json)
# print the JSON string representation of the object
print(BinRackResponse.to_json())

# convert the object into a dict
bin_rack_response_dict = bin_rack_response_instance.to_dict()
# create an instance of BinRackResponse from a dict
bin_rack_response_from_dict = BinRackResponse.from_dict(bin_rack_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


