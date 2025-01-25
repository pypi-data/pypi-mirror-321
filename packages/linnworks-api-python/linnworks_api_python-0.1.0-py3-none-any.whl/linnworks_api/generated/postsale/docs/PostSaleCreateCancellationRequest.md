# PostSaleCreateCancellationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**CancellationRequest**](CancellationRequest.md) |  | [optional] 

## Example

```python
from linnworks_api.generated.postsale.models.post_sale_create_cancellation_request import PostSaleCreateCancellationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSaleCreateCancellationRequest from a JSON string
post_sale_create_cancellation_request_instance = PostSaleCreateCancellationRequest.from_json(json)
# print the JSON string representation of the object
print(PostSaleCreateCancellationRequest.to_json())

# convert the object into a dict
post_sale_create_cancellation_request_dict = post_sale_create_cancellation_request_instance.to_dict()
# create an instance of PostSaleCreateCancellationRequest from a dict
post_sale_create_cancellation_request_from_dict = PostSaleCreateCancellationRequest.from_dict(post_sale_create_cancellation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


