# GetWarehouseTotesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**totes** | [**List[WarehouseTOTE]**](WarehouseTOTE.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.locations.models.get_warehouse_totes_response import GetWarehouseTotesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWarehouseTotesResponse from a JSON string
get_warehouse_totes_response_instance = GetWarehouseTotesResponse.from_json(json)
# print the JSON string representation of the object
print(GetWarehouseTotesResponse.to_json())

# convert the object into a dict
get_warehouse_totes_response_dict = get_warehouse_totes_response_instance.to_dict()
# create an instance of GetWarehouseTotesResponse from a dict
get_warehouse_totes_response_from_dict = GetWarehouseTotesResponse.from_dict(get_warehouse_totes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


