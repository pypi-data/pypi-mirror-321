# GetBinrackByIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binrack_ids** | **List[int]** |  | [optional] 

## Example

```python
from linnworks_api.generated.stock.models.get_binrack_by_id_request import GetBinrackByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetBinrackByIdRequest from a JSON string
get_binrack_by_id_request_instance = GetBinrackByIdRequest.from_json(json)
# print the JSON string representation of the object
print(GetBinrackByIdRequest.to_json())

# convert the object into a dict
get_binrack_by_id_request_dict = get_binrack_by_id_request_instance.to_dict()
# create an instance of GetBinrackByIdRequest from a dict
get_binrack_by_id_request_from_dict = GetBinrackByIdRequest.from_dict(get_binrack_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


