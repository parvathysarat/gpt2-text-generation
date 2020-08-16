# gpt2-text-generation

Fine tuning and text-generation using OpenAI's GPT-2 on blog data set. 

```content-extraction``` : Extracting blog data using wordpress API <br>

```dataset``` : Train, validation, test datasets from extracted content <br>

```prepare_data.ipynb``` : Prepare data into train, valid, test files <br>

```text_generation.ipyb``` : Fine-tune GPT-2 on prepared train set and text generation  

Code files in ```transformers``` that need to be replaced: ```run_generation.py``` and ```run_language_modeling.py``` (instructions in text_generation.ipynb)
