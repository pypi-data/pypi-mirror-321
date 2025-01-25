# PostSaleStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_header** | **str** |  | [optional] 
**status_detail** | [**PostSaleSubStatus**](PostSaleSubStatus.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.postsale.models.post_sale_status import PostSaleStatus

# TODO update the JSON string below
json = "{}"
# create an instance of PostSaleStatus from a JSON string
post_sale_status_instance = PostSaleStatus.from_json(json)
# print the JSON string representation of the object
print(PostSaleStatus.to_json())

# convert the object into a dict
post_sale_status_dict = post_sale_status_instance.to_dict()
# create an instance of PostSaleStatus from a dict
post_sale_status_from_dict = PostSaleStatus.from_dict(post_sale_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


