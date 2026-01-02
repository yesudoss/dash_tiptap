**Create Virtual Env**
```bash
python -m venv env
env/scripts/activate
```

**Dependency Installation**
```bash
pip install -r requirements.txt
npm install --legacy-peer-deps
```

**Build JS & Generate Python**:
```bash
npm run build:js
# Validates and maps the React props to Python classes
dash-generate-components ./src/lib/components dash_tiptap -p package.json
```

**Run**
```bash
python usage.py
```
***
**Using Docker**
```bash
docker build -t dash-tiptap .
docker run -p 8050:8050 dash-tiptap
```

Check http://127.0.0.1:8050/ for result

***
## Approach and Implementation Details

This component bridges the gap between Python (Dash) and JavaScript (React) to provide a rich text editing experience with @mention support.

**Core Concept**:
- The component is a React wrapper around the **Tiptap** headless editor.
- It uses a custom `DashTiptap` class in Python to define props like `value` (HTML content) and `mentions` (list of users).
- When the editor content changes in the browser, the React component calls `setProps` to send the new HTML back to Dash.
- Dash callbacks can then use this value as an `Input`.
## Library and Framework Versions Used

**Frontend (JavaScript/React)**:
- **React**: `^18.2.0` (Modern functional components & hooks)
- **Tiptap**: `^3.14.0` (Core, Starter Kit, Mention Extension)
- **Tippy.js**: `^6.3.7` (Popup positioning)
- **Webpack**: `^5.84.1` (Bundling)

**Backend (Python)**:
- **Dash**: `^3.3.0` (requires `dash[dev]` for component generation)
****
## Demo
Attached the result video in the repository
https://github.com/yesudoss/dash_tiptap/blob/main/result-vid.mp4
