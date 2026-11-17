from flask import Flask, jsonify, request, send_from_directory
from pathlib import Path

# Flask serves the existing HTML/CSS/JavaScript frontend.
# Student profile and application demo data remain in browser localStorage.
BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__, static_folder=None)


@app.get("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")


@app.get("/<path:filename>")
def frontend_files(filename):
    # Serve only files inside this project folder.
    return send_from_directory(BASE_DIR, filename)


@app.get("/api/health")
def health():
    return jsonify({
        "status": "success",
        "message": "Smart Campus Placement Portal server is running"
    })


@app.post("/api/contact-placement-cell")
def contact_placement_cell():
    """Demo endpoint showing how a frontend form can send data to Flask."""
    data = request.get_json(silent=True) or {}
    name = str(data.get("name", "")).strip()
    email = str(data.get("email", "")).strip()
    message = str(data.get("message", "")).strip()

    if not name or not email or not message:
        return jsonify({
            "status": "error",
            "message": "Name, email and message are required."
        }), 400

    # This academic demo validates the request but does not email or store it.
    return jsonify({
        "status": "success",
        "message": "Your demo request was received.",
        "submitted_by": name
    }), 201


@app.post("/api/notify-person")
def notify_person():
    """Demo endpoint: validates a 'notify a known person' request (selected/rejected)."""
    data = request.get_json(silent=True) or {}
    email = str(data.get("email", "")).strip()
    status = str(data.get("status", "")).strip()
    if "@" not in email or status not in ("Selected", "Rejected"):
        return jsonify({"status": "error", "message": "Valid email and status (Selected/Rejected) required."}), 400
    # Demo only: a real system would send an email/SMS here.
    print(f"[NOTIFY] {email}: {data.get('message', '')}")
    return jsonify({"status": "success", "message": f"Notification queued for {email}."}), 201


if __name__ == "__main__":
    # Run locally at http://127.0.0.1:5000
    app.run(host="127.0.0.1", port=5000, debug=True)
