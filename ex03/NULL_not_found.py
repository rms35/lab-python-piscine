def	NULL_not_found(object: any) -> int:
	r = type(object)
	try:
		if r is None:
			print("{None}: ", {type(object)})
		elif isinstance(object, ):
			pass
		else:
			print("asd")
	except Exception as e:
		print("Error: {e}")
		return 1
	return 0