import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import AdaBoostClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATASET_PATH = os.path.join(
    BASE_DIR,
    "datasets",
    "winequality.csv"
)

MODEL_DIR = os.path.join(
    BASE_DIR,
    "models"
)

os.makedirs(MODEL_DIR, exist_ok=True)


columns = [
    "class",
    "alcohol",
    "malic_acid",
    "ash",
    "alcalinity_of_ash",
    "magnesium",
    "total_phenols",
    "flavanoids",
    "nonflavanoid_phenols",
    "proanthocyanins",
    "color_intensity",
    "hue",
    "od280_od315",
    "proline"
]


data = pd.read_csv(
    DATASET_PATH,
    header=None,
    names=columns
)


X = data.drop("class", axis=1)
y = data["class"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


models = {

    "Logistic Regression":
        LogisticRegression(max_iter=1000),

    "K-Nearest Neighbors":
        KNeighborsClassifier(n_neighbors=5),

    "Decision Tree":
        DecisionTreeClassifier(random_state=42),

    "Random Forest":
        RandomForestClassifier(
            n_estimators=100,
            random_state=42
        ),

    "Support Vector Machine":
        SVC(
            probability=True,
            random_state=42
        ),

    "Naive Bayes":
        GaussianNB(),

    "Gradient Boosting":
        GradientBoostingClassifier(
            random_state=42
        ),

    "AdaBoost":
        AdaBoostClassifier(
            random_state=42
        )
}


metrics = {}


for name, model in models.items():

    if name in [
        "Logistic Regression",
        "K-Nearest Neighbors",
        "Support Vector Machine"
    ]:
        model.fit(X_train_scaled, y_train)

        train_predictions = model.predict(X_train_scaled)
        test_predictions = model.predict(X_test_scaled)

    else:
        model.fit(X_train, y_train)

        train_predictions = model.predict(X_train)
        test_predictions = model.predict(X_test)


    training_score = model.score(
        X_train_scaled if name in [
            "Logistic Regression",
            "K-Nearest Neighbors",
            "Support Vector Machine"
        ] else X_train,
        y_train
    )


    testing_score = model.score(
        X_test_scaled if name in [
            "Logistic Regression",
            "K-Nearest Neighbors",
            "Support Vector Machine"
        ] else X_test,
        y_test
    )


    accuracy = accuracy_score(
        y_test,
        test_predictions
    )


    precision = precision_score(
        y_test,
        test_predictions,
        average="weighted",
        zero_division=0
    )


    recall = recall_score(
        y_test,
        test_predictions,
        average="weighted",
        zero_division=0
    )


    f1 = f1_score(
        y_test,
        test_predictions,
        average="weighted",
        zero_division=0
    )


    metrics[name] = {
        "accuracy": round(float(accuracy), 4),
        "training_score": round(float(training_score), 4),
        "testing_score": round(float(testing_score), 4),
        "precision": round(float(precision), 4),
        "recall": round(float(recall), 4),
        "f1_score": round(float(f1), 4)
    }


    model_path = os.path.join(
        MODEL_DIR,
        name.replace(" ", "_").lower() + ".pkl"
    )


    joblib.dump(
        model,
        model_path
    )


joblib.dump(
    scaler,
    os.path.join(MODEL_DIR, "scaler.pkl")
)


joblib.dump(
    metrics,
    os.path.join(MODEL_DIR, "metrics.pkl")
)


print()
print("=" * 50)
print("MODEL TRAINING COMPLETED")
print("=" * 50)


for name, result in metrics.items():

    print()
    print(name)

    print(
        "Accuracy       :",
        result["accuracy"]
    )

    print(
        "Training Score :",
        result["training_score"]
    )

    print(
        "Testing Score  :",
        result["testing_score"]
    )

    print(
        "Precision      :",
        result["precision"]
    )

    print(
        "Recall         :",
        result["recall"]
    )

    print(
        "F1 Score       :",
        result["f1_score"]
    )


print()
print("Models saved inside:")
print(MODEL_DIR)
print("=" * 50)