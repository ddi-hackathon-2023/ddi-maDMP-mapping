class DuplicateMappingSchema(Exception):
   """Raised when more than one Mapping Schema have the same identifier"""
   pass


class MissingMappingSchema(Exception):
   """Raised when Mapping Schema is not found with an identifier"""
   pass


class MissingDefaultValue(Exception):
   """Raised when expecting a defaul value, but none is provided"""
   pass


class NotAnArray(Exception):
   """Raised when content of a node is expected to be an array, but is not"""
   pass


class MissingMappingMethod(Exception):
   """Raised when a mapping method cannot be found"""
   pass
