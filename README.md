# Demand Lab — Interview Preparation Website

A static, mobile-friendly interview coaching site covering supply-chain basics, rolling forecasts, ERP/AP2 concepts, PSI, inventory reallocation, metrics, Excel, 10 interview answers, flashcards, and mock interviews.

**No build step, framework, API key, server or paid subscription is required.** Files are plain HTML, CSS and JavaScript. All examples are fictional teaching scenarios; they do not claim to represent Samsung's proprietary processes.

## Preview locally

Open `index.html` in your browser. (For a local development server, run `python3 -m http.server 8000` in this folder, then visit `http://localhost:8000`.)

## Publish with GitHub Pages

1. Sign in to GitHub and create a **new public repository** (for example `demand-planner-interview-lab`).
2. Upload the **contents** of this folder to the repository **root**. `index.html` must be at the root, not inside a nested `demand-planner-interview-lab` folder.
3. Commit the files to the `main` branch.
4. Go to **Settings → Pages** and under **Build and deployment**, select **Deploy from a branch**, then `main` and `/(root)`. Save.
5. Once GitHub Pages finishes publishing, your shareable URL will usually be `https://YOUR-USERNAME.github.io/demand-planner-interview-lab/`. Check the exact URL in Pages settings.

GitHub Pages visibility: The repository and static site will be publicly reachable. Do not add private coaching notes or personal candidate data to source files.

## Publish with Vercel

1. Push the project files to a GitHub repository.
2. Open the Vercel Dashboard, choose **Add New → Project**, and import that repository.
3. For a plain HTML/CSS/JS site, select **Other** (if a framework is requested), leave the build command blank, and leave output directory at `.` / repository root if necessary.
4. Click **Deploy**. Copy the live `*.vercel.app` URL into WhatsApp or any messaging app.

Alternatively, Vercel supports deployments using its CLI; importing a GitHub repository is simplest for this project.

## How learning progress works

Marked interview questions, Excel skills, flashcard progress and typed notes are saved with `localStorage` in the viewer's own browser. Different devices/browsers do **not** sync. Clearing site data removes progress. Do not type confidential employer or personal information into public/shared devices.

## Site files

- `index.html` — website content and navigation
- `styles.css` — responsive visual design
- `app.js` — interview content, PSI simulator, forecast math, flashcards, scores and offline CSV download
- `favicon.svg` — icon
- `.nojekyll` — compatible with GitHub Pages

## Notes

- The interview sample answers are **templates**; substitute real accomplishments when asked about past experience.
- PSI and financial risk examples are simplified training scenarios and require feasibility checks in a real job.
- The WAPE and bias math uses actual demand as denominator, with signed error `Actual − Forecast`.
