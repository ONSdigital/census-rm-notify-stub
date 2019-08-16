import json
import uuid

from flask import Flask, request, Response

app = Flask(__name__)

sms_requests = []


@app.route('/v2/notifications/sms', methods=['POST'])
def send_sms():
    data = json.loads(request.data)

    sms_requests.append(data)

    template_id = 'https://api.notifications.service.gov.uk/templates/' + \
                  data["template_id"]

    response = {'id': str(uuid.uuid4()),
                'reference': data['reference'],
                'template': {
                    'version': 1,
                    'id': data['template_id'],
                    'uri': template_id},
                'content': {
                    'body': json.dumps(data),
                    'from_number': '1234'}
                }

    return Response(response=json.dumps(response),
                    status=201, mimetype='application/json')


@app.route('/log', methods=['GET'])
def get_sms():
    return json.dumps(sms_requests), 200


@app.route('/reset', methods=['GET'])
def reset():
    sms_requests.clear()
    return {}, 200


if __name__ == '__main__':
    app.run(host="0.0.0.0")
