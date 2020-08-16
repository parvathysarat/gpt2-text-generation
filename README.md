# gpt2-text-generation

Fine tuning and text-generation using OpenAI's GPT-2 on blog data set from https://trustmeyourealive.wordpress.com/. 


```content-extraction``` : Extracting blog data using wordpress API <br>

```dataset``` : Train, validation, test datasets from extracted content <br>

```prepare_data.ipynb``` : Prepare data into train, valid, test files <br>

```text_generation.ipyb``` : Fine-tune GPT-2 on prepared train set and text generation  

### Dataset details:  

Total tokens : 246446 (76 articles)   
Vocabulary : 50260  
Training set(by line) :2752  

Code files in ```transformers``` that need to be replaced after cloning: ```run_generation.py``` and ```run_language_modeling.py``` (instructions in text_generation.ipynb)

### Generated sequences 

Frankly, I am in awe/shock - these sequences truly sound like me, and I'm quite relieved GPT-3 hasn't been open sourced (yet):

1. <BOS> Its the moment that leaves you with the most anxiety.   
2. <BOS> There are still days left until the end of our semester - it is Saturday.   
3. <BOS> But my brother and I know each other, we also know he always wears a green t-shirt and grey jeans with green-ish socks that cover a half-inch under his left thigh.   
4. <BOS> I've always wanted to be a part of society, or a part of people.   
5. <BOS> It takes less than 5 minutes for an hour (and sometimes even longer if you leave home).
