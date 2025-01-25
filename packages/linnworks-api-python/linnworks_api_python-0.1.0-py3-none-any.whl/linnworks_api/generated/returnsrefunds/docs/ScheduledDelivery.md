# ScheduledDelivery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **datetime** |  | [optional] 
**to** | **datetime** |  | [optional] 

## Example

```python
from linnworks_api.generated.returnsrefunds.models.scheduled_delivery import ScheduledDelivery

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledDelivery from a JSON string
scheduled_delivery_instance = ScheduledDelivery.from_json(json)
# print the JSON string representation of the object
print(ScheduledDelivery.to_json())

# convert the object into a dict
scheduled_delivery_dict = scheduled_delivery_instance.to_dict()
# create an instance of ScheduledDelivery from a dict
scheduled_delivery_from_dict = ScheduledDelivery.from_dict(scheduled_delivery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


