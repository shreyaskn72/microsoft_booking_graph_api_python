# Microsoft Bookings API OAuth Authorization Example

This Python script demonstrates how to interact with the Microsoft Bookings API using OAuth authorization.

## Prerequisites

Before running the script, make sure you have the following:

- A Microsoft Azure account
- Microsoft Bookings OAuth client credentials (client ID and client secret)
- Python installed on your system

## Usage

1. **Register Your Application with Microsoft Azure:**
   - Log in to the Azure portal and navigate to the Azure Active Directory.
   - Register a new application and obtain the client ID and client secret.
   - Configure the redirect URL for your application.

2. **Set Up the Script:**
   - Open the `microsoft_bookings_oauth.py` script.
   - Replace `'your_client_id'`, `'your_client_secret'`, and `'https://example.com/oauth/callback'` with your actual client credentials and redirect URL respectively.

3. **Run the Script:**
   - Execute the script using Python:

     ```bash
     python microsoft_bookings_oauth.py
     ```

4. **Authorization Process:**
   - The script will print an authorization URL. Copy this URL and open it in your browser.
   - Follow the prompts to log in to your Microsoft account and authorize your application.
   - After authorization, you will be redirected to the specified redirect URL with an authorization code.
   - Enter the authorization code when prompted by the script.

5. **Obtaining Tokens:**
   - Once the authorization code is entered, the script will exchange it for an access token and refresh token.
   - These tokens will be used to authenticate subsequent requests to the Microsoft Bookings API.

## Notes

- This script demonstrates the OAuth authorization process to obtain access and refresh tokens. In a production environment, you should securely manage these tokens and handle token expiration and refreshing.
- Ensure that your Microsoft Bookings OAuth application is configured with the correct redirect URL and has the necessary permissions to access Microsoft Bookings resources.