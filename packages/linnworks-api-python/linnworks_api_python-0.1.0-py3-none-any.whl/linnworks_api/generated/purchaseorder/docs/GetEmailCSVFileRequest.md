# GetEmailCSVFileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk_purchase_id** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.get_email_csv_file_request import GetEmailCSVFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetEmailCSVFileRequest from a JSON string
get_email_csv_file_request_instance = GetEmailCSVFileRequest.from_json(json)
# print the JSON string representation of the object
print(GetEmailCSVFileRequest.to_json())

# convert the object into a dict
get_email_csv_file_request_dict = get_email_csv_file_request_instance.to_dict()
# create an instance of GetEmailCSVFileRequest from a dict
get_email_csv_file_request_from_dict = GetEmailCSVFileRequest.from_dict(get_email_csv_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


