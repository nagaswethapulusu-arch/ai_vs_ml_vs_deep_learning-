# AI vs Machine Learning vs Deep Learning

A beginner-friendly project that compares **Artificial Intelligence (AI)**, **Machine Learning (ML)** and **Deep Learning (DL)** using definitions, a comparison table, real-world examples and an explanation of how they are related.

## Objective

Build a clear understanding of the relationship between AI, ML, and Deep Learning.

## Tools Used

- Python 3
- Jupyter Notebook
- Markdown
- Pandas (for the comparison table)
- Streamlit (for the live demo)

## Dataset

No dataset is required.

## Definitions

- **Artificial Intelligence (AI):** the broad field of building machines that can perform tasks that normally need human intelligence, such as reasoning, problem solving, understanding language and recognising images.
- **Machine Learning (ML):** a subset of AI where a system learns patterns from data instead of following fixed rules, then uses them to make predictions or decisions.
- **Deep Learning (DL):** a subset of ML that uses neural networks with many layers to learn features from raw data such as images, audio and text.

## Relationship

```
+--------------------------------------------------+
|  Artificial Intelligence (AI)                    |
|   +------------------------------------------+   |
|   |  Machine Learning (ML)                   |   |
|   |   +----------------------------------+   |   |
|   |   |  Deep Learning (DL)              |   |   |
|   |   +----------------------------------+   |   |
|   +------------------------------------------+   |
+--------------------------------------------------+
```

Every deep learning system is a machine learning system, and every machine learning system is an AI system, but not the other way round. A simple rule-based chess program is AI but not ML.

## Comparison Table

| Aspect | Artificial Intelligence | Machine Learning | Deep Learning |
|--------|------------------------|------------------|---------------|
| **Definition** | Machines that imitate human intelligence | Systems that learn patterns from data | ML using multi-layer neural networks |
| **Scope** | Broadest field | Subset of AI | Subset of ML |
| **How it works** | Rules, search, logic, or learning | Learns from data to predict or decide | Neural networks learn features on their own |
| **Data needed** | Can work with little or no data (rule-based) | Needs a good amount of data | Needs a very large amount of data |
| **Feature engineering** | Rules written by humans | Humans usually choose the features | Features are learned automatically |
| **Hardware** | Normal computer is enough for simple systems | Normal computer or CPU is usually enough | Needs a GPU for large models |
| **Training time** | None for rule-based systems | Minutes to hours | Hours to days or more |
| **Explainability** | Rule-based systems are easy to explain | Often easier to explain (for example decision trees) | Hard to explain (black box) |
| **Common techniques** | Expert systems, search algorithms, rule engines | Linear regression, decision trees, random forest, SVM | CNN, RNN, Transformer |
| **Real-world examples** | Chess program, rule-based customer support bot | Spam filter, recommendation system, house price prediction | Face recognition, voice assistants, self-driving perception, chatbots |

## Real-World Examples

| Field | Examples |
|-------|----------|
| **AI (rule-based)** | Chess program using fixed rules, customer support bot with scripted answers, automatic traffic signal timing |
| **Machine Learning** | Email spam filter, movie and product recommendation systems, predicting house prices from past sales |
| **Deep Learning** | Face and image recognition, voice assistants (speech recognition), language translation and chatbots |

## Approach

1. **Define** each term in simple words.
2. **Compare** them in a table using the same aspects for all three (scope, data needed, hardware, explainability, techniques, examples).
3. **Give real-world examples** for each, including recommendation systems and image recognition.
4. **Explain the relationship** using nested circles: AI contains ML, and ML contains DL.
5. **Build the table with Pandas** in the notebook, and show the same content in an interactive Streamlit app.

## How to Run

1. Install Python, Jupyter Notebook and Pandas:
   ```
   pip install notebook pandas
   ```
2. Clone or download this repository.
3. Open a terminal in the project folder and run:
   ```
   python -m notebook
   ```
4. Open `ai_vs_ml_vs_deep_learning.ipynb`.
5. Run all cells from top to bottom (`Shift + Enter`).

## Limitations

- The table simplifies each topic. Real systems can mix approaches, for example a product that uses rules, classic ML and deep learning together.
- Examples are illustrative and not an exhaustive list.

## Possible Improvements

- Add a fourth level for Generative AI.
- Add a small code demo, such as a rule-based program vs a simple ML model.
- Add images or diagrams for neural networks.

## Author

SwethaPulusu
