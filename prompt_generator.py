from langchain_core.prompts import PromptTemplate

# --- Prompt Template ---
template = PromptTemplate(
    template=
    """
    You are a Senior Research Scientist. 
    Analyze the following topic/paper: {paper_input}
    
    Constraints:
    - Writing Style: {style}
    - Detail Level: {length}

    Please provide the output in this EXACT format:
    
    ## 📌 Executive Summary
    (Provide a high-level overview)
    
    ## 📖 Core Concepts
    (Explain the main ideas and methodology in bullet points)
    
    ## 💡 Why It Matters
    (Explain the real-world significance and applications)
    
    ## 🚀 Future Implications
    (Predict how this will evolve in the next 5 years)
    """,
    input_variables=["paper_input", "style", "length"]
)
# Prompt Template

template.save("template.json")