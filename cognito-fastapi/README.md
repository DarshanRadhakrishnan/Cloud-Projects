# AWS Cognito + FastAPI Secure Backend

This project demonstrates a **cloud-native authentication and authorization architecture** using **AWS Cognito** and **FastAPI**, following real-world backend best practices. Authentication is delegated to AWS Cognito, while FastAPI acts as a protected **resource server** that verifies JWT tokens and serves authorized APIs.

---

## Key Features

- AWS Cognito Hosted UI for login and signup
- JWT-based stateless authentication
- FastAPI dependency-based authorization
- Secure token verification using Cognito JWKS
- DynamoDB for application data storage
- No password handling in the backend
- Clean separation of concerns

---

## Architecture Overview

![Architecture Diagram](docs/architecture.png)

### High-Level Flow

1. The user authenticates via **AWS Cognito Hosted UI**
2. Cognito validates credentials and issues **JWT tokens**
3. The client sends API requests with the token in the `Authorization` header
4. FastAPI verifies the token before executing protected endpoints
5. Authorized requests access DynamoDB-backed resources

---

## Authentication Flow (Step-by-Step)

### 1. User Login (Cognito Hosted UI)

- AWS Cognito provides a **hosted login and signup interface**
- The login UI is **not part of this repository**
- Authentication happens **outside the backend**

```
Client → Cognito Hosted UI → Login
```

### 2. Token Issuance

After successful authentication, Cognito issues:

- **Access Token**
- **ID Token**
- **(Optional) Refresh Token**

All tokens are signed using **RS256 (asymmetric encryption)**.

### 3. API Request with Token

The client sends requests to the backend with the access token:

```http
Authorization: Bearer <access_token>
```

### 4. Token Verification (Before Endpoint Execution)

Before executing a protected endpoint:

1. FastAPI extracts the token from the request
2. The token is verified using Cognito public keys (JWKS)
3. Token claims are validated (issuer, audience, expiration)
4. Only after successful validation is the endpoint executed

---

## Is Authentication Implemented as Middleware?

**No.** Authentication is implemented using **FastAPI dependencies**, not middleware.

### Reasoning

- **Middleware** executes for every request
- **Dependencies** execute only for routes that declare them
- Provides fine-grained control over protected vs public endpoints
- This approach follows FastAPI's recommended design pattern

---

## Why AWS Cognito Instead of Traditional JWT Libraries?

### Traditional JWT Approach (Avoided)

- Backend stores and verifies passwords
- Backend signs and manages JWT tokens
- Manual key rotation
- Custom MFA and account recovery logic
- This increases security risk and maintenance complexity

### AWS Cognito Approach (Used)

AWS Cognito acts as a **managed identity provider**. It handles:

- Password storage and hashing
- Email verification
- Multi-factor authentication (MFA)
- Account recovery
- Token issuance
- Key rotation

The backend:

- Never handles credentials
- Never generates tokens
- Only verifies tokens

This enforces **separation of concerns**.

---

## Why Not Cookie-Based JWT Authentication?

This project uses **Authorization header–based JWTs**, not cookies.

### Reasons

- Avoids CSRF vulnerabilities
- Fully stateless
- Works across:
  - Web applications
  - Mobile applications
  - CLI tools
- Cloud and microservice friendly
- Easier horizontal scaling

This is the recommended approach for API-based systems.

---

## Project Structure and File Responsibilities

```
backend/
│
├── .env
├── requirements.txt
└── app/
    ├── main.py
    ├── auth/
    │   ├── cognito.py
    │   └── dependencies.py
    ├── routes/
    │   ├── users.py
    │   └── items.py
    └── services/
        └── dynamodb.py
```

### `.env`

Stores environment-specific configuration:

- AWS region
- Cognito User Pool ID
- Cognito App Client ID
- DynamoDB table name

### `main.py`

Application entry point:

- Loads environment variables
- Creates FastAPI application instance
- Registers route modules

**Note:** `main.py` does not perform authentication.

### `auth/cognito.py`

- Constructs Cognito issuer and JWKS URLs
- Fetches Cognito public keys
- Verifies JWT signatures and claims

This file validates tokens, not credentials.

### `auth/dependencies.py`

- Extracts JWT from the `Authorization` header
- Invokes token verification
- Injects authenticated user into protected routes

### `routes/`

Defines API endpoints:

- `users.py` → user-related endpoints
- `items.py` → business logic endpoints

Each protected route explicitly declares an authentication dependency.

### `services/dynamodb.py`

- Manages DynamoDB connection
- Provides table access to route handlers

---

## How Authentication Is Enforced

Authentication is enforced **at request time**, not during application startup.

```
HTTP Request
     ↓
FastAPI Router
     ↓
Authentication Dependency
     ↓
Endpoint Logic
```

Public routes remain accessible without authentication.

---

## Deployment Notes

- AWS Cognito User Pool and DynamoDB table are created manually
- Backend is deployed independently (e.g., EC2)
- Authentication UI is hosted and managed by AWS Cognito

---

## Security Considerations

- JWTs use **RS256 asymmetric signing**
- Private signing keys remain with AWS Cognito
- Backend only uses public keys
- No session storage
- No password exposure

---

## Summary

| Component | Role |
|-----------|------|
| **AWS Cognito** | Identity Provider |
| **FastAPI** | Resource Server |
| **JWT** | Stateless Authorization |
| **DynamoDB** | Application Storage |
| **Hosted UI** | Secure, managed authentication interface |

This architecture closely mirrors production-grade cloud systems.

---

## Future Improvements

- Role-based access control using Cognito groups
- Refresh token handling
- S3 integration with signed URLs
- Infrastructure automation using AWS CDK
- CI/CD pipeline integration

---

## Author Notes

This project focuses on secure authentication design, cloud best practices, and clean architectural separation, rather than frontend implementation.
