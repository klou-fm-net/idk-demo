from aws_cdk import (
    aws_dynamodb as db,
    aws_ssm as ssm
)

def create_dynamodb_table(scope) :
    db_table = db.Table(
        scope, 
        "DemoTable",
        partition_key = db.Attribute(name = "bookName", type = db.AttributeType.STRING),
        billing_mode = db.BillingMode.PAY_PER_REQUEST,
    )

    ssm.StringParameter(scope, "DynamoTableNameParam",
        parameter_name="/config/dynamoTableName",
        string_value=db_table.table_name
    )

    return db_table