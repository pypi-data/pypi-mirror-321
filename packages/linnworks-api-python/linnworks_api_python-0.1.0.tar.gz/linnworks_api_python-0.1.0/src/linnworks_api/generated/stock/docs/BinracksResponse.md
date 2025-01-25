# BinracksResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bin_racks** | [**List[WarehouseBinRack]**](WarehouseBinRack.md) | List of binracks available for the given item in the order applicability. | [optional] 
**decisions** | **List[str]** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.binracks_response import BinracksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BinracksResponse from a JSON string
binracks_response_instance = BinracksResponse.from_json(json)
# print the JSON string representation of the object
print(BinracksResponse.to_json())

# convert the object into a dict
binracks_response_dict = binracks_response_instance.to_dict()
# create an instance of BinracksResponse from a dict
binracks_response_from_dict = BinracksResponse.from_dict(binracks_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


