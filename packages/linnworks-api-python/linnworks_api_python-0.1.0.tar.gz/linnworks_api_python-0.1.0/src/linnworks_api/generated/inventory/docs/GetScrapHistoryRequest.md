# GetScrapHistoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_number** | **int** |  | [optional] 
**entries_per_page** | **int** |  | [optional] 

## Example

```python
from linnworks_api.generated.inventory.models.get_scrap_history_request import GetScrapHistoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetScrapHistoryRequest from a JSON string
get_scrap_history_request_instance = GetScrapHistoryRequest.from_json(json)
# print the JSON string representation of the object
print(GetScrapHistoryRequest.to_json())

# convert the object into a dict
get_scrap_history_request_dict = get_scrap_history_request_instance.to_dict()
# create an instance of GetScrapHistoryRequest from a dict
get_scrap_history_request_from_dict = GetScrapHistoryRequest.from_dict(get_scrap_history_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


