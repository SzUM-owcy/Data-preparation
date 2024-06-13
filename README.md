# Plant Disease Recognition

The goal of this project is to develop a machine learning system for recognizing plant diseases.

## Description

### Plant Disease Classification

**Authors:**
- Krzysztof Nazar
- Hubert Nacmer
- Łukasz Kawa

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

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING](CONTRIBUTING.md) file for details on the code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Kaggle for providing the [Plant Disease Recognition dataset](https://www.kaggle.com/datasets/rashikrahmanpritom/plant-disease-recognition-dataset?resource=download).
- All contributors to this project.

---

Feel free to further customize the content and add more details as needed.
