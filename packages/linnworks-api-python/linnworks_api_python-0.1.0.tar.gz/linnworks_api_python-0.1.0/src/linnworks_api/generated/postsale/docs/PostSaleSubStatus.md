# PostSaleSubStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_tag** | **str** |  | [optional] 
**status_description** | **str** |  | [optional] 
**actionable** | **bool** |  | [optional] 
**action_description** | **str** |  | [optional] 
**editable_fields** | **List[str]** |  | [optional] 

## Example

```python
from linnworks_api.generated.postsale.models.post_sale_sub_status import PostSaleSubStatus

# TODO update the JSON string below
json = "{}"
# create an instance of PostSaleSubStatus from a JSON string
post_sale_sub_status_instance = PostSaleSubStatus.from_json(json)
# print the JSON string representation of the object
print(PostSaleSubStatus.to_json())

# convert the object into a dict
post_sale_sub_status_dict = post_sale_sub_status_instance.to_dict()
# create an instance of PostSaleSubStatus from a dict
post_sale_sub_status_from_dict = PostSaleSubStatus.from_dict(post_sale_sub_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


