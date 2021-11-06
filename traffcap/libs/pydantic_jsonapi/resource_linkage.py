from typing import Optional, Union, List

from pydantic import BaseModel

from traffcap.libs.pydantic_jsonapi.resource_identifier import ResourceIdentifier

ResourceLinkage = Optional[Union[ResourceIdentifier, List[ResourceIdentifier]]]
ResourceLinkage.__doc__ = "https://jsonapi.org/format/#document-resource-object-linkage"
