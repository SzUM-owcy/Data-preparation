# Plant Disease Recognition

The goal of this project is to develop a machine learning system for recognizing plant diseases, improving agricultural sustainability and food production by facilitating timely interventions. **Our trained model achieves an impressive accuracy of 90.04%**, making it a reliable tool for identifying healthy plants and distinguishing between powdery mildew and rust infections. This high performance demonstrates the model's potential to significantly aid in early disease detection and prevention.

## Description

### Plant Disease Classification

**Authors:**
- Krzysztof Nazar
- Hubert Nacmer
- Łukasz Kawa

**Final Report:**
The final report with a detailed analysis, methodologies, and results can be found [here](https://github.com/SzUM-owcy/Data-preparation/blob/main/Plant%20Disease%20Classification%20report.pdf).

The final report provides an in-depth analysis of the project, covering the following key aspects:
- **Introduction:** Overview of the importance of plant disease recognition in agriculture.
- **Methodology:** Detailed description of the data preprocessing steps, model architecture, training procedures, and evaluation metrics.
- **Results:** Comprehensive presentation of the model's performance metrics, including accuracy, precision, recall, and F1-score, along with confusion matrices.
- **Discussion:** Insights into the strengths and weaknesses of the model, potential improvements, and future work.
- **Conclusion:** Summary of findings and the impact of the project on agricultural practices.

### Problem Definition

The objective of the system is to accurately classify plant images into three categories: Healthy, Powdery, and Rust. Healthy plants exhibit no signs of disease, while powdery mildew and rust infections are characterized by distinct visual symptoms such as powdery white spots and rust-colored spores, respectively. The classification of plant diseases is crucial for implementing timely interventions and mitigating crop losses, ultimately enhancing agricultural sustainability and food production.

## Dataset
We utilize the Plant Disease Recognition dataset available on Kaggle. You can access the dataset [here](https://www.kaggle.com/datasets/rashikrahmanpritom/plant-disease-recognition-dataset?resource=download).

This dataset contains images of plants with three labels: "Healthy," "Powdery," and "Rust," indicating different plant conditions. In total, there are 1530 images split into train, test, and validation sets.

## Folder Structure
```
Data-preparation/
│   .gitignore 
│   Data preparation.ipynb
│   LICENSE
│   README.md
│
└───data/
    │
    ├── Test/
    │   ├── Healthy/
    │   ├── Powdery/
    │   └── Rust/
    │
    ├── Train/
    │   ├── Healthy/
    │   ├── Powdery/
    │   └── Rust/
    │
    └── Validation/
        ├── Healthy/
        ├── Powdery/
        └── Rust/
```



## Getting Started

### Prerequisites

Make sure you have the following software installed:
- Python 3.x
- Jupyter Notebook
- Necessary Python libraries (listed in `requirements.txt`)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/plant-disease-recognition.git
    cd plant-disease-recognition
    ```

2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Download the dataset from Kaggle and place it in the `data` directory as per the folder structure above.

## Usage

1. Open the Jupyter Notebook for data preparation:
    ```bash
    jupyter notebook "Data preparation.ipynb"
    ```

2. Follow the instructions in the notebook to preprocess the data and train the model.

### Evaluation Metrics

To evaluate the performance of the trained models, the following metrics are used:

- **Accuracy**: The ratio of correctly classified instances to the total number of instances.
- **Precision**: The proportion of true positive predictions among all positive predictions made by the model.
- **Recall**: The proportion of true positive predictions among all actual positive instances in the dataset.
- **F1-Score**: The harmonic mean of precision and recall, providing a comprehensive measure of the model's performance.
- **Confusion Matrices**: These offer insights into the types and frequencies of classification errors, helping to understand the model's strengths and weaknesses across different classes.

### Model Improvements

Several approaches were explored to improve the models, including:

1. **Increasing Epochs**: Training the model for more epochs to enhance performance. Metrics peaked at the 22nd epoch with the best results being:
    - Accuracy: 0.9004
    - Recall: 0.8995
    - Precision: 0.9031
    - F1-Score: 0.8982

2. **Grid Search (Batch Size)**: Experimenting with different batch sizes (8, 16, 32) to optimize model performance. The model with a batch size of 32 provided the best results on the test set.

### Machine Learning Methods and Models

We employed Convolutional Neural Networks (CNNs) for image classification, utilizing convolutional and pooling layers to extract features and reduce dimensionality. Categorical Crossentropy was used as the loss function, suitable for multi-class classification problems.

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING](CONTRIBUTING.md) file for details on the code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Kaggle for providing the [Plant Disease Recognition dataset](https://www.kaggle.com/datasets/rashikrahmanpritom/plant-disease-recognition-dataset?resource=download).
- All contributors to this project.

---

Feel free to further customize the content and add more details as needed.
