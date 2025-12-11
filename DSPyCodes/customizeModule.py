import dspy
import os

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"))

"""Example code piece
class MyProgram(dspy.Module):
    
    # 构造器
    def __init__(self, ...):
        # Define attributes and sub-modules here
        {constructor_code}

    # 包含了自定义的DSPy Module的核心逻辑
    def forward(self, input_name1, input_name2, ...):
        # Implement your program's logic here
        {custom_logic_code}
"""
class QueryGenerator(dspy.Signature):
    """Generate a query based on question to fetch relevant context"""
    question: str = dspy.InputField()
    query: str = dspy.OutputField()

def search_wikipedia(query: str) -> list[str]:
    """Query ColBERT endpoint, which is a knowledge source based on wikipedia data"""
    results = dspy.ColBERTv2(url='http://20.102.90.50:2017/wiki17_abstracts')(query)
    return [x["text"] for x in results]

class RAG(dspy.Module):
    def __init__(self):
        self.query_generator = dspy.Predict(QueryGenerator)
        self.answer_generator = dspy.ChainOfThought("question,context->answer")

    def forward(self, question, **kwargs):
        query = self.query_generator(question=question).query
        context = search_wikipedia(query)[0]
        return self.answer_generator(question=question, context=context).answer

rag = RAG()
print(rag(question="Is Lebron James the basketball GOAT?"))