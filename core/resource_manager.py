import numpy as np
import threading
from .model import classify_risk

class HospitalResourceManager:
    def __init__(self, resources):
        self.total = np.array(resources)
        self.available = self.total.copy()
        self.allocations = {}
        self.lock = threading.Lock()

    def allocate_resources(self, patient_id, request, patient_data):
        with self.lock:
            request = np.array(request)
            if any(request > self.available):
                return False, "Insufficient resources"

            risk = classify_risk(patient_data)
            if risk == 1:  # High risk
                self.available -= request
                self.allocations[patient_id] = request
                return True, f"Resources allocated to high-risk patient {patient_id}"
            else:
                return False, "Low-risk patient - no emergency allocation"

    def emergency_interrupt(self, patient_id, request):
        with self.lock:
            request = np.array(request)
            self.available -= request
            self.allocations[patient_id] = request
            return True, "Emergency interrupt allocation done"

    def status(self):
        return {
            "available": self.available.tolist(),
            "allocations": {pid: alloc.tolist() for pid, alloc in self.allocations.items()}
        }
