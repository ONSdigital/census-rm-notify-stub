# census-rm-notify-stub

Provides a way of testing the census-rm-notify-processor without using the real GOV NOTIFY service.


## API

### GOV.UK Notify Endpoints

#### `POST /gov_notify_api/v2/notifications/sms`
This endpoint receives _send sms_ requests for the official GOV.UK Notify API and stores them in memory.

### Programatic Endpoints

#### `GET /log`
Get all sms requests that have been submitted.

#### `GET /reset`
Clears all sms requests.