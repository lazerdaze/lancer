class CustomError(Exception):
	pass


class NodeExistsError(CustomError):
	pass


class NodeTypeError(CustomError):
	pass


class AttributeExistsError(CustomError):
	pass


class ConnectionError(CustomError):
	pass


class ConstraintError(CustomError):
	pass


class PluginError(CustomError):
	pass