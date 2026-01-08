# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)


## Why AWS Amplify and Its Role in the Frontend

AWS Amplify is a frontend development platform that simplifies the integration of web applications with AWS services. In this project, AWS Amplify is used to bridge the gap between the React frontend and the serverless backend deployed using AWS SAM.

### Why AWS Amplify Was Used

The frontend of this application requires secure user authentication, token management, and seamless communication with protected backend APIs. Implementing these features manually would require significant effort and could introduce security risks. AWS Amplify was chosen because it provides a high-level abstraction for frontend developers, enabling secure and scalable integration with AWS services without handling low-level configurations.

### Role of AWS Amplify in This Project

AWS Amplify performs the following key functions in the application:

- **Authentication Management**  
  Amplify configures and integrates Amazon Cognito User Pools to provide user sign-up and sign-in functionality. It manages password handling, validation, and secure authentication workflows automatically.

- **Token Handling and Session Management**  
  After successful authentication, Amplify securely stores JSON Web Tokens (JWTs) in the browser and automatically refreshes them when required. This ensures that authenticated sessions remain valid without manual intervention.

- **Secure API Access**  
  Amplify enables the React frontend to retrieve authentication tokens and attach them to HTTP requests sent to the backend APIs. These tokens are used by Amazon API Gateway to authenticate requests before invoking AWS Lambda functions.

- **Simplified Frontend–Backend Integration**  
  Amplify generates configuration files (such as `aws-exports.js`) that allow the frontend application to communicate with AWS resources using correct region and service identifiers. This removes the need for hard-coded credentials or manual AWS SDK configuration.

### Summary

AWS Amplify is used in this project to simplify frontend development while maintaining strong security and scalability. It abstracts authentication complexity, securely manages user sessions, and enables the React frontend to interact with a Cognito-protected serverless backend in a clean and maintainable manner.
