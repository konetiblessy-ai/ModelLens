/* =========================================
   MODEL DATA
========================================= */

const modelData = {

    supervised: {

        title: "SUPERVISED LEARNING",

        description:
            "Learn from labelled data and predict known outcomes.",

        problems: {

            regression: {

                title: "REGRESSION",

                description:
                    "Predict continuous numerical values.",

                algorithms: [

                    ["01", "Linear Regression",
                        "Predict a continuous value using a linear relationship."],

                    ["02", "Multiple Linear Regression",
                        "Use multiple input features to predict a numerical value."],

                    ["03", "Polynomial Regression",
                        "Model non-linear relationships between variables."],

                    ["04", "Ridge Regression",
                        "Linear regression with L2 regularization."],

                    ["05", "Lasso Regression",
                        "Regularized regression with feature selection."],

                    ["06", "Elastic Net Regression",
                        "Combines Ridge and Lasso regularization."],

                    ["07", "Decision Tree Regression",
                        "Predict numerical values using decision rules."],

                    ["08", "Random Forest Regression",
                        "Combine multiple decision trees for prediction."],

                    ["09", "KNN Regression",
                        "Predict values using nearby observations."],

                    ["10", "Support Vector Regression",
                        "Fit a regression function using support vectors."],

                    ["11", "Gradient Boosting Regression",
                        "Build sequential trees to improve predictions."]
                ]
            },


            classification: {

                title: "CLASSIFICATION",

                description:
                    "Predict categories or classes from labelled data.",

                algorithms: [

                    ["01", "Logistic Regression",
                        "Predict categorical outcomes using probabilities."],

                    ["02", "KNN Classifier",
                        "Classify observations using their nearest neighbours."],

                    ["03", "Decision Tree Classifier",
                        "Classify data using decision rules."],

                    ["04", "Random Forest Classifier",
                        "Combine multiple decision trees for classification."],

                    ["05", "Support Vector Machine",
                        "Find an optimal boundary between classes."],

                    ["06", "Naive Bayes",
                        "Probabilistic classification using Bayes' theorem."],

                    ["07", "Gaussian Naive Bayes",
                        "Naive Bayes designed for continuous features."],

                    ["08", "Multinomial Naive Bayes",
                        "Useful for count-based feature data."],

                    ["09", "Bernoulli Naive Bayes",
                        "Designed for binary feature data."],

                    ["10", "Gradient Boosting Classifier",
                        "Sequential ensemble learning for classification."],

                    ["11", "AdaBoost Classifier",
                        "Combines weak learners into a stronger classifier."],

                    ["12", "Extra Trees Classifier",
                        "Highly randomized tree-based ensemble model."]
                ]
            }
        }
    },


    unsupervised: {

        title: "UNSUPERVISED LEARNING",

        description:
            "Discover hidden structures and patterns without target labels.",

        problems: {

            clustering: {

                title: "CLUSTERING",

                description:
                    "Group similar observations together.",

                algorithms: [

                    ["01", "K-Means",
                        "Partition observations into K clusters."],

                    ["02", "Hierarchical Clustering",
                        "Create a hierarchy of related clusters."],

                    ["03", "DBSCAN",
                        "Find clusters using density-based grouping."],

                    ["04", "Gaussian Mixture Model",
                        "Model data using a mixture of Gaussian distributions."],

                    ["05", "Mean Shift",
                        "Find dense regions within a dataset."],

                    ["06", "Spectral Clustering",
                        "Cluster observations using graph-based relationships."]
                ]
            },


            dimensionality: {

                title: "DIMENSIONALITY REDUCTION",

                description:
                    "Reduce the number of features while preserving useful information.",

                algorithms: [

                    ["01", "PCA",
                        "Reduce dimensions while preserving maximum variance."],

                    ["02", "Factor Analysis",
                        "Discover hidden factors behind observed variables."],

                    ["03", "Truncated SVD",
                        "Reduce dimensionality using matrix decomposition."],

                    ["04", "t-SNE",
                        "Visualize high-dimensional data in lower dimensions."],

                    ["05", "UMAP",
                        "Create meaningful low-dimensional representations."]
                ]
            }
        }
    },


    deep: {

        title: "DEEP LEARNING",

        description:
            "Explore neural networks and modern AI architectures.",

        problems: {

            neural: {

                title: "NEURAL NETWORKS",

                description:
                    "Learn complex relationships using connected neural layers.",

                algorithms: [

                    ["01", "ANN",
                        "Artificial Neural Network for general prediction tasks."],

                    ["02", "MLP",
                        "Multi-Layer Perceptron for non-linear learning."]
                ]
            },


            vision: {

                title: "COMPUTER VISION",

                description:
                    "Process and understand image-based information.",

                algorithms: [

                    ["01", "CNN",
                        "Convolutional Neural Network for image processing."],

                    ["02", "ResNet",
                        "Deep residual architecture for computer vision."],

                    ["03", "VGG",
                        "Deep convolutional neural network architecture."],

                    ["04", "EfficientNet",
                        "Efficient convolutional architecture."]
                ]
            },


            sequence: {

                title: "SEQUENCE / TIME SERIES",

                description:
                    "Process sequential and time-dependent information.",

                algorithms: [

                    ["01", "RNN",
                        "Recurrent Neural Network for sequential data."],

                    ["02", "LSTM",
                        "Learn long-term dependencies in sequences."],

                    ["03", "GRU",
                        "Efficient recurrent architecture."],

                    ["04", "Bidirectional LSTM",
                        "Process sequence information in both directions."]
                ]
            },


            modern: {

                title: "MODERN DEEP LEARNING",

                description:
                    "Explore modern generative and attention-based architectures.",

                algorithms: [

                    ["01", "Autoencoder",
                        "Learn compressed representations of data."],

                    ["02", "Variational Autoencoder",
                        "Learn probabilistic latent representations."],

                    ["03", "Transformer",
                        "Attention-based architecture for complex sequences."],

                    ["04", "Vision Transformer",
                        "Transformer architecture designed for image data."]
                ]
            }
        }
    }
};


/* =========================================
   CURRENT SELECTION
========================================= */

let selectedAlgorithm = "";

let selectedLearningType = "";

let selectedProblemKey = "";


/* =========================================
   HERO
========================================= */

function scrollToLearning() {

    const section =
        document.getElementById("learning");

    if (!section) {
        return;
    }

    section.scrollIntoView({
        behavior: "smooth",
        block: "start"
    });
}


/* =========================================
   02 / MODEL EXPLORER
========================================= */

function showExplorer(type) {

    const data =
        modelData[type];

    if (!data) {
        return;
    }

    const explorer =
        document.getElementById("explorer");

    const title =
        document.getElementById("explorer-title");

    const description =
        document.getElementById("explorer-description");

    const problemArea =
        document.getElementById("problem-area");

    const algorithmArea =
        document.getElementById("algorithm-area");


    if (
        !explorer ||
        !title ||
        !description ||
        !problemArea ||
        !algorithmArea
    ) {
        return;
    }


    title.textContent =
        data.title;

    description.textContent =
        data.description;


    algorithmArea.classList.add("hidden");


    let html = "";


    Object.entries(data.problems).forEach(
        ([key, problem]) => {

            html += `

                <div
                    class="problem-card"
                    onclick="showAlgorithms('${type}', '${key}')"
                >

                    <div class="problem-number">
                        ${key.toUpperCase()}
                    </div>

                    <h3>
                        ${escapeHtml(problem.title)}
                    </h3>

                    <p>
                        ${escapeHtml(problem.description)}
                    </p>

                    <span class="problem-arrow">
                        Explore →
                    </span>

                </div>

            `;
        }
    );


    problemArea.innerHTML = `

        <div class="problem-grid">

            ${html}

        </div>

    `;


    explorer.classList.remove("hidden");


    explorer.scrollIntoView({
        behavior: "smooth",
        block: "start"
    });
}


/* =========================================
   03 / ALGORITHMS
========================================= */

function showAlgorithms(
    type,
    problemKey
) {

    const data =
        modelData[type];

    if (!data) {
        return;
    }


    const problem =
        data.problems[problemKey];

    if (!problem) {
        return;
    }


    const algorithmArea =
        document.getElementById(
            "algorithm-area"
        );

    const algorithmTitle =
        document.getElementById(
            "algorithm-title"
        );

    const algorithmGrid =
        document.getElementById(
            "algorithm-grid"
        );


    if (
        !algorithmArea ||
        !algorithmTitle ||
        !algorithmGrid
    ) {
        return;
    }


    algorithmTitle.textContent =
        problem.title +
        " ALGORITHMS";


    let html = "";


    problem.algorithms.forEach(
        algorithm => {

            const code =
                algorithm[0];

            const name =
                algorithm[1];

            const description =
                algorithm[2];


            const safeName =
                JSON.stringify(name);

            const safeType =
                JSON.stringify(type);

            const safeProblemKey =
                JSON.stringify(problemKey);


            html += `

                <div class="algorithm-card">

                    <div class="algorithm-code">
                        MODEL / ${code}
                    </div>

                    <h3>
                        ${escapeHtml(name)}
                    </h3>

                    <p>
                        ${escapeHtml(description)}
                    </p>

                    <button
                        type="button"
                        class="algorithm-button"
                        onclick='selectAlgorithm(
                            ${safeName},
                            ${safeType},
                            ${safeProblemKey}
                        )'
                    >
                        ANALYZE MODEL →
                    </button>

                </div>

            `;
        }
    );


    algorithmGrid.innerHTML =
        html;


    algorithmArea.classList.remove(
        "hidden"
    );


    setTimeout(() => {

        algorithmArea.scrollIntoView({
            behavior: "smooth",
            block: "start"
        });

    }, 100);
}


/* =========================================
   04 / SELECT ALGORITHM
========================================= */

function selectAlgorithm(
    name,
    learningType,
    problemKey
) {

    const analysis =
        document.getElementById(
            "analysis"
        );

    const model =
        document.getElementById(
            "analysis-model"
        );

    const problem =
        document.getElementById(
            "analysis-problem"
        );

    const selectedProblem =
        modelData[
            learningType
        ]?.problems?.[
            problemKey
        ];


    if (
        !analysis ||
        !model ||
        !problem ||
        !selectedProblem
    ) {
        return;
    }


    selectedAlgorithm =
        name;

    selectedLearningType =
        learningType;

    selectedProblemKey =
        problemKey;


    model.textContent =
        name;

    problem.textContent =
        selectedProblem.title;


    analysis.classList.remove(
        "hidden"
    );


    const results =
        document.getElementById(
            "project-results"
        );


    if (results) {

        results.classList.add(
            "hidden"
        );
    }


    const urlInput =
        document.getElementById(
            "project-url"
        );


    if (urlInput) {

        urlInput.value = "";
    }


    const csvInput =
        document.getElementById(
            "csv-file"
        );


    if (csvInput) {

        csvInput.value = "";
    }


    const status =
        document.getElementById(
            "connection-status"
        );


    if (status) {

        status.textContent = "";
    }


    setTimeout(() => {

        analysis.scrollIntoView({
            behavior: "smooth",
            block: "start"
        });

    }, 150);
}


/* =========================================
   CSV FILE SELECTION
========================================= */

function handleCSVChange() {

    const csvInput =
        document.getElementById(
            "csv-file"
        );

    const status =
        document.getElementById(
            "connection-status"
        );


    if (
        !csvInput ||
        !status
    ) {
        return;
    }


    if (
        !csvInput.files ||
        csvInput.files.length === 0
    ) {

        status.textContent = "";

        return;
    }


    const file =
        csvInput.files[0];


    if (
        !file.name
            .toLowerCase()
            .endsWith(".csv")
    ) {

        status.textContent =
            "PLEASE SELECT A CSV FILE.";

        csvInput.value = "";

        return;
    }


    status.textContent =
        "CSV READY: " +
        file.name;
}


/* =========================================
   04 / PROJECT ANALYSIS
========================================= */

async function analyzeProject() {

    const urlInput =
        document.getElementById(
            "project-url"
        );

    const algorithmElement =
        document.getElementById(
            "analysis-model"
        );

    const problemElement =
        document.getElementById(
            "analysis-problem"
        );

    const statusElement =
        document.getElementById(
            "connection-status"
        );

    const csvInput =
        document.getElementById(
            "csv-file"
        );


    if (
        !urlInput ||
        !algorithmElement ||
        !problemElement ||
        !statusElement
    ) {

        console.error(
            "Required ModelLens elements are missing."
        );

        return;
    }


    const url =
        urlInput.value.trim();


    const algorithm =
        selectedAlgorithm ||
        algorithmElement.textContent.trim() ||
        "Not selected";


    const problem =
        selectedProblemKey ||
        problemElement.textContent.trim() ||
        "Not selected";


    /* =====================================
       VALIDATE URL
    ===================================== */

    if (!url) {

        statusElement.textContent =
            "ENTER A PROJECT URL FIRST.";

        return;
    }


    if (
        !url.startsWith("http://") &&
        !url.startsWith("https://")
    ) {

        statusElement.textContent =
            "ENTER A COMPLETE PROJECT URL.";

        return;
    }


    /* =====================================
       VALIDATE CSV
    ===================================== */

    if (
        !csvInput ||
        !csvInput.files ||
        csvInput.files.length === 0
    ) {

        statusElement.textContent =
            "SELECT YOUR CSV DATASET FIRST.";

        return;
    }


    const csvFile =
        csvInput.files[0];


    if (
        !csvFile.name
            .toLowerCase()
            .endsWith(".csv")
    ) {

        statusElement.textContent =
            "ONLY CSV FILES ARE SUPPORTED.";

        return;
    }


    /* =====================================
       BUTTON LOADING STATE
    ===================================== */

    const analyzeButton =
        document.querySelector(
            ".analyze-button"
        );


    let originalButtonText =
        "";


    if (analyzeButton) {

        originalButtonText =
            analyzeButton.textContent;

        analyzeButton.textContent =
            "ANALYZING MODEL...";

        analyzeButton.disabled =
            true;
    }


    statusElement.textContent =
        "UPLOADING DATASET AND ANALYZING MODEL...";


    try {

        /* =================================
           CREATE FORM DATA
        ================================= */

        const formData =
            new FormData();


        formData.append(
            "project_url",
            url
        );


        formData.append(
            "learning_type",
            selectedLearningType
        );


        formData.append(
            "problem_type",
            selectedProblemKey
        );


        formData.append(
            "algorithm",
            selectedAlgorithm
        );


        formData.append(
            "file",
            csvFile
        );


        /* =================================
           SEND TO FASTAPI
        ================================= */

        const response =
            await fetch(
                "/api/analyze-model",
                {
                    method: "POST",
                    body: formData
                }
            );


        /* =================================
           READ SERVER RESPONSE
        ================================= */

        let result;

        try {

            result =
                await response.json();

        } catch (jsonError) {

            throw new Error(
                "SERVER RETURNED AN INVALID RESPONSE."
            );
        }


        /* =================================
           CHECK SERVER ERROR
        ================================= */

        if (!response.ok) {

            let errorMessage =
                "MODEL ANALYSIS FAILED.";

            if (result.detail) {

                if (
                    typeof result.detail ===
                    "string"
                ) {

                    errorMessage =
                        result.detail;

                } else {

                    errorMessage =
                        JSON.stringify(
                            result.detail
                        );
                }
            }


            throw new Error(
                errorMessage
            );
        }


        /* =================================
           SUCCESS
        ================================= */

        statusElement.textContent =
            "MODEL ANALYSIS COMPLETE.";


        /* =================================
           DISPLAY PROJECT INFORMATION
        ================================= */

        setText(
            "result-project",
            result.project_name ||
            getProjectName(url)
        );


        setText(
            "result-algorithm",
            result.algorithm ||
            algorithm
        );


        setText(
            "result-problem",
            result.problem ||
            problem
        );


        setText(
            "result-endpoints",
            result.api?.endpoint_count ??
            result.endpoints ??
            "1"
        );


        setText(
            "result-status",
            result.status ||
            "ANALYZED"
        );


        /* =================================
           PERFORMANCE METRICS
        ================================= */

        const metrics =
            result.metrics || {};


        if (
            selectedProblemKey ===
            "classification"
        ) {

            setText(
                "result-accuracy",
                formatMetric(
                    "Accuracy",
                    metrics.accuracy
                )
            );


            setText(
                "result-precision",
                formatMetric(
                    "Precision",
                    metrics.precision
                )
            );


            setText(
                "result-recall",
                formatMetric(
                    "Recall",
                    metrics.recall
                )
            );


            setText(
                "result-f1",
                formatMetric(
                    "F1 Score",
                    metrics.f1
                )
            );


            setText(
                "result-testing",
                formatMetric(
                    "Testing Score",
                    metrics.testing_score
                )
            );
        }


        else if (
            selectedProblemKey ===
            "regression"
        ) {

            setText(
                "result-accuracy",
                formatMetric(
                    "R²",
                    metrics.r2
                )
            );


            setText(
                "result-precision",
                formatValue(
                    "MAE",
                    metrics.mae
                )
            );


            setText(
                "result-recall",
                formatValue(
                    "MSE",
                    metrics.mse
                )
            );


            setText(
                "result-f1",
                formatValue(
                    "RMSE",
                    metrics.rmse
                )
            );


            setText(
                "result-testing",
                formatMetric(
                    "Testing Score",
                    metrics.testing_score
                )
            );
        }


        else if (
            selectedProblemKey ===
            "clustering"
        ) {

            setText(
                "result-accuracy",
                formatValue(
                    "Silhouette",
                    metrics.silhouette_score
                )
            );


            setText(
                "result-precision",
                formatValue(
                    "Davies-Bouldin",
                    metrics.davies_bouldin_score
                )
            );


            setText(
                "result-recall",
                formatValue(
                    "Clusters",
                    metrics.cluster_count
                )
            );


            setText(
                "result-f1",
                "UNSUPERVISED"
            );


            setText(
                "result-testing",
                "NO TARGET LABEL"
            );
        }


        else {

            setText(
                "result-accuracy",
                "ANALYZED"
            );


            setText(
                "result-precision",
                "N/A"
            );


            setText(
                "result-recall",
                "N/A"
            );


            setText(
                "result-f1",
                "N/A"
            );


            setText(
                "result-testing",
                "N/A"
            );
        }


        setText(
            "result-model-type",
            result.model_type ||
            selectedLearningType.toUpperCase()
        );


        /* =================================
           MODEL INFORMATION
        ================================= */

        setText(
            "detail-model-type",
            result.model_type ||
            algorithm
        );


        setText(
            "detail-problem",
            result.problem ||
            problem
        );


        setText(
            "detail-features",
            formatFeatureList(
                result.features
            )
        );


        setText(
            "detail-target",
            result.target ||
            "Not detected"
        );


        /* =================================
           API ANALYSIS
        ================================= */

        const api =
            result.api || {};


        setText(
            "api-endpoint-count",
            api.endpoint_count ??
            "1"
        );


        setText(
            "api-prediction",
            api.prediction_endpoint ||
            "/api/analyze-model"
        );


        setText(
            "api-documentation",
            api.documentation ||
            "FastAPI documentation available"
        );


        displayEndpointList(
            api.detected_endpoints
        );


        /* =================================
           MISSING ITEMS
        ================================= */

        displayList(
            "missing-items",
            result.missing_items
        );


        /* =================================
           IMPROVEMENTS
        ================================= */

        displayList(
            "improvement-items",
            result.improvements
        );


        /* =================================
           SUMMARY
        ================================= */

        setText(
            "analysis-summary",
            result.summary ||
            "ModelLens completed the model analysis successfully."
        );


        /* =================================
           SHOW REPORT
        ================================= */

        const results =
            document.getElementById(
                "project-results"
            );


        if (results) {

            results.classList.remove(
                "hidden"
            );


            setTimeout(() => {

                results.scrollIntoView({
                    behavior: "smooth",
                    block: "start"
                });

            }, 200);
        }
    }


    catch (error) {

        console.error(
            "ModelLens analysis error:",
            error
        );


        statusElement.textContent =
            "ANALYSIS FAILED: " +
            error.message;


        const results =
            document.getElementById(
                "project-results"
            );


        if (results) {

            results.classList.add(
                "hidden"
            );
        }
    }


    finally {

        /* =================================
           RESTORE BUTTON
        ================================= */

        if (analyzeButton) {

            analyzeButton.textContent =
                originalButtonText ||
                "ANALYZE MODEL →";

            analyzeButton.disabled =
                false;
        }
    }
}


/* =========================================
   HELPER: SET TEXT
========================================= */

function setText(
    elementId,
    value
) {

    const element =
        document.getElementById(
            elementId
        );


    if (!element) {
        return;
    }


    if (
        value === undefined ||
        value === null ||
        value === ""
    ) {

        element.textContent =
            "N/A";

        return;
    }


    element.textContent =
        value;
}


/* =========================================
   HELPER: FORMAT METRIC
========================================= */

function formatMetric(
    label,
    value
) {

    if (
        value === undefined ||
        value === null ||
        Number.isNaN(Number(value))
    ) {

        return label + ": N/A";
    }


    const number =
        Number(value);


    return (
        label +
        ": " +
        (number * 100).toFixed(2) +
        "%"
    );
}


/* =========================================
   HELPER: FORMAT NORMAL VALUE
========================================= */

function formatValue(
    label,
    value
) {

    if (
        value === undefined ||
        value === null ||
        Number.isNaN(Number(value))
    ) {

        return label + ": N/A";
    }


    return (
        label +
        ": " +
        Number(value).toFixed(4)
    );
}


/* =========================================
   HELPER: FEATURE LIST
========================================= */

function formatFeatureList(
    features
) {

    if (
        !features ||
        !Array.isArray(features) ||
        features.length === 0
    ) {

        return "Not detected";
    }


    return features.join(", ");
}


/* =========================================
   HELPER: ENDPOINT LIST
========================================= */

function displayEndpointList(
    endpoints
) {

    const element =
        document.getElementById(
            "detected-endpoints"
        );


    if (!element) {
        return;
    }


    element.innerHTML = "";


    if (
        !endpoints ||
        !Array.isArray(endpoints) ||
        endpoints.length === 0
    ) {

        element.innerHTML =
            "<li>No additional endpoints detected.</li>";

        return;
    }


    endpoints.forEach(
        endpoint => {

            const li =
                document.createElement(
                    "li"
                );


            li.textContent =
                endpoint;


            element.appendChild(
                li
            );
        }
    );
}


/* =========================================
   HELPER: DISPLAY LIST
========================================= */

function displayList(
    elementId,
    items
) {

    const element =
        document.getElementById(
            elementId
        );


    if (!element) {
        return;
    }


    element.innerHTML = "";


    if (
        !items ||
        !Array.isArray(items) ||
        items.length === 0
    ) {

        const li =
            document.createElement(
                "li"
            );


        li.textContent =
            "No major issues detected.";


        element.appendChild(
            li
        );


        return;
    }


    items.forEach(
        item => {

            const li =
                document.createElement(
                    "li"
                );


            li.textContent =
                item;


            element.appendChild(
                li
            );
        }
    );
}


/* =========================================
   HELPER: PROJECT NAME
========================================= */

function getProjectName(
    url
) {

    try {

        const parsedUrl =
            new URL(url);


        let hostname =
            parsedUrl.hostname;


        hostname =
            hostname.replace(
                /^www\./,
                ""
            );


        return hostname;

    } catch (error) {

        return "User Project";
    }
}


/* =========================================
   HELPER: ESCAPE HTML
========================================= */

function escapeHtml(
    value
) {

    if (
        value === undefined ||
        value === null
    ) {

        return "";
    }


    return String(value)
        .replace(
            /&/g,
            "&amp;"
        )
        .replace(
            /</g,
            "&lt;"
        )
        .replace(
            />/g,
            "&gt;"
        )
        .replace(
            /"/g,
            "&quot;"
        )
        .replace(
            /'/g,
            "&#039;"
        );
}


/* =========================================
   PAGE LOAD
========================================= */

document.addEventListener(
    "DOMContentLoaded",
    () => {

        const csvInput =
            document.getElementById(
                "csv-file"
            );


        if (csvInput) {

            csvInput.addEventListener(
                "change",
                handleCSVChange
            );
        }
    }
);
document.addEventListener("DOMContentLoaded", function () {

    const csvFile = document.getElementById("csv-file");
    const csvFileName = document.getElementById("csv-file-name");

    if (csvFile && csvFileName) {

        csvFile.addEventListener("change", function () {

            if (csvFile.files.length > 0) {
                csvFileName.textContent = csvFile.files[0].name;
            } else {
                csvFileName.textContent =
                    "Upload the dataset used to train your model";
            }

        });

    }

});