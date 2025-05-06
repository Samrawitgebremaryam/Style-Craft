"""
Advanced prompt templates for The Writer's Lens.
Implements various prompt engineering techniques including:
- Few-shot learning
- Chain-of-thought prompting
- Role-based prompting
- Structured output formatting
"""

from typing import Dict, List, Optional

class PromptTemplate:
    def __init__(self, author: str, style_context: str):
        self.author = author
        self.style_context = style_context
        self.few_shot_examples = self._get_few_shot_examples()
        
    def _get_few_shot_examples(self) -> List[Dict[str, str]]:
        """Get few-shot examples for the selected author."""
        # This would be populated with actual examples
        return [
            {
                "input": "Write about a sunset",
                "output": "Example output in author's style"
            }
        ]
    
    def format_few_shot_prompt(self, user_input: str) -> str:
        """Format prompt with few-shot examples."""
        examples = "\n\n".join([
            f"Input: {ex['input']}\nOutput: {ex['output']}"
            for ex in self.few_shot_examples
        ])
        
        return f"""You are {self.author}. Your writing style is characterized by: {self.style_context}

Here are some examples of my writing style:

{examples}

Now, please write about: {user_input}

Let's break this down step by step:
1. First, consider the key themes and emotions
2. Then, structure the narrative
3. Finally, write in my distinctive style

Your response:"""

    def format_chain_of_thought(self, user_input: str) -> str:
        """Format prompt with chain-of-thought reasoning."""
        return f"""You are {self.author}. Your writing style is characterized by: {self.style_context}

Let's write about: {user_input}

First, let's think through this step by step:

1. What are the key themes and emotions to convey?
2. How would I typically structure this narrative?
3. What distinctive stylistic elements should I include?
4. How can I maintain my unique voice throughout?

Now, write the response incorporating these elements:"""

    def format_role_based(self, user_input: str) -> str:
        """Format prompt with enhanced role-based context."""
        return f"""You are {self.author}, a master of literary craft. Your writing is known for: {self.style_context}

As {self.author}, you are known for your:
- Unique narrative voice
- Distinctive thematic elements
- Characteristic stylistic choices
- Signature literary devices

Now, write about: {user_input}

Remember to maintain your authentic voice and style throughout the response."""

def get_prompt_template(author: str, style_context: str, technique: str = "few_shot") -> str:
    """Get formatted prompt based on selected technique."""
    template = PromptTemplate(author, style_context)
    
    techniques = {
        "few_shot": template.format_few_shot_prompt,
        "chain_of_thought": template.format_chain_of_thought,
        "role_based": template.format_role_based
    }
    
    return techniques.get(technique, template.format_few_shot_prompt) 