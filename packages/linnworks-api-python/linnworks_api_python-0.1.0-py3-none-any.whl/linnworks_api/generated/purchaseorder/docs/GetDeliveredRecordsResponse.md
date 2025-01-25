# GetDeliveredRecordsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CommonPurchaseOrderDeliveredRecord]**](CommonPurchaseOrderDeliveredRecord.md) |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.get_delivered_records_response import GetDeliveredRecordsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDeliveredRecordsResponse from a JSON string
get_delivered_records_response_instance = GetDeliveredRecordsResponse.from_json(json)
# print the JSON string representation of the object
print(GetDeliveredRecordsResponse.to_json())

# convert the object into a dict
get_delivered_records_response_dict = get_delivered_records_response_instance.to_dict()
# create an instance of GetDeliveredRecordsResponse from a dict
get_delivered_records_response_from_dict = GetDeliveredRecordsResponse.from_dict(get_delivered_records_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


