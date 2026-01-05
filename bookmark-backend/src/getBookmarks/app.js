const AWS = require('aws-sdk');

const dynamoDB = new AWS.DynamoDB.DocumentClient();
const TABLE_NAME = process.env.TABLE_NAME;

exports.handler = async (event) => {
  try {
    // Get authenticated user ID
    const userId = event.requestContext.authorizer.claims.sub;

    const result = await dynamoDB.query({
      TableName: TABLE_NAME,
      KeyConditionExpression: 'userId = :uid',
      ExpressionAttributeValues: {
        ':uid': userId
      }
    }).promise();

    return {
      statusCode: 200,
      body: JSON.stringify(result.Items)
    };

  } catch (error) {
    console.error(error);
    return {
      statusCode: 500,
      body: JSON.stringify({ message: 'Internal Server Error' })
    };
  }
};
