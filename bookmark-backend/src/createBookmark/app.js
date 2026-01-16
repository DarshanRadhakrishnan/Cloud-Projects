const AWS = require('aws-sdk');
const { v4: uuidv4 } = require('uuid');

const dynamoDB = new AWS.DynamoDB.DocumentClient();
const TABLE_NAME = process.env.TABLE_NAME;

exports.handler = async (event) => {
  try {
    const requestId = event.requestContext.requestId;
    const userId = event.requestContext.authorizer.claims.sub;

    console.log(JSON.stringify({
      level: 'INFO',
      message: 'Creating bookmark',
      userId,
      requestId,
      timestamp: new Date().toISOString()
    }));

    // Parse request body
    const body = JSON.parse(event.body);
    const { url, title, notes } = body;

    if (!url || !title) {
      console.log(JSON.stringify({
        level: 'WARN',
        message: 'Missing required fields',
        userId,
        requestId,
        timestamp: new Date().toISOString()
      }));
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

    console.log(JSON.stringify({
      level: 'INFO',
      message: 'Bookmark created successfully',
      userId,
      bookmarkId: bookmark.bookmarkId,
      requestId,
      timestamp: new Date().toISOString()
    }));

    return {
      statusCode: 201,
      body: JSON.stringify(bookmark)
    };

  } catch (error) {
    const requestId = event.requestContext?.requestId || 'unknown';
    const userId = event.requestContext?.authorizer?.claims?.sub || 'unknown';
    console.log(JSON.stringify({
      level: 'ERROR',
      message: 'Error creating bookmark',
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
