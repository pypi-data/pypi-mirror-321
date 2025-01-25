# AmazonBNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** |  | [optional] 
**node_path** | **str** |  | [optional] 
**item_type** | **str** |  | [optional] 
**department_name** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.amazon_b_node import AmazonBNode

# TODO update the JSON string below
json = "{}"
# create an instance of AmazonBNode from a JSON string
amazon_b_node_instance = AmazonBNode.from_json(json)
# print the JSON string representation of the object
print(AmazonBNode.to_json())

# convert the object into a dict
amazon_b_node_dict = amazon_b_node_instance.to_dict()
# create an instance of AmazonBNode from a dict
amazon_b_node_from_dict = AmazonBNode.from_dict(amazon_b_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


