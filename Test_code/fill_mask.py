from transformers import pipeline
model=pipeline('fill-mask',model='bert-base-uncased')
sentence="Python is the [MASK] language in the world."
result=model(sentence)
for r in result:
    print(f"Option: {r['token_str']}, Score: {r['score']:.4f}")
    print({sentence.replace('[MASK]', r['token_str'])})