from flask import Flask
import subprocess
import time
import os

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Muskan Gupta"
    username = os.getlogin()
    
    # Get server time in IST
    ist_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    
    # Get top command output
    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    
    return f"""
    <h3>Name: {name}</h3>
    <h3>Username: {username}</h3>
    <h3>Server Time (IST): {ist_time}</h3>
    <pre>TOP OUTPUT: {top_output}</pre>
    """
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
