def	NULL_not_found(object: any) -> int:
	r = None
	try:
		match object:
			case None:
				r = 'Nothing: '
			case float() if object != object:
				r = 'Cheese: '
			case bool() if object is False:
				r = 'Fake: '
			case int() if object == 0:
				r = 'Zero: '
			case str() if not object:
				r = 'Empty: '
			case _:
				print('Type not found')
				return 1
		if r is not None:
			print(f'{r} {object} {type(object)}')
	except Exception as e:
		print("Error: {e}")
		return 1
	return 0