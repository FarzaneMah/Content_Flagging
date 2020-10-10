# Extracting YouTube Comments with YouTube API & Python
To access the YouTube Data API, you need to have a project on Google Console. This is because you need to obtain authorization credentials to make API calls in your application.
1. Create a new project on Google Console. 
2. Enable API and services on your project. 
3. Setup credentials and download the .json file. 
4. Install Google API client library. 
```
pip install google-api-python-client
```
5. Install additional libraries which will handle authentication
```
pip install google-auth google-auth-oauthlib google-auth-httplib2
```
6. Strict the scope of Google API to youtube (this is part of the code).
7. Run the "Youtube_Scraping" jupyter notebook and follow the steps there.

For more detailed information visit https://python.gotrained.com/youtube-api-extracting-comments/
