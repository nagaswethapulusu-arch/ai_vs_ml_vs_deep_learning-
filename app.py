import pandas as pd
import streamlit as st

st.title("AI vs Machine Learning vs Deep Learning")
st.write("A simple comparison using definitions, a comparison table, real-world examples and how they are related.")

comparison = {
    "Aspect": [
        "Definition", "Scope", "How it works", "Data needed", "Feature engineering",
        "Hardware", "Training time", "Explainability", "Common techniques", "Real-world examples",
    ],
    "Artificial Intelligence": [
        "Machines that imitate human intelligence",
        "Broadest field",
        "Rules, search, logic, or learning",
        "Can work with little or no data (rule-based)",
        "Rules written by humans",
        "Normal computer is enough for simple systems",
        "None for rule-based systems",
        "Rule-based systems are easy to explain",
        "Expert systems, search algorithms, rule engines",
        "Chess program, rule-based customer support bot",
    ],
    "Machine Learning": [
        "Systems that learn patterns from data",
        "Subset of AI",
        "Learns from data to predict or decide",
        "Needs a good amount of data",
        "Humans usually choose the features",
        "Normal computer or CPU is usually enough",
        "Minutes to hours",
        "Often easier to explain (for example decision trees)",
        "Linear regression, decision trees, random forest, SVM",
        "Spam filter, recommendation system, house price prediction",
    ],
    "Deep Learning": [
        "ML using multi-layer neural networks",
        "Subset of ML",
        "Neural networks learn features on their own",
        "Needs a very large amount of data",
        "Features are learned automatically",
        "Needs a GPU for large models",
        "Hours to days or more",
        "Hard to explain (black box)",
        "CNN, RNN, Transformer",
        "Face recognition, voice assistants, self-driving perception, chatbots",
    ],
}
df = pd.DataFrame(comparison)

examples = {
    "Artificial Intelligence": ["Chess program using fixed rules", "Customer support bot with scripted answers", "Automatic traffic signal timing"],
    "Machine Learning": ["Email spam filter", "Movie and product recommendation systems", "Predicting house prices from past sales"],
    "Deep Learning": ["Face and image recognition", "Voice assistants (speech recognition)", "Language translation and chatbots"],
}

definitions = {
    "Artificial Intelligence": "The broad field of building machines that can perform tasks that normally need human intelligence, such as reasoning, problem solving, understanding language and recognising images.",
    "Machine Learning": "A subset of AI where a system learns patterns from data instead of following fixed rules, then uses them to make predictions or decisions.",
    "Deep Learning": "A subset of ML that uses neural networks with many layers to learn features from raw data such as images, audio and text.",
}

tab_def, tab_table, tab_examples, tab_relation = st.tabs(["Definitions", "Comparison table", "Examples", "How they are related"])

with tab_def:
    for name, text in definitions.items():
        st.subheader(name)
        st.write(text)

with tab_table:
    st.table(df.set_index("Aspect"))

with tab_examples:
    choice = st.radio("Choose a field", list(examples.keys()), horizontal=True)
    for item in examples[choice]:
        st.write("- " + item)

with tab_relation:
    st.code(
        "+--------------------------------------------------+\n"
        "|  Artificial Intelligence (AI)                    |\n"
        "|   +------------------------------------------+   |\n"
        "|   |  Machine Learning (ML)                   |   |\n"
        "|   |   +----------------------------------+   |   |\n"
        "|   |   |  Deep Learning (DL)              |   |   |\n"
        "|   |   +----------------------------------+   |   |\n"
        "|   +------------------------------------------+   |\n"
        "+--------------------------------------------------+",
        language=None,
    )
    st.write("AI is the broader field. ML is one way to achieve AI by learning from data. DL is one way to do ML using deep neural networks.")
    st.write("Every deep learning system is a machine learning system, and every machine learning system is an AI system, but not the other way round. A simple rule-based chess program is AI but not ML.")
