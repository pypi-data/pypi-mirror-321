# OrdersRunRulesEngineRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_ids** | **List[str]** | List of order IDs to run rules on | [optional] 
**rule_id** | **int** | Id of Rule to run. Null if all rules should be run | [optional] 

## Example

```python
from linnworks_api.generated.orders.models.orders_run_rules_engine_request import OrdersRunRulesEngineRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrdersRunRulesEngineRequest from a JSON string
orders_run_rules_engine_request_instance = OrdersRunRulesEngineRequest.from_json(json)
# print the JSON string representation of the object
print(OrdersRunRulesEngineRequest.to_json())

# convert the object into a dict
orders_run_rules_engine_request_dict = orders_run_rules_engine_request_instance.to_dict()
# create an instance of OrdersRunRulesEngineRequest from a dict
orders_run_rules_engine_request_from_dict = OrdersRunRulesEngineRequest.from_dict(orders_run_rules_engine_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


