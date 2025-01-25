# GetViewMetaDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prep_owners** | [**List[Int32StringKeyValuePair]**](Int32StringKeyValuePair.md) |  | [optional] 
**label_owners** | [**List[Int32StringKeyValuePair]**](Int32StringKeyValuePair.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.warehousetransfer_v2.models.get_view_meta_data_response import GetViewMetaDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetViewMetaDataResponse from a JSON string
get_view_meta_data_response_instance = GetViewMetaDataResponse.from_json(json)
# print the JSON string representation of the object
print(GetViewMetaDataResponse.to_json())

# convert the object into a dict
get_view_meta_data_response_dict = get_view_meta_data_response_instance.to_dict()
# create an instance of GetViewMetaDataResponse from a dict
get_view_meta_data_response_from_dict = GetViewMetaDataResponse.from_dict(get_view_meta_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


