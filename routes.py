from flask import Blueprint, request, jsonify

import services

main = Blueprint('main', __name__)

@main.route('/api/v1/message', methods=['POST'])
def post_message():
    # 바디에서 json 데이터 추출
    data = request.get_json()
    if not data:
        return {"error": "No input data provided"}, 400
    if 'message' not in data:
        return {"error": "'content' field is required"}, 400
    res = services.post_message(data['message'])
    return jsonify(res)


@main.route('/api/v1/user', methods=["POST"])
def create_user():
    user_ip = request.remote_addr
    if request.method == 'POST':
        data = request.get_json()
        return jsonify(services.create_user(user_ip=user_ip, username=data['username']))

@main.route('/api/v1/messages', methods=["POST"])
def get_user_messages():
    user_ip = request.remote_addr
    if request.method == 'POST':
        data = request.get_json()
        messages = services.get_message_by_user(user_ip=user_ip, username=data["username"])
        return[message.to_dict() for message in messages]
