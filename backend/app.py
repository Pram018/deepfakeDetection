from flask import Flask, render_template
from backend.routes.analysis_routes import analysis_bp


app = Flask(
    __name__,
    template_folder='../frontend/templates',
    static_folder='../frontend/static'
)

app.register_blueprint(analysis_bp)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect')
def detect():
    return render_template('detect.html')

if __name__ == '__main__':
    app.run(debug=True)
