from tortoise import fields, models


class User(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=10, description="Name user")
    last_name = fields.CharField(max_length=10, description="Last name user")
    email = fields.CharField(max_length=30, description="Email user")
    hashed_password = fields.CharField(max_length=200, null=True)
    username = fields.CharField(max_length=50, null=True)

    class Meta:
        table = "user"

    def __str__(self):
        return f'{self.name} {self.last_name}'
