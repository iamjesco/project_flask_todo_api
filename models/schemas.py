from app import ma


class TodoSchema(ma.Schema):
	class Meta:
		ordered = True
		fields = ('pk', 'body', 'created', 'updated')


todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)