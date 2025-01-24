# Why is this library called fruitstand?

Because we’re comparing apples and oranges! Most testing involves checking that a value returned from a function is the same as what is expected. This doesn’t work when working with LLMs, as they are nondeterministic. Therefore, you need to check that there is a threshold of similarity.

# Why would I want to use this library?

If you’re using a particular LLM model prompt to determine an action based on the response, you may want to ensure that a response has a certain similarity when transitioning between models. This library allows you to set a baseline with the current model and verify that upgrading or changing models maintains the same behavior.

For example, you are using an LLM to do intent detection for your chatbot. You have a prompt like this:

```
Based on the provided user prompt, determine if the user wanted to:
1. Change their address
2. Change their name
3. Cancel their subscription

User Prompt:
I would like to update my subscription.
```

Using fruitstand will ensure that the LLM routes to the correct intent as you upgrade/change your llm/model.

# Using fruitstand

There are two steps to running tests using Fruitstand. The first step is creating a baseline, which runs queries against a specific LLM and model. If you are currently using an LLM with a specific model, this should be your baseline. Creating a baseline allows you to ensure that if you switch models, you can expect similar responses. Doing this promptly will also help you test for model degradation.

Once you have your baseline, you can test other LLMs and models against it. These tests will ensure that you can switch models without negatively impacting any developed functionality.

## Running Fruitstand via Command Line

### Baseline

#### Arguments:

- -f, --filename: File containing test data (required).
- -o, --output: Directory to store baseline data (required).
- -qllm: LLM to generate baseline queries for (required). # 'openai' | 'anthropic'| 'gemini'
- -qm, --model: Model for the query LLM (required). e.g. 'gpt-4o-mini'
- -qkey: API key for querying the LLM (required).
- -ellm: LLM for generating embeddings (required). # 'openai' | 'gemini'
- -em: Model for generating embeddings (required). # e.g. 'text-embedding-3-large'
- -ekey: API key for the embeddings LLM (required).

#### Example

```
fruitstand baseline -o ./baseline -f ./data/test_data.json -qllm openai -qm "gpt-4o-mini" -qkey sk-******** -ellm openai -em text-embedding-3-large -ekey sk--********
```

### Test

#### Arguments:

- -b, --baseline: File containing baseline data (required).
- -f, --filename: File containing test data (required).
- -o, --output: Directory to store test results (required).
- -llm: LLM to run queries against (required). # 'openai' | 'anthropic' | 'gemini'
- -m, --model: Model for the query LLM (required). # e.g. 'gpt-4o-mini'
- -qkey: API key for querying the LLM (required).
- -ekey: API key for the embeddings LLM (must match baseline’s embeddings LLM) (required).
- -threshold: Similarity threshold to determine test success (required, float).

#### Example

```
fruitstand test -b ./baseline/baseline__openai_gpt-4o-mini__openai_text-embedding-3-large__1736980847061344.json -o ./test_results data -f ./data/test_data.json -llm openai -m "gpt-4o-mini" -qkey sk-******** -ekey sk--******** -threshold 0.85
```

## Example Usage in Python

Below is an example of how to use the Fruitstand library directly in Python to create a baseline and run tests.

### Creating a Baseline

```
from fruitstand import Fruitstand

fruitstand = Fruitstand()

openai_api_key = "your_openai_api_key"

baseline_data = fruitstand.baseline(
    query_llm="openai",
    query_api_key=openai_api_key,
    query_model="gpt-4o-mini",
    embeddings_llm="openai",
    embeddings_api_key=openai_api_key,
    embeddings_model="text-embedding-3-large",
    data=[
        "How far is the earth from the sun?",
        "Where is Manchester in the UK?"
    ]
)

print("Baseline data:", baseline_data)
```

### Running Tests

```
test_data = fruitstand.test(
    test_query_llm="openai",
    test_query_api_key=openai_api_key,
    test_query_model="gpt-4o-mini",
    baseline_embeddings_api_key=openai_api_key,
    baseline_data=baseline_data,
    test_data=[
        "How far is the earth from the sun?",
        "Where is Manchester in the UK?"
    ],
    success_threshold=0.85
)

print("Test data:", test_data)
```
