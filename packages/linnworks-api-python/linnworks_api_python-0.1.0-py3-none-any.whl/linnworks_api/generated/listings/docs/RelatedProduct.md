# RelatedProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **str** |  | [optional] 
**product_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**link_assigned** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.listings.models.related_product import RelatedProduct

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedProduct from a JSON string
related_product_instance = RelatedProduct.from_json(json)
# print the JSON string representation of the object
print(RelatedProduct.to_json())

# convert the object into a dict
related_product_dict = related_product_instance.to_dict()
# create an instance of RelatedProduct from a dict
related_product_from_dict = RelatedProduct.from_dict(related_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


