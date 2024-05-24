# Decomposing Vision-based LLM Predictions for Auto-Evaluation with GPT-4

This repository contains the code for decomposing vision-based LLM (Language and Vision) predictions using GPT-4. This is the partial code implementation of the "Paper Decomposing Vision-based LLM Predictions for Auto-Evaluation with GPT-4" by Zhu et al.

## Installation

To reproduce the work, follow these steps:

1. Install the required dependencies by running the following command:

    ```shell
    pip install openai streamlit
    ```
## Usage

1. Navigate to the project directory:

    ```shell
    cd Decomposing-GPT-4-Vision-based-LLM-Predictions
    ```
2. In this main.py file set the OpenAI API key
    ```python
    # Set the OpenAI API key
    os.environ['OPENAI_API_KEY'] = "sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    ```

3. Run the application:

    ```shell
    python -m streamlit run main.py
    ```