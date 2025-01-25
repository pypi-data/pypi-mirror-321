# Consignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consignment_id** | **int** |  | [optional] 
**order_id** | **int** |  | [optional] 
**customer** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**weight** | **float** |  | [optional] 
**tracking_numbers** | **List[str]** |  | [optional] 
**packages** | **int** |  | [optional] 
**consignment_packages** | [**List[ManifestPackage]**](ManifestPackage.md) |  | [optional] 
**properties** | [**List[ServiceProperty]**](ServiceProperty.md) |  | [optional] 
**deferred** | **bool** |  | [optional] 
**service** | **str** |  | [optional] 

## Example

```python
from linnworks_api.generated.shippingservice.models.consignment import Consignment

# TODO update the JSON string below
json = "{}"
# create an instance of Consignment from a JSON string
consignment_instance = Consignment.from_json(json)
# print the JSON string representation of the object
print(Consignment.to_json())

# convert the object into a dict
consignment_dict = consignment_instance.to_dict()
# create an instance of Consignment from a dict
consignment_from_dict = Consignment.from_dict(consignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


