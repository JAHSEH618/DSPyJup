import dspy
import os

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"))

class QA(dspy.Signature):
    question: str = dspy.InputField()
    history: dspy.History = dspy.InputField()
    answer: str = dspy.OutputField()

predict = dspy.Predict(QA)
history = dspy.History(messages=[])

predict.demos.append(
    dspy.Example(
        question="What is the capital of France?",
        history=dspy.History(
            messages=[
                {"question": "What is the capital of Germany?"},
                {"question": "What is the capital of Germany?", "answer": "Berlin"},
            ]
        ),
        answer="Paris",
    )
)

predict(question="What id the capital of America?", history=dspy.History(messages=[]))
dspy.inspect_history()