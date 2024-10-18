# Microsoft Graph API Access Token Retrieval from Refresh Token

This Python script demonstrates how to obtain a new access token from a refresh token using the Azure Active Directory (Azure AD) token endpoint. The refreshed access token can be used to authenticate requests to the Microsoft Graph API or other protected resources.

## Requirements

- Python 3.x
- `requests` library (install via `pip install requests`)

## Usage

1. Clone or download the provided Python script.

2. Update the following variables in the script with your Azure AD application details:
   - `TENANT_ID`: Your Azure AD tenant ID.
   - `CLIENT_ID`: Your Azure AD application (client) ID.
   - `CLIENT_SECRET`: Your Azure AD application client secret.
   - `REFRESH_TOKEN`: The refresh token obtained earlier.

3. Run the Python script in your terminal or command prompt.

4. Upon successful execution, the script will retrieve a new access token using the provided refresh token.

## Script Explanation

- The script sends a POST request to the Azure AD token endpoint (`TOKEN_URL`) with the provided refresh token and other required parameters.

- The response from the token endpoint contains several parameters:
  - `token_type`: The type of token returned.
  - `expires_in`: The duration for which the access token is valid.
  - `access_token`: The new access token.
  - `scope`: The scope of the access token.
  - `refresh_token`: A new refresh token (if provided).
  - `id_token`: Identity token for the authenticated user (if applicable).
  - `not_before`: The earliest time at which the token can be used.
  - `expires_on`: The expiration time of the access token.
  - `resource`: The resource identifier for the token.

- These parameters are crucial for authentication and authorization when interacting with the Microsoft Graph API or other protected resources.

## Response Parameters

- `token_type`: The type of token returned. Typically, it's `"Bearer"` for OAuth 2.0 tokens.

- `expires_in`: The duration, in seconds, for which the access token is valid.

- `access_token`: The new access token that can be used to authenticate requests to the Microsoft Graph API.

- `scope`: The scope of the access token.

- `refresh_token`: A new refresh token that can be used to obtain another access token when the current access token expires.

- `id_token`: Identity token for the authenticated user (if applicable).

- `not_before`: The earliest time at which the token can be used.

- `expires_on`: The expiration time of the access token.

- `resource`: The resource identifier for the token.

## Note

- Ensure that your application securely handles the obtained access and refresh tokens. Protect these tokens as sensitive information and avoid hardcoding them in your application source code.