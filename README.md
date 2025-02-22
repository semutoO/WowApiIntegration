# World of Warcraft Api Integration
This Python code provides two controllers that will call the Blizzard World of Warcraft API.

## Requirements

You'll need to visit the [Blizzard's Developer Portal](https://develop.battle.net/documentation/guides) website to create your own client for their APIs. 

Follow their documentation on creating your Client Id and Client Secret and add them to the [WowApiConfig.json](wowApiConfig.json). 

## Making API calls
To call an endpoint, use the functions off of either [WowGameDataController.py](WowApiIntegration/Controllers/WowGameDataController.py) or [WowCharacterProfileController.py](WowApiIntegration/Controllers/WowCharacterProfileController.py).

Each call will also add your client id and client secret to the authentication header.

In the event that Blizzard changes their endpoint address or parts of the request objects, users should be able to pass in these properties to the request object to be consumed and added to the urlParams in the [WowApiInvoker.py](WowApiIntegration/AppServices/WowApiInvoker.py)

## Responses
Responses will return the body's content as JSON from the API call.
