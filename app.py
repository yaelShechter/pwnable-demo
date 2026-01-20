from flask import Flask, render_template, Response, stream_with_context
import json
from challenges import CHALLENGES
from exploits import EXPLOIT_FUNCTIONS

app = Flask(__name__)

def generate_exploit_stream(challenge_id):
    """Generate exploit stream for given challenge"""
    if challenge_id not in CHALLENGES:
        yield f"data: {json.dumps({'type': 'error', 'message': 'Challenge not found'})}\n\n"
        return
    
    challenge_config = CHALLENGES[challenge_id]
    exploit_func = EXPLOIT_FUNCTIONS.get(challenge_id)
    
    if not exploit_func:
        yield f"data: {json.dumps({'type': 'error', 'message': 'Exploit not implemented'})}\n\n"
        return
    
    yield from exploit_func(challenge_config)

@app.route('/')
def index():
    return render_template('index.html', challenges=CHALLENGES)

@app.route('/stream_exploit/<challenge_id>')
def stream_exploit(challenge_id):
    return Response(stream_with_context(generate_exploit_stream(challenge_id)), 
                   mimetype='text/event-stream',
                   headers={'Cache-Control': 'no-cache',
                           'X-Accel-Buffering': 'no'})

if __name__ == '__main__':
    app.run(debug=True, port=5000, threaded=True)