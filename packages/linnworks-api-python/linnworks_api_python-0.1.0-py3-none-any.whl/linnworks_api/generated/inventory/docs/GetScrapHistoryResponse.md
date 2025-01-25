# GetScrapHistoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scrap_history** | [**GenericPagedResultScrapItem**](GenericPagedResultScrapItem.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.get_scrap_history_response import GetScrapHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetScrapHistoryResponse from a JSON string
get_scrap_history_response_instance = GetScrapHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(GetScrapHistoryResponse.to_json())

# convert the object into a dict
get_scrap_history_response_dict = get_scrap_history_response_instance.to_dict()
# create an instance of GetScrapHistoryResponse from a dict
get_scrap_history_response_from_dict = GetScrapHistoryResponse.from_dict(get_scrap_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


