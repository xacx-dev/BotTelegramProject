from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator
class tokens(models.Model):
    """
    The tokens model
    """

    id = fields.IntField(pk=True)
    idinmain = fields.IntField()
    telegramid = fields.IntField(unique=True)
    token = fields.TextField()


token_Pydantic = pydantic_model_creator(tokens, name="token")
tokenIn_Pydantic = pydantic_model_creator(tokens, name="tokenIn", exclude_readonly=True)