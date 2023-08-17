from flask import Flask, render_template
import yaml
import subprocess

app = Flask(__name__)

@app.route('/home')
def handle():
    try:
        data = {}
        with open('data.yaml', 'r') as file:
            data = yaml.safe_load(file)
        return render_template("index.html", data=data['content'])
    except Exception as e:
        return(str(e))

# @webhook.hook()        # Defines a handler for the 'push' event
# def on_push(data):
#     print(f"Got push with: {json.dumps(data, indent=4)}")
#     bashCommand = "cwm --rdf test.rdf --ntriples > test.nt"
#     devnull = open(os.devnull, 'wb') # Use this in Python < 3.3
#     Popen(['nohup', 'update.sh'], stdout=devnull, stderr=devnull)
#     exit(0)

if __name__ == '__main__':
    app.run(threaded=True, port=10000)

