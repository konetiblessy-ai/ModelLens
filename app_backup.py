import requests
from urllib.parse import urlparse

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI(
    title="ModelLens",
    description="AI Model Analyzer",
    version="1.0.0"
)


app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


templates = Jinja2Templates(
    directory="templates"
)


# =========================================
# HOME PAGE
# =========================================

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


# =========================================
# STATUS
# =========================================

@app.get("/api/status")
async def status():

    return {
        "status": "online",
        "application": "ModelLens",
        "message": "AI Model Analyzer is ready"
    }


# =========================================
# PROJECT ANALYZER
# =========================================

@app.post("/api/analyze-project")
async def analyze_project(data: dict):

    url = data.get("url", "").strip()

    algorithm = data.get(
        "algorithm",
        "Unknown"
    )

    problem = data.get(
        "problem",
        "Unknown"
    )

    # -----------------------------------------
    # CHECK URL
    # -----------------------------------------

    if not url:
        return {
            "error": "Project URL is required."
        }

    if (
        not url.startswith("http://")
        and
        not url.startswith("https://")
    ):
        return {
            "error": (
                "Enter a complete URL such as "
                "http://127.0.0.1:8000"
            )
        }

    try:

        # -----------------------------------------
        # PARSE URL
        # -----------------------------------------

        parsed = urlparse(url)

        if not parsed.hostname:
            return {
                "error": "Invalid project URL."
            }

        # -----------------------------------------
        # CONNECT TO PROJECT
        # -----------------------------------------

        response = requests.get(
            url,
            timeout=5
        )

        page_text = response.text.lower()

        # -----------------------------------------
        # DETECT API ENDPOINTS
        # -----------------------------------------

        endpoint_count = 0
        detected_endpoints = []

        try:

            openapi_url = url.rstrip("/") + "/openapi.json"

            openapi_response = requests.get(
                openapi_url,
                timeout=5
            )

            if openapi_response.ok:

                openapi = openapi_response.json()

                detected_endpoints = list(
                    openapi.get(
                        "paths",
                        {}
                    ).keys()
                )

                endpoint_count = len(
                    detected_endpoints
                )

        except Exception:
            pass

        # -----------------------------------------
        # ANALYSIS ARRAYS
        # -----------------------------------------

        missing = []
        improvements = []

        # -----------------------------------------
        # CHECK PREDICTION ENDPOINT
        # -----------------------------------------

        prediction_endpoints = [
            "/predict",
            "/api/predict",
            "/prediction",
            "/api/prediction"
        ]

        has_prediction = any(
            endpoint in detected_endpoints
            for endpoint in prediction_endpoints
        )

        if not has_prediction:

            missing.append(
                "A clearly exposed prediction endpoint "
                "was not detected."
            )

            improvements.append(
                "Expose a dedicated prediction endpoint "
                "so the model can be tested externally."
            )

        # -----------------------------------------
        # CHECK MODEL INFORMATION
        # -----------------------------------------

        model_info_endpoints = [
            "/api/model-info",
            "/model-info",
            "/api/model",
            "/model"
        ]

        has_model_info = any(
            endpoint in detected_endpoints
            for endpoint in model_info_endpoints
        )

        if not has_model_info:

            missing.append(
                "Model metadata such as algorithm, "
                "features and evaluation details "
                "is not exposed."
            )

            improvements.append(
                "Add a model-information API containing "
                "the algorithm, features and evaluation metrics."
            )

        # -----------------------------------------
        # CHECK EVALUATION METRICS
        # -----------------------------------------

        evaluation_words = [
            "accuracy",
            "precision",
            "recall",
            "f1",
            "r2",
            "mean absolute error",
            "confusion matrix"
        ]

        has_evaluation = any(
            word in page_text
            for word in evaluation_words
        )

        if not has_evaluation:

            missing.append(
                "Model evaluation metrics were not "
                "detected on the project page."
            )

            improvements.append(
                "Expose evaluation metrics such as "
                "accuracy, precision, recall and F1 score."
            )

        # -----------------------------------------
        # CHECK API DOCUMENTATION
        # -----------------------------------------

        has_docs = (
            "/docs" in detected_endpoints
            or
            "/redoc" in detected_endpoints
        )

        if not has_docs:

            missing.append(
                "Interactive API documentation "
                "was not detected."
            )

            improvements.append(
                "Add API documentation so the model "
                "endpoints are easier to understand and test."
            )

        # -----------------------------------------
        # DETECT PROJECT NAME
        # -----------------------------------------

        if "iris" in page_text:

            project_name = "Iris ML Project"

        elif "random forest" in page_text:

            project_name = "Random Forest ML Project"

        else:

            project_name = (
                parsed.hostname or "ML Project"
            )

        # -----------------------------------------
        # PROJECT STATUS
        # -----------------------------------------

        if not missing:

            summary = (
                "ModelLens detected the main project "
                "components. The selected model appears "
                "to have a clear analysis and prediction interface."
            )

            project_status = "HEALTHY"

        else:

            summary = (
                f"ModelLens connected successfully and "
                f"reviewed the {algorithm} project. "
                f"{len(missing)} improvement area(s) were detected."
            )

            project_status = "REVIEW"

        # -----------------------------------------
        # RETURN ANALYSIS
        # -----------------------------------------

        return {

            "project": project_name,

            "algorithm": algorithm,

            "problem": problem,

            "endpoint_count": endpoint_count,

            "status": project_status,

            "missing": missing,

            "improvements": improvements,

            "summary": summary
        }

    # -----------------------------------------
    # CONNECTION ERROR
    # -----------------------------------------

    except requests.exceptions.RequestException:

        return {

            "error": (
                "ModelLens could not connect to that URL. "
                "Make sure the ML project is running."
            )
        }

    # -----------------------------------------
    # OTHER ERROR
    # -----------------------------------------

    except Exception as e:

        return {

            "error": f"Analysis failed: {str(e)}"
        }