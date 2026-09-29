from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.responses import PlainTextResponse
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import pandas as pd
import numpy as np
import os
import re

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

from sklearn.linear_model import (
    LinearRegression,
    LogisticRegression,
    Ridge,
    Lasso,
    ElasticNet
)

from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import (
    RandomForestClassifier,
    RandomForestRegressor,
    GradientBoostingClassifier,
    GradientBoostingRegressor,
    AdaBoostClassifier,
    ExtraTreesClassifier
)

from sklearn.neighbors import (
    KNeighborsClassifier,
    KNeighborsRegressor
)

from sklearn.svm import (
    SVC,
    SVR
)

from sklearn.naive_bayes import (
    GaussianNB,
    MultinomialNB,
    BernoulliNB
)

from sklearn.cluster import (
    KMeans,
    AgglomerativeClustering,
    DBSCAN
)

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    r2_score,
    mean_absolute_error,
    mean_squared_error,
    silhouette_score,
    davies_bouldin_score
)


app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


os.makedirs("datasets", exist_ok=True)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )


def clean_column_name(name):
    return re.sub(r"[^a-zA-Z0-9_]", "_", str(name)).strip("_")


def detect_target(df):
    """
    Try to automatically identify the target column.

    Priority:
    1. Common target names
    2. Last column
    """

    common_names = [
        "target",
        "label",
        "class",
        "output",
        "result",
        "prediction",
        "species",
        "diagnosis",
        "outcome",
        "salary",
        "price"
    ]

    columns_lower = {
        str(column).lower(): column
        for column in df.columns
    }

    for name in common_names:
        if name in columns_lower:
            return columns_lower[name]

    return df.columns[-1]


def prepare_features(X):
    """
    Prepare numeric and categorical columns.
    """

    numeric_columns = X.select_dtypes(
        include=["int64", "int32", "float64", "float32"]
    ).columns.tolist()

    categorical_columns = X.select_dtypes(
        include=["object", "category", "bool"]
    ).columns.tolist()

    numeric_pipeline = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="median")
            )
        ]
    )

    categorical_pipeline = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="most_frequent")
            ),
            (
                "encoder",
                __import__(
                    "sklearn.preprocessing",
                    fromlist=["OneHotEncoder"]
                ).OneHotEncoder(
                    handle_unknown="ignore"
                )
            )
        ]
    )

    transformers = []

    if numeric_columns:
        transformers.append(
            (
                "numeric",
                numeric_pipeline,
                numeric_columns
            )
        )

    if categorical_columns:
        transformers.append(
            (
                "categorical",
                categorical_pipeline,
                categorical_columns
            )
        )

    return ColumnTransformer(
        transformers=transformers
    )


def get_model(algorithm, problem_type):
    name = algorithm.lower().strip()

    if problem_type == "regression":

        if "linear regression" == name:
            return LinearRegression()

        if "multiple linear regression" == name:
            return LinearRegression()

        if "ridge" in name:
            return Ridge()

        if "lasso" in name:
            return Lasso()

        if "elastic net" in name:
            return ElasticNet()

        if "decision tree" in name:
            return DecisionTreeRegressor(random_state=42)

        if "random forest" in name:
            return RandomForestRegressor(
                n_estimators=100,
                random_state=42
            )

        if "knn" in name:
            return KNeighborsRegressor()

        if "support vector" in name:
            return SVR()

        if "gradient boosting" in name:
            return GradientBoostingRegressor(
                random_state=42
            )

        if "polynomial" in name:
            return LinearRegression()

        return RandomForestRegressor(
            n_estimators=100,
            random_state=42
        )

    if problem_type == "classification":

        if "logistic" in name:
            return LogisticRegression(
                max_iter=2000
            )

        if "knn" in name:
            return KNeighborsClassifier()

        if "decision tree" in name:
            return DecisionTreeClassifier(
                random_state=42
            )

        if "random forest" in name:
            return RandomForestClassifier(
                n_estimators=100,
                random_state=42
            )

        if name == "svm" or "support vector" in name:
            return SVC(
                probability=True
            )

        if "gaussian" in name:
            return GaussianNB()

        if "multinomial" in name:
            return MultinomialNB()

        if "bernoulli" in name:
            return BernoulliNB()

        if "gradient boosting" in name:
            return GradientBoostingClassifier(
                random_state=42
            )

        if "adaboost" in name:
            return AdaBoostClassifier(
                random_state=42
            )

        if "extra trees" in name:
            return ExtraTreesClassifier(
                n_estimators=100,
                random_state=42
            )

        if "naive bayes" in name:
            return GaussianNB()

        return RandomForestClassifier(
            n_estimators=100,
            random_state=42
        )

    return None


@app.post("/api/analyze-model")
async def analyze_model(
    project_url: str = Form(""),
    learning_type: str = Form(""),
    problem_type: str = Form(""),
    algorithm: str = Form(""),
    file: UploadFile = File(...)
):

    try:

        filename = file.filename

        if not filename:
            return {
                "success": False,
                "error": "Please select a CSV file."
            }

        if not filename.lower().endswith(".csv"):
            return {
                "success": False,
                "error": "Only CSV files are supported."
            }

        safe_filename = os.path.basename(filename)

        file_path = os.path.join(
            "datasets",
            safe_filename
        )

        contents = await file.read()

        with open(file_path, "wb") as output_file:
            output_file.write(contents)

        df = pd.read_csv(file_path)

        if df.empty:
            return {
                "success": False,
                "error": "The CSV file is empty."
            }

        if len(df.columns) < 2:
            return {
                "success": False,
                "error": "CSV must contain at least two columns."
            }

        original_columns = df.columns.tolist()

        target_column = detect_target(df)

        X = df.drop(columns=[target_column])
        y = df[target_column]

        feature_columns = X.columns.tolist()

        rows = len(df)
        columns = len(df.columns)

        # -----------------------------------------
        # UNSUPERVISED LEARNING
        # -----------------------------------------

        if problem_type == "clustering":

            numeric_df = X.select_dtypes(
                include=np.number
            )

            if numeric_df.shape[1] < 2:
                return {
                    "success": False,
                    "error": "Clustering requires at least two numeric feature columns."
                }

            numeric_df = numeric_df.fillna(
                numeric_df.median()
            )

            scaler = StandardScaler()

            X_scaled = scaler.fit_transform(
                numeric_df
            )

            algorithm_lower = algorithm.lower()

            if "k-means" in algorithm_lower:

                model = KMeans(
                    n_clusters=3,
                    random_state=42,
                    n_init=10
                )

                labels = model.fit_predict(
                    X_scaled
                )

            elif "hierarchical" in algorithm_lower:

                model = AgglomerativeClustering(
                    n_clusters=3
                )

                labels = model.fit_predict(
                    X_scaled
                )

            elif "dbscan" in algorithm_lower:

                model = DBSCAN()

                labels = model.fit_predict(
                    X_scaled
                )

            else:

                model = KMeans(
                    n_clusters=3,
                    random_state=42,
                    n_init=10
                )

                labels = model.fit_predict(
                    X_scaled
                )

            unique_labels = set(labels)

            if len(unique_labels) > 1:

                silhouette = silhouette_score(
                    X_scaled,
                    labels
                )

                db_score = davies_bouldin_score(
                    X_scaled,
                    labels
                )

            else:

                silhouette = None
                db_score = None

            cluster_count = len(
                set(labels)
            )

            return {
                "success": True,
                "project": project_url,
                "algorithm": algorithm,
                "problem": problem_type,
                "learning_type": learning_type,
                "rows": rows,
                "columns": columns,
                "features": feature_columns,
                "target": "Not applicable",
                "model_type": "Unsupervised Learning",
                "metrics": {
                    "silhouette": silhouette,
                    "davies_bouldin": db_score,
                    "clusters": cluster_count
                },
                "api": {
                    "endpoint_count": 0,
                    "prediction": False,
                    "documentation": False,
                    "endpoints": []
                },
                "missing": [],
                "improvements": [
                    "Consider testing different cluster counts.",
                    "Scale numerical features before clustering.",
                    "Compare clustering metrics between algorithms."
                ],
                "summary": (
                    f"ModelLens analyzed {rows} rows using "
                    f"{algorithm}. The dataset produced "
                    f"{cluster_count} clusters."
                )
            }

        # -----------------------------------------
        # SUPERVISED LEARNING
        # -----------------------------------------

        if problem_type not in [
            "classification",
            "regression"
        ]:

            return {
                "success": False,
                "error": (
                    "This version currently supports "
                    "classification, regression and clustering."
                )
            }

        if y.isnull().all():

            return {
                "success": False,
                "error": "The target column contains no usable values."
            }

        # Classification target encoding
        target_encoder = None

        if problem_type == "classification":

            target_encoder = LabelEncoder()

            y = y.fillna(
                y.mode()[0]
            )

            y = target_encoder.fit_transform(
                y.astype(str)
            )

        else:

            y = pd.to_numeric(
                y,
                errors="coerce"
            )

            valid_rows = y.notna()

            X = X.loc[valid_rows]
            y = y.loc[valid_rows]

        if len(X) < 10:

            return {
                "success": False,
                "error": "The dataset needs at least 10 usable rows."
            }

        # Remove columns that contain no useful data
        useful_features = []

        for column in X.columns:

            if X[column].notna().sum() > 0:
                useful_features.append(column)

        X = X[useful_features]

        if X.shape[1] == 0:

            return {
                "success": False,
                "error": "No usable feature columns were found."
            }

        feature_columns = X.columns.tolist()

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.20,
            random_state=42,
            stratify=y if problem_type == "classification"
            and len(np.unique(y)) > 1 else None
        )

        preprocessor = prepare_features(X)

        model = get_model(
            algorithm,
            problem_type
        )

        if model is None:

            return {
                "success": False,
                "error": f"Algorithm '{algorithm}' is not supported yet."
            }

        pipeline = Pipeline(
            steps=[
                (
                    "preprocessor",
                    preprocessor
                ),
                (
                    "model",
                    model
                )
            ]
        )

        pipeline.fit(
            X_train,
            y_train
        )

        predictions = pipeline.predict(
            X_test
        )

        # -----------------------------------------
        # CLASSIFICATION METRICS
        # -----------------------------------------

        if problem_type == "classification":

            accuracy = accuracy_score(
                y_test,
                predictions
            )

            precision = precision_score(
                y_test,
                predictions,
                average="weighted",
                zero_division=0
            )

            recall = recall_score(
                y_test,
                predictions,
                average="weighted",
                zero_division=0
            )

            f1 = f1_score(
                y_test,
                predictions,
                average="weighted",
                zero_division=0
            )

            metrics = {
                "accuracy": float(accuracy),
                "precision": float(precision),
                "recall": float(recall),
                "f1": float(f1),
                "testing": float(accuracy)
            }

        # -----------------------------------------
        # REGRESSION METRICS
        # -----------------------------------------

        else:

            r2 = r2_score(
                y_test,
                predictions
            )

            mae = mean_absolute_error(
                y_test,
                predictions
            )

            mse = mean_squared_error(
                y_test,
                predictions
            )

            rmse = np.sqrt(
                mse
            )

            metrics = {
                "r2": float(r2),
                "mae": float(mae),
                "mse": float(mse),
                "rmse": float(rmse),
                "testing": float(r2)
            }

        # -----------------------------------------
        # MODEL REVIEW
        # -----------------------------------------

        missing_items = []

        if rows < 50:
            missing_items.append(
                "Dataset contains relatively few rows."
            )

        if X.isnull().sum().sum() > 0:
            missing_items.append(
                "Missing values were detected and handled."
            )

        if problem_type == "classification":

            if len(np.unique(y)) < 2:
                missing_items.append(
                    "Target contains insufficient classes."
                )

        if len(missing_items) == 0:
            missing_items.append(
                "No major dataset issue detected."
            )

        improvements = [
            "Compare multiple algorithms before selecting a final model.",
            "Use cross-validation for a more reliable evaluation.",
            "Check for class imbalance when working with classification.",
            "Inspect important features and remove irrelevant columns."
        ]

        # -----------------------------------------
        # FINAL RESPONSE
        # -----------------------------------------

        return {
            "success": True,

            "project": project_url,

            "project_name": (
                os.path.basename(
                    project_url.rstrip("/")
                )
                if project_url
                else "Uploaded ML Project"
            ),

            "algorithm": algorithm,

            "problem": problem_type,

            "learning_type": learning_type,

            "rows": rows,

            "columns": columns,

            "features": feature_columns,

            "target": str(target_column),

            "model_type": (
                "Classification Model"
                if problem_type == "classification"
                else "Regression Model"
            ),

            "metrics": metrics,

            "api": {
                "endpoint_count": 1,
                "prediction": True,
                "documentation": True,
                "endpoints": [
                    "/api/analyze-model"
                ]
            },

            "missing": missing_items,

            "improvements": improvements,

            "summary": (
                f"ModelLens successfully trained and evaluated "
                f"{algorithm} using {rows} rows and "
                f"{len(feature_columns)} feature columns. "
                f"The detected target column is '{target_column}'."
            ),

            "prediction_sample": [
                {
                    "actual": (
                        float(actual)
                        if isinstance(
                            actual,
                            (np.integer, np.floating)
                        )
                        else str(actual)
                    ),
                    "predicted": (
                        float(predicted)
                        if isinstance(
                            predicted,
                            (np.integer, np.floating)
                        )
                        else str(predicted)
                    )
                }
                for actual, predicted in list(
                    zip(
                        y_test,
                        predictions
                    )
                )[:10]
            ]
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }


@app.post("/upload")
async def upload_csv(file: UploadFile = File(...)):

    try:

        if not file.filename.lower().endswith(".csv"):

            return {
                "success": False,
                "error": "Only CSV files are allowed."
            }

        safe_filename = os.path.basename(
            file.filename
        )

        file_path = os.path.join(
            "datasets",
            safe_filename
        )

        contents = await file.read()

        with open(file_path, "wb") as output_file:
            output_file.write(contents)

        df = pd.read_csv(
            file_path
        )

        return {
            "success": True,
            "filename": safe_filename,
            "rows": len(df),
            "columns": len(df.columns),
            "column_names": df.columns.tolist()
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }
@app.get("/robots.txt", response_class=PlainTextResponse)
async def robots_txt(request: Request):

    base_url = str(request.base_url).rstrip("/")

    return f"""User-agent: *
Allow: /

Sitemap: {base_url}/sitemap.xml
"""


@app.get("/sitemap.xml", response_class=PlainTextResponse)
async def sitemap_xml(request: Request):

    base_url = str(request.base_url).rstrip("/")

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">

    <url>
        <loc>{base_url}/</loc>
    </url>

</urlset>
"""