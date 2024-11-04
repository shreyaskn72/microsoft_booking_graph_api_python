# Microsoft Graph API to fetch user info based on access token
This script demonstrates how to use the Microsoft Graph API to retrieve user information from the `https://graph.microsoft.com/oidc/userinfo` endpoint using an access token.

## Prerequisites

- Python 3.x
- `requests` library (install via `pip install requests`)
- Azure AD App Registration:
  - **Client ID**
  - **Client Secret**
  - **Tenant ID**
  - Necessary API permissions (e.g., `openid`, `profile`)

## Usage

1. Clone or download the provided Python script.

2. Update the following variables in the script with your Azure AD application details:
   - `TENANT_ID`: Your Azure AD tenant ID.
   - `CLIENT_ID`: Your Azure AD application (client) ID.
   - `CLIENT_SECRET`: Your Azure AD application client secret.
   - `microsoft_access_token`: The microsoft_access_token obtained from step1 and step1.

3. Run the Python script in your terminal or command prompt.

### Description

This function retrieves user information from the Microsoft Graph API using a valid OAuth 2.0 access token.

Here's a detailed explanation of the typical response from the `https://graph.microsoft.com/oidc/userinfo` endpoint, along with the structure and meaning of the response fields:

### Response Structure

When you successfully call the `get_logged_in_user_details` function, the response from the Microsoft Graph API will generally be a JSON object containing user claims. Here’s an example response and its explanation:

```json
{
    "sub": "1234567890",
    "name": "John Doe",
    "preferred_username": "johndoe@example.com",
    "given_name": "John",
    "family_name": "Doe",
    "email": "johndoe@example.com",
    "groups": [
        "group1",
        "group2"
    ],
    "upn": "johndoe@example.com"
}
```

### Response Fields Explained

- **`sub`**: (string) The unique identifier for the user in the directory. This is typically used as the subject identifier.

- **`name`**: (string) The full name of the user as displayed in the directory.

- **`preferred_username`**: (string) The preferred username of the user, often their email address or another identifier that the user prefers.

- **`given_name`**: (string) The first name of the user.

- **`family_name`**: (string) The last name of the user.

- **`email`**: (string) The user's email address. Note that this may be included based on the permissions granted.

- **`groups`**: (array of strings) A list of groups that the user belongs to, if the token includes group claims. This requires specific permissions.

- **`upn`**: (string) The User Principal Name (UPN), which is usually the user's email address in Azure AD.



### Error Responses

If there is an error, the API will typically return a response with a status code other than 200. The error response may look like this:

```json
{
    "error": {
        "code": "InvalidAuthenticationToken",
        "message": "Access token is invalid.",
        "innerError": {
            "request-id": "abcdefgh-ijkl-mnop-qrst-uvwxyz123456",
            "date": "2024-11-04T12:00:00"
        }
    }
}
```

#### Error Fields Explained

- **`error`**: An object containing error details.
  - **`code`**: (string) A specific error code indicating the type of error.
  - **`message`**: (string) A human-readable description of the error.
  - **`innerError`**: (object) Additional error information, including:
    - **`request-id`**: (string) The unique identifier for the request, useful for debugging.
    - **`date`**: (string) The timestamp of the error occurrence.

