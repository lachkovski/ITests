from flask import Flask # type: ignore # type: igonre
app = Flask(__name__)
@app.route('/')
def home():
   return "Hello, Kubernetes!"
if __name__ == "__main__":
 app.run(host='0.0.0.0', port=5000)