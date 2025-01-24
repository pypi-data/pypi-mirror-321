# Azure GenAI Utils

This repository contains a set of utilities for working with Azure GenAI. The utilities are written in Python and are designed to be used for Hackathons, Workshops, and other events where you need to quickly get started with Azure GenAI.

## Requirements
- Azure Subscription
- Bing Search API Key
- Python 3.8 or later

## Installation
`pip install azure-genai-utils`

## Usage 
### Bing Search
```
from azure_genai_utils.tools import BingSearch
from dotenv import load_dotenv

# You need to add BING_SUBSCRIPTION_KEY=xxxx in .env file
load_dotenv()

# Basic usage
bing = BingSearch(max_results=2, locale="ko-KR")
results = bing.invoke("마이크로소프트 오토젠")
print(results)

## Include news search results and format output
bing = BingSearch(
    max_results=2,
    locale="ko-KR",
    include_news=True,
    include_entity=False,
    format_output=True,
)
results = bing.invoke("마이크로소프트 오토젠")
print(results)
```

### Synthetic Data Generation
```
from azure_genai_utils.synthetic.qa_generator import QADataGenerator, CustomQADataGenerator, QAType

model_config = {
    "deployment": "gpt-4o-mini",
    "model": "gpt-4o-mini",
    "max_tokens": 256,
}

qa_generator = QADataGenerator(model_config=model_config)

# qa_generator = CustomQADataGenerator(
#     model_config=model_config, templates_dir=f"./synthetic/prompt_templates/ko"
# )

import asyncio
from typing import Dict

concurrency = 3  # number of concurrent calls
sem = asyncio.Semaphore(concurrency)

qa_type = QAType.LONG_ANSWER

input_batch = [
    "The quick brown fox jumps over the lazy dog.",
    "1+1=2",
    "What is the capital of France?",
]


async def generate_async(text: str) -> Dict:
    async with sem:
        return await qa_generator.generate_async(
            text=text,
            qa_type=qa_type,
            num_questions=3,  # Number of questions to generate per text
        )


results = await asyncio.gather(
    *[generate_async(text) for text in input_batch], return_exceptions=True
)

qna_list = []

for result in results:
    if isinstance(result, Exception):
        raise result  # exception raised inside generate_async()
    qna_list.append(result["question_answers"])

print("Successfully generated QAs")
print(qna_list)
```

## License Summary
This sample code is provided under the Apache 2.0 license. See the LICENSE file.