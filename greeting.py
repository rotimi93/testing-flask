from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/getmsg/', methods=['GET'])
def respond():
	name = request.args.get('name', None)
	print(f"Received: {name}")

	response = {}

	if not name:
		response['ERROR'] = "No name found. Please send a name."
	elif str(name).isdigit():
		response["ERROR"] = 'The name cant be  numeric. Please send a string'
	else:
		response["MESSAGE"] = f"Welcome {name} to our awesome API."

	return jsonify(response)

@app.route('/post/', methods=["POST"])
def post_something():
	param = request.form.get('name')
	print(param)

	if param:
		return jsonify({
			"Message":f"Welcome {name} to our awesome API",
			"Method":"POST"
		})
	else:
		return jsonify({
			"ERROR": "No name found. Please send a name"
		})

@app.route('/')
def index():
	return "<h1>Welcome to our medium-greeting-api</h1>"

if __name__ == '__main__':
	app.run(threaded=True, port=5000)

