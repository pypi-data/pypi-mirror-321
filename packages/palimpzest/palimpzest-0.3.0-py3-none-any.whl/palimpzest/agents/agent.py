from __future__ import annotations

from palimpzest.sets import Dataset
from typing import Any, List, Optional, Union

import palimpzest as pz

# NOTE: THINK LOW-LEVEL
# what are the abstractions that support many agent systems?
# do NOT create high-level agents (e.g. RAGAgent, ToolAgent, etc.)
# do NOT bake-in communication patterns (e.g. guardrails, summarization, etc.)
# find the general subset of operations and optimize those

# TODO: implement the following applications:
# - plain-old RAG agent (find emails in enron)
# - tool use agent ()
# - mixture of agents (see paper for example)
# - multi-agent system w/non-deterministic compute (e.g. backtrack if need be)


# class Agent:
#     def __init__(self, instruction: str):
#         self.instruction = instruction

#     # def __call__(self, input: pz.Dataset, prompt: Optional[str]=None):
#     #     prompt = (
#     #         f"You are a helpful assistant with the following instruction:\n\nInstruction {self.instruction}"
#     #         if prompt is None
#     #         else prompt
#     #     )

#     def retrieve(self, input: pz.Dataset, k: int) -> pz.Dataset:
#         assert self.resources is not None, "Need to provide a vector store for retrieval"
#         for record in input:
#             documents = self.resources.retrieve(record, k=k)
#             prompt = f"""
#               Given the input {input.__class__.__name__} and documents provided in the following context, execute the following instruction:
#               Input {record}
#               Context: {documents}
#               Instruction: {self.instruction}
#             """
#             # ... invoke LLM

#     def rerank(self, input: pz.Dataset) -> pz.Dataset:
#         for record in input:
#             prompt = f"""
#                 Given the input {input.__class__.__name__} rank the input according to the following instruction:
#                 Input {record}
#                 Instruction {self.instruction}
#             """
#             # ... invoke LLM 


class Agent:
    def __init__(self, instruction: str, schema: pz.Schema, retriever: Optional[Retriever]=None):
        self.instruction = instruction
        self.schema = schema
        self.retriever = retriever

    def __call__(self, input: Union[pz.Dataset, List[pz.Dataset]]) -> pz.Dataset:
        # handle aggregation in MoA example
        if type(input) == type([]):
            intermediates = []
            for input_ds in input:
                inter_ds = pz.Dataset(source=input_ds, schema=self.schema)
                intermediates.append(inter_ds)
            # NOTE: the Dataset construction below supposes a pz.Join logical operator
            return pz.Dataset(source=intermediates, schema=self.schema)

        return pz.Dataset(source=input, schema=self.schema, retriever=self.retriever)

#### Single-Layer Mixture of Agents for Question Answering ####
# construct schemas
class Question(pz.Schema):
    question = pz.StringField("The question which needs to be answered.")

class Answer(pz.Schema):
    answer = pz.StringField("The answer to the given question")

# construct agents
prop_agents = [Agent(instruction="Answer the given Question to the best of your ability", schema=Answer) for _ in range(5)]
agg_agent = [Agent(instruction="Summarize the provided answers into a single, concise answer", Schema=Answer)]

# construct logical plan
questions = pz.Dataset("questions", schema=Question)
prop_answers = []
for prop_agent in prop_agents:
    prop_answers = prop_agent(questions)
final_answers = agg_agent(prop_answers)

#### RAG agent for synthesizing code ####
import chromadb

class Retriever:
    def __init__(self, source: Any, collection_name: Optional[str]):
        self.source = source
        self.collection_name = collection_name

    def retrieve(self, query: str, k: int) -> List[pz.TextFile]:
        # query and k are provided by the physical operator which will ultimately invoke this method;
        # thus, k can be parameterized by the PhysicalPlanner
        files = None
        if type(self.source) == chromadb.PersistentClient:
            collection = self.source.get_or_create_collection(name=self.collection_name)
            files = collection.query(query_texts=[query], n_results=k)
        else:
            raise Exception("Not implemented yet")
            
        return files

# construct schemas
class UserInput(pz.Schema):
    user_input = pz.StringField("Text from the user describing what code they wish to edit or add to the codebase")

class CodeDiff(pz.Schema):
    code_diff = pz.StringField("Code diff to be appplied to the code base to satisfy the user's request")
    code_filename = pz.StringField("The file to apply the code diff to")
    code_start_line_number = pz.NumericField("The line at which to apply the code diff")

# construct agents
codegen_agent = Agent(
    instruction=""""
        Take the given UserInput and any related code files and produce a
        code diff. making the change(s) or addition(s) request by the user.
    """,
    retriever=Retriever(
        source=chromadb.PersistentClient(path="/path/to/vectorstore"), # could also specify source="path/to/code/"
        collection_name="codebase",
    ),
    schema=CodeDiff,
)

# construct logical plan
user_inputs = pz.Dataset("user_inputs", schema=UserInput)
code_diffs = codegen_agent(user_inputs)



#### An example of a PyTorch direction for PZ ####
import palimpzest as pz
from palimpzest.operators import convert, filter, join
from palimpzest.foundations import BaseAgent

class ProposerAgent(BaseAgent):
    def __init__(self, instruction: str):
        self.instruction = instruction

    def __call__(self, input: pz.Dataset, outputSchema: pz.Schema):
        return convert(input, desc=self.instruction, schema=outputSchema)

class AggregatorAgent(BaseAgent):
    def __init__(self, instruction: str):
        self.instruction = instruction

    def __call__(self, inputs: List[pz.Dataset], outputSchema: pz.Schema):
        agg_input = join(inputs)
        final_output = convert(agg_input, desc=self.instruction, schema=outputSchema)
        for record in final_output:
            if record.contains(self.bad_words):
                final_output = convert(agg_input, desc=self.instruction, schema=outputSchema)

        return final_output

# construct schemas
class Question(pz.Schema):
    question = pz.StringField("The question which needs to be answered.")

class Answer(pz.Schema):
    answer = pz.StringField("The answer to the given question")

# construct agents
prop_agents = [ProposerAgent(instruction="Answer the given Question to the best of your ability") for _ in range(5)]
agg_agent = [Agent(instruction="Summarize the provided answers into a single, concise answer")]

# construct logical plan
questions = pz.Dataset("questions", schema=Question)
prop_answers = []
for prop_agent in prop_agents:
    prop_answers = prop_agent(questions, outputSchema=Answer)
final_answers = agg_agent(prop_answers, outputSchema=Answer)

# execute the plan
results = pz.Execute(final_answers)


# ### defined in primitives.py ###
# def convert(input: pz.Dataset, ..., schema: pz.Schema):
#   # pz.Dataset maintains a list of the logical operations applied
#   input.ops.append(ConvertScan(input.schema, schema, ...))

#   # the list above will ultimately comprise the logical plan that we optimize

#   # then, to make the code physically function at compile time
#   for record in input:
#     for field in schema.fieldNames():
#       if isinstance(field, pz.StringField):
#         setattr(record, field, "")
#       if isinstance(field, pz.NumericField):
#         setattr(record, field, 0)
#       # ...

#   return input


# ### Defined by the user ###
# class ProposerAgent(BaseAgent):
#     def __init__(self, instruction: str):
#         self.instruction = instruction

#     def __call__(self, input: pz.Dataset, outputSchema: pz.Schema):
#         answer_records = convert(input, desc=self.instruction, schema=outputSchema)
#         for record in answer_records:
#              for bad_word in self.bad_words:
#                  record.answer = answer_record.answer.replace(bad_word, "MIT")
#         return answer_records


# # construct schemas
# class Question(pz.Schema):
#     question = pz.StringField("The question which needs to be answered.")

# class Answer(pz.Schema):
#     answer = pz.StringField("The answer to the given question")

# # construct agent
# prop_agent = ProposerAgent(instruction="answer the question")

# # construct logical plan
# questions = pz.Dataset("questions", schema=Question)
# answers = prop_agent(questions)

# # compile logical plan
# plan = pz.Compile(answers)

# # execute compiled plan (and obviously improve after getting sample data) 
# results = pz.Execute(plan)