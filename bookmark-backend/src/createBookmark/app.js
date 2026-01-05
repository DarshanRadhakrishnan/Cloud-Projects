const AWS = require('aws-sdk');
const { v4: uuidv4 } = require('uuid');

const dynamoDB = new AWS.DynamoDB.DocumentClient();
const TABLE_NAME = process.env.TABLE_NAME;

exports.handler = async (event) => {
  try {
    // Get authenticated user ID from Cognito
    const userId = event.requestContext.authorizer.claims.sub;

    // Parse request body
    const body = JSON.parse(event.body);
    const { url, title, notes } = body;

    if (!url || !title) {
      return {
        statusCode: 400,
        body: JSON.stringify({ message: 'url and title are required' })
      };
    }

    const bookmark = {
      userId,
      bookmarkId: uuidv4(),
      url,
      title,
      notes: notes || '',
      createdAt: new Date().toISOString()
    };

    await dynamoDB.put({
      TableName: TABLE_NAME,
      Item: bookmark
    }).promise();

    return {
      statusCode: 201,
      body: JSON.stringify(bookmark)
    };

  } catch (error) {
    console.error(error);
    return {
      statusCode: 500,
      body: JSON.stringify({ message: 'Internal Server Error' })
    };
  }
};
