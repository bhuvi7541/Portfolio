"""All portfolio content lives here. Edit this file — templates render from it."""

PROFILE = {
    "name": "Bhuvaneshwari M",
    "role": "Python Developer",
    "specialty": "FastAPI · Computer Vision",
    "location": "Madurai, Tamil Nadu",
    "email": "bhuvi7541@gmail.com",
    "phone": "+91 63823 26018",
    "phone_raw": "+916382326018",
    "linkedin": "https://www.linkedin.com/in/bhuvi7541/",
    "resume": "files/Bhuvaneshwari_M_Resume.pdf",
    "intro": (
        "I build backend systems, REST APIs and real-time dashboards for traffic and toll "
        "management — from DeepStream and YOLOv8 detection pipelines to FastAPI services and "
        "PostgreSQL reporting."
    ),
    "summary": [
        "I'm a Python developer with 2+ years of experience building backend applications, "
        "REST APIs, real-time dashboards and computer vision solutions at COS Artificial "
        "Intelligence in Madurai.",
        "My work spans real-time traffic monitoring, vehicle detection and classification (ATCC), "
        "ANPR data analysis, MQTT-based communication and video management systems — and the "
        "Linux deployment that keeps them running, with Nginx and systemd.",
    ],
    "status": "Open to new opportunities",
    "seeking": "Open to Python Backend Development and Computer Vision Engineering roles.",
}

ROLES = ["Python Developer", "FastAPI Backend Engineer", "Computer Vision Engineer"]

STATS = [
    {"value": 2, "suffix": "+", "label": "Years of experience"},
    {"value": 9, "suffix": "", "label": "Projects delivered"},
    {"value": 30, "suffix": "+", "label": "Tools & technologies"},
]

FACTS = [
    ("Experience", "2+ years"),
    ("Currently", "COS Artificial Intelligence"),
    ("Based in", "Madurai, India"),
    ("Education", "M.Sc. IT · CGPA 8.5"),
]

# Real screenshots shown in the hero carousel
SHOWCASE = [
    {"image": "img/atms-dashboard.jpg", "project": "ATMS-2023", "caption": "Corridor control dashboard — live devices, incidents and operations map"},
    {"image": "img/rvtl-live.jpg", "project": "RVTL", "caption": "LHS + RHS live view with hourly video management"},
    {"image": "img/gatei-tat.jpg", "project": "GATE-I", "caption": "Turnaround-time report — trips, average TAT, cross-stays, invalid entries"},
    {"image": "img/atcc-dashboard.jpg", "project": "Movable ATCC", "caption": "Kit health — disk, CPU / GPU temperature, RAM"},
    {"image": "img/sesha-rfid.jpg", "project": "Sesha Plus Audit", "caption": "RFID transactions with daily totals and filters"},
    {"image": "img/mlff-class.jpg", "project": "MLFF Audit", "caption": "TMS class vs AI class analysis"},
    {"image": "img/atms-vsm.jpg", "project": "ATMS-2023", "caption": "Section speed between two ANPR kits — over-limit and challan cases"},
]

# (name, devicon class) — None shows a monogram tile instead of a logo
SKILLS = [
    {"group": "Backend", "items": [
        ("Python", "devicon-python-plain"), ("FastAPI", "devicon-fastapi-plain"), ("Django", "devicon-django-plain"),
        ("REST APIs", None), ("SQLAlchemy", "devicon-sqlalchemy-plain"), ("Pydantic", None)]},
    {"group": "AI & Video", "items": [
        ("NVIDIA DeepStream", None), ("YOLOv8", None), ("PaddleOCR", None), ("OpenCV", "devicon-opencv-plain"),
        ("GStreamer", None), ("FFmpeg", None), ("OpenVINO", None)]},
    {"group": "Data & Messaging", "items": [
        ("PostgreSQL", "devicon-postgresql-plain"), ("MySQL", "devicon-mysql-original"), ("Redis", "devicon-redis-plain"),
        ("MQTT", None), ("AWS Kinesis", "devicon-amazonwebservices-plain-wordmark")]},
    {"group": "Security", "items": [("RBAC", None), ("JWT", None), ("Session Tokens", None)]},
    {"group": "Frontend", "items": [
        ("HTML", "devicon-html5-plain"), ("CSS", "devicon-css3-plain"), ("JavaScript", "devicon-javascript-plain"),
        ("Jinja2", None), ("Bootstrap", "devicon-bootstrap-plain")]},
    {"group": "Tools & Deployment", "items": [
        ("Git", "devicon-git-plain"), ("Linux", "devicon-linux-plain"), ("Nginx", "devicon-nginx-original"),
        ("systemd", None), ("VS Code", "devicon-vscode-plain"), ("Claude", None), ("Cursor", None), ("GitHub Copilot", "devicon-github-original")]},
]

EXPERIENCE = [
    {
        "role": "Python Developer",
        "org": "COS Artificial Intelligence Pvt. Ltd.",
        "place": "Madurai",
        "period": "Jun 2024 — Present",
        "current": True,
        "points": [
            "Build end-to-end project dashboards: frontend UI, FastAPI backend APIs, PostgreSQL integration, validation and reporting.",
            "Run continuous R&D to improve ATCC vehicle counting/classification and ANPR accuracy; benchmark DeepStream and OpenVINO pipelines on GPU vs CPU.",
            "Implemented RBAC and JWT-based authentication with Redis for session and token management.",
            "Validate detection accuracy and performance on live camera streams; deploy with Nginx and systemd.",
        ],
    },
    {
        "role": "Python Developer Intern",
        "org": "COS Artificial Intelligence Pvt. Ltd.",
        "place": "Madurai",
        "period": "Dec 2022 — Apr 2023",
        "current": False,
        "points": [
            "Learned Django, RTSP streams, OpenCV, GStreamer and DeepStream; set up the ATCC dashboard and added report downloads.",
        ],
    },
    {
        "role": "Front-End Developer Intern",
        "org": "Vyukshathriya Technologix Pvt. Ltd.",
        "place": "Madurai",
        "period": "Sep 2022 — Nov 2022",
        "current": False,
        "points": [
            "Built responsive web dashboards with HTML, CSS, JavaScript and Bootstrap, and deployed them on Netlify.",
        ],
    },
]

EDUCATION = [
    {"degree": "M.Sc. Information Technology", "school": "Fatima College (Autonomous), Madurai",
     "years": "2021 — 2023", "score": "CGPA 8.5"},
    {"degree": "B.Sc. Information Technology", "school": "Fatima College (Autonomous), Madurai",
     "years": "2018 — 2021", "score": "CGPA 7.9"},
]

# Projects with real screenshots are shown large ("featured"); the rest as cards.
PROJECTS = [
    {
        "slug": "atms",
        "name": "ATMS-2023 — Central Control Dashboard",
        "tagline": "Advanced Traffic Management System",
        "in_progress": False,
        "description": "The control-room tier of a three-tier highway platform: field AI kits report to package dashboards, which feed one central dashboard for the whole corridor. It brings incident detection, radar and section speed, e-challans, roadside signboards and reporting into a single screen.",
        "flow": ["Field AI kits", "Package dashboards", "ATMS control centre"],
        "points": [
            "Operations map with live device status and open incidents; push an incident to emergency contacts by mail or SMS",
            "VIDES and TMCS incident monitoring with evidence images, ANPR / overview camera logs and auto-refresh",
            "Radar speed display (VASD) and section speed (VSM) — average speed of a plate between two ANPR kits",
            "E-challan workflow: Initiated → Verified → pushed to NIC, with callback and a 60 s retry queue",
            "Roadside LED signboard messaging over TCP, recorded video clip retrieval, maintenance log",
            "Ten Excel reports, MQTT publishing to a unified dashboard, per-module RBAC enforced by middleware",
        ],
        "stack": ["Python", "FastAPI", "PostgreSQL", "SQLAlchemy", "Redis", "MQTT", "Leaflet", "ApexCharts", "APScheduler", "openpyxl"],
        "images": ["img/atms-dashboard.jpg", "img/atms-incidents.jpg", "img/atms-vides.jpg", "img/atms-tmcs.jpg",
                   "img/atms-vasd.jpg", "img/atms-vsm.jpg", "img/atms-vms.jpg", "img/atms-reports.jpg"],
    },
    {
        "slug": "sesha-safe",
        "name": "Sesha Safe — AI Traffic Enforcement",
        "tagline": "Roadside AI Kits + Cloud Dashboard",
        "in_progress": False,
        "description": "A two-tier enforcement platform: Jetson Orin kits at the roadside count and classify every vehicle crossing a drawn line, read its number plate and capture evidence of helmet, seat-belt and triple-riding violations; one cloud dashboard registers kits, locations and cameras, starts and stops detection remotely, streams live video and produces reports.",
        "flow": ["IP cameras (RTSP)", "Jetson kit — YOLO11 + ANPR", "Upload queue", "Cloud dashboard"],
        "points": [
            "18-class vehicle detection on DeepStream 7.1 / TensorRT FP16 with NvSORT tracking; line-crossing counts by lane and direction",
            "ANPR with PARSeq OCR and Indian-plate correction; helmet / no-helmet, seat-belt and triple-riding evidence crops",
            "Per-kit API keys, 20 s heartbeat and config pull, kit health (disk, CPU / GPU temperature, RAM, FPS)",
            "WebRTC live view through the cloud, streamed only while someone is watching",
            "Remote draw-line and Detect / Stop, per-run reports with evidence and record correction, daily & summary Excel reports",
            "Module-level RBAC, Redis sessions, login lockout and reCAPTCHA; VAPT / SQTC security hardening",
        ],
        "stack": ["Python", "FastAPI", "PostgreSQL", "Redis", "DeepStream", "YOLO11", "PARSeq OCR", "WebRTC", "Jetson Orin", "ApexCharts"],
        "images": ["img/seshasafe-helmet.jpg", "img/seshasafe-home.jpg", "img/seshasafe-nohelmet.jpg",
                   "img/seshasafe-live.jpg", "img/seshasafe-runs.jpg", "img/seshasafe-report.jpg"],
    },
    {
        "slug": "gate-i",
        "name": "GATE-I — AI Access Control",
        "tagline": "Plant Gate Monitoring with ANPR",
        "in_progress": False,
        "description": "Every vehicle in and out of a plant, accounted for. A gate camera reads number plates; GATE-I checks each one against registered and support vehicles, opens or denies the gate, and turns every read into trips, turnaround time and overstay alerts.",
        "flow": ["Gate camera", "ANPR kit", "Gate check API", "Trips & TAT", "Reports & alerts"],
        "points": [
            "Gate check API: registered or mapped support vehicle → allowed; anything else → logged as an invalid entry",
            "Trip pairing of entry and exit reads into turnaround time, cross-stays and per-vehicle history",
            "Report Insights with TAT, Cross Stay, Gate Activity and VR tabs — summary cards, five charts, Excel exports",
            "Overstay alerts (pop-up and e-mail), live camera view over WebSocket, hourly detections with video clip download",
            "Role / module access mapping; nine end-to-end browser test suites driving headless Chrome",
        ],
        "stack": ["Python", "FastAPI", "PostgreSQL", "SQLAlchemy", "WebSocket", "Jinja2", "ApexCharts", "AWS Kinesis Video Streams", "APScheduler"],
        "images": ["img/gatei-tat.jpg", "img/gatei-charts.jpg", "img/gatei-traffic.jpg", "img/gatei-trips.jpg", "img/gatei-vr.jpg"],
    },
    {
        "slug": "toll-sync",
        "name": "Toll Sync",
        "tagline": "Toll Automation & Traffic Analytics",
        "in_progress": False,
        "description": "Integrated ATCC, ANPR and TMS audit reporting to analyze vehicle counts, classification, FASTag mismatches and toll traffic trends.",
        "points": [
            "Detection management with per-camera line and ROI mapping",
            "Audit reports comparing system and detected vehicle classes, with vehicle images",
            "Video ingest through AWS Kinesis Video Streams",
        ],
        "stack": ["Python", "FastAPI", "PostgreSQL", "DeepStream", "YOLOv8", "PaddleOCR", "AWS Kinesis Video Streams"],
        "images": ["img/tollsync-audit.jpg", "img/tollsync-detection.jpg", "img/tollsync-login.jpg"],
    },
    {
        "slug": "rvtl",
        "name": "RVTL — Rajkot Vadinar Toll Way",
        "tagline": "AI Traffic Counting for Toll-Evasion Recovery",
        "in_progress": False,
        "description": "Vehicles bypassing a toll plaza on leakage roads mean lost revenue. RVTL counts and classifies every one of them in both directions on edge AI kits, syncs the data to a host PC, and turns it into tamper-proof, auditable reports the authorities use to recover that revenue.",
        "flow": ["Gantry cameras", "LPU kits (LHS & RHS)", "Host PC sync", "Dashboard & reports"],
        "points": [
            "Accuracy targets of ≥ 99% counting and ≥ 98% classification; the system reached 98.5–99% on RHS and 96% on the busier LHS",
            "Kit dashboard: draw the counting line on the live frame, start / stop detection, auto-resume after power loss",
            "Host dashboard: kit health (camera, temperature, storage), LHS + RHS live view with hourly video downloads",
            "Audit module to correct vehicle classes and hide duplicate or opposite-direction captures, with full audit trail",
            "Hourly, 15-minute, daily and monthly Excel reports — including cropped vehicle images",
            "Hourly ZIP backups with restore, OneDrive sync, e-mail alerts, RBAC with per-module permissions",
        ],
        "stack": ["Python", "FastAPI", "PostgreSQL", "YOLOv8", "GStreamer", "SQLAlchemy", "Pandas", "Jetson Orin NX", "Ubuntu"],
        "images": ["img/rvtl-live.jpg", "img/rvtl-kit.jpg", "img/rvtl-drawline.jpg", "img/rvtl-history.jpg",
                   "img/rvtl-audit.jpg", "img/rvtl-permissions.jpg", "img/rvtl-analytics.jpg"],
    },
    {
        "slug": "movable-atcc",
        "name": "Movable ATCC",
        "tagline": "Portable Traffic Counting & Classification",
        "in_progress": False,
        "description": "A portable counting kit that can be set up at any plaza or road: it counts and classifies vehicles from live camera feeds, stores data offline on the kit and syncs to the cloud when connectivity returns.",
        "flow": ["Camera", "Movable LPU kit", "Offline store", "Cloud sync"],
        "points": [
            "Kit health dashboard — disk, CPU / GPU temperature, RAM and live resource usage",
            "Live view per LPU and camera with a live / off toggle",
            "Plaza, device, camera and project management; draw line & ROI mapping for detection",
            "Day-hour reports and an RFID-unmatched view for reconciliation",
        ],
        "stack": ["Python", "FastAPI", "PostgreSQL", "DeepStream", "YOLOv8", "GStreamer"],
        "images": ["img/atcc-dashboard.jpg", "img/atcc-live.jpg"],
    },
    {
        "slug": "video-converter",
        "name": "Video Converter Tool",
        "tagline": "Batch Video Conversion & Compression",
        "in_progress": False,
        "description": "A web tool that converts whole folders of raw video files to the format you need, with the same encoding settings used for IP-camera footage, so quality and file size stay consistent across every file.",
        "flow": ["Upload or folder path", "Encoding settings", "FFmpeg conversion", "Download ZIP"],
        "points": [
            "Batch-converts every file of a chosen input format in a folder (e.g. AVI → MKV)",
            "Configurable resolution, FPS, bitrate, CRF and encoding preset (ultrafast → veryslow) to balance quality, speed and size",
            "Saved conversion jobs with live status, convert / stop controls, edit and job details",
            "Converted output saved to a target folder and downloadable from the app as a ZIP",
        ],
        "stack": ["Python", "FastAPI", "FFmpeg", "MySQL", "Jinja2"],
        "images": ["img/videoconv-form.jpg", "img/videoconv-list.jpg", "img/videoconv-upload.jpg"],
    },
    {
        "slug": "sesha-audit",
        "name": "Sesha Plus Audit",
        "tagline": "AI vs RFID Toll Audit Dashboard",
        "in_progress": False,
        "description": "An audit dashboard for a live toll plaza that puts AI detections and RFID (FASTag) transactions side by side, so mismatched or misclassified vehicles stand out.",
        "flow": ["AI records", "RFID transactions", "Toll data upload", "Data comparison"],
        "points": [
            "Filter by plaza, lane, camera and date-time range; search by tag ID",
            "Daily vehicle totals at a glance, paginated transaction table, one-click download",
            "Upload toll data and compare it against AI and RFID records",
        ],
        "stack": ["Python", "FastAPI", "PostgreSQL"],
        "images": ["img/sesha-rfid.jpg", "img/sesha-audit.jpg"],
    },
    {
        "slug": "mlff-audit",
        "name": "MLFF Audit Dashboard",
        "tagline": "TCMS vs RFID vs ATCC / ANPR Reconciliation",
        "in_progress": False,
        "description": "Upload the authority's toll report and the hourly ATCC / ANPR + RFID report ZIPs, and the dashboard reconciles them — comparing classes, counts and plate reads to show where toll records and AI data disagree.",
        "flow": ["Authority report (.xlsx)", "Reports ZIP", "Comparison", "Analysis"],
        "points": [
            "TMS class vs AI class analysis on every matched transaction",
            "Not-found partial match finder — falls back to last-4-digit plate matching to recover missed pairs",
            "Result text capture analysis — how many plate reads were fully captured vs partial or blank",
        ],
        "stack": ["Python", "FastAPI", "Pandas", "openpyxl"],
        "images": ["img/mlff-compare.jpg", "img/mlff-class.jpg", "img/mlff-notfound.jpg"],
    },
]


NAV = [
    ("about", "About"),
    ("skills", "Skills"),
    ("experience", "Experience"),
    ("projects", "Projects"),
    ("contact", "Contact"),
]


def context():
    return {
        "profile": PROFILE, "roles": ROLES, "stats": STATS, "facts": FACTS, "showcase": SHOWCASE,
        "skills": SKILLS, "experience": EXPERIENCE, "education": EDUCATION, "nav": NAV, "projects": PROJECTS,
    }
