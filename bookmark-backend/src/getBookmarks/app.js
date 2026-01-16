const AWS = require('aws-sdk');

const dynamoDB = new AWS.DynamoDB.DocumentClient();
const TABLE_NAME = process.env.TABLE_NAME;

exports.handler = async (event) => {
  try {
    const requestId = event.requestContext.requestId;
    const userId = event.requestContext.authorizer.claims.sub;

    console.log(JSON.stringify({
      level: 'INFO',
      message: 'Fetching bookmarks',
      userId,
      requestId,
      timestamp: new Date().toISOString()
    }));

    const result = await dynamoDB.query({
      TableName: TABLE_NAME,
      KeyConditionExpression: 'userId = :uid',
      ExpressionAttributeValues: {
        ':uid': userId
      }
    }).promise();

    console.log(JSON.stringify({
      level: 'INFO',
      message: 'Bookmarks fetched successfully',
      userId,
      count: result.Items.length,
      requestId,
      timestamp: new Date().toISOString()
    }));

    return {
      statusCode: 200,
      body: JSON.stringify(result.Items)
    };

  } catch (error) {
    const requestId = event.requestContext?.requestId || 'unknown';
    const userId = event.requestContext?.authorizer?.claims?.sub || 'unknown';
    console.log(JSON.stringify({
      level: 'ERROR',
      message: 'Error fetching bookmarks',
      error: error.message,
      userId,
      requestId,
      timestamp: new Date().toISOString()
    }));
    return {
      statusCode: 500,
      body: JSON.stringify({ message: 'Internal Server Error' })
    };
  }
};
