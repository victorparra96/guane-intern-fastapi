from tortoise import fields, models


class Dog(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=10, description="Name dog")
    picture = fields.CharField(
        max_length=200,
        description="Picture dog",
        null=True)
    is_adopted = fields.BooleanField(default=True)
    create_date = fields.DatetimeField(auto_now_add=True)
    idUser = fields.ForeignKeyField(
        "models.User", related_name="user"
    )

    class Meta:
        table = "dog"

    def __str__(self):
        return self.name
