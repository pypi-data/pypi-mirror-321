# EmailSent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachment_url** | **str** |  | [optional] [readonly] 
**pk_email_id** | **int** |  | [optional] [readonly] 
**recipient** | **str** |  | [optional] [readonly] 
**send_date** | **datetime** |  | [optional] [readonly] 
**subject** | **str** |  | [optional] [readonly] 
**user_name** | **str** |  | [optional] [readonly] 

## Example

```python
from linnworks_api.generated.purchaseorder.models.email_sent import EmailSent

# TODO update the JSON string below
json = "{}"
# create an instance of EmailSent from a JSON string
email_sent_instance = EmailSent.from_json(json)
# print the JSON string representation of the object
print(EmailSent.to_json())

# convert the object into a dict
email_sent_dict = email_sent_instance.to_dict()
# create an instance of EmailSent from a dict
email_sent_from_dict = EmailSent.from_dict(email_sent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


