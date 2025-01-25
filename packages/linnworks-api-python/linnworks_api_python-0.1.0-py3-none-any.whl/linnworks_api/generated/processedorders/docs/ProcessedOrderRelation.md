# ProcessedOrderRelation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_order_pk_order_id** | **str** |  | [optional] 
**child_order_pk_order_id** | **str** |  | [optional] 
**parent_order_id** | **int** |  | [optional] 
**child_order_id** | **int** |  | [optional] 
**relation_type** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.processedorders.models.processed_order_relation import ProcessedOrderRelation

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessedOrderRelation from a JSON string
processed_order_relation_instance = ProcessedOrderRelation.from_json(json)
# print the JSON string representation of the object
print(ProcessedOrderRelation.to_json())

# convert the object into a dict
processed_order_relation_dict = processed_order_relation_instance.to_dict()
# create an instance of ProcessedOrderRelation from a dict
processed_order_relation_from_dict = ProcessedOrderRelation.from_dict(processed_order_relation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


