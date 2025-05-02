from flask import request, jsonify, render_template
from .resource_manager import HospitalResourceManager
import numpy as np

manager = HospitalResourceManager(resources=[10, 5, 7])

def init_routes(app):
    @app.route("/allocate", methods=['POST'])
    def allocate():
        data = request.json
        patient_id = data['patient_id']
        request_res = data['request']
        patient_features = data['features']

        success, message = manager.allocate_resources(patient_id, request_res, patient_features)
        status = manager.status()

        return jsonify({
            "success": success,
            "message": message,
            "allocations": status['allocations'],
            "available": status['available']
        })

    @app.route("/emergency", methods=['POST'])
    def emergency():
        data = request.json
        pid = data['patient_id']
        request_res = data['request']
        success, msg = manager.emergency_interrupt(pid, request_res)
        return jsonify({"success": success, "message": msg})

    @app.route("/status", methods=['GET'])
    def status():
        return jsonify(manager.status())

    @app.route('/dashboard')
    def dashboard():
        patient_data = []
        for pid, alloc in manager.allocations.items():
            risk_score = np.random.uniform(0.4, 1.0)
            patient_data.append({
                'name': pid,
                'risk': round(risk_score, 2)
            })
        
        return render_template('dash.html', patients=patient_data, available=manager.available.tolist())
