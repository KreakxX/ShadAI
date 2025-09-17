import os
import requests

prompts = set()
codes = []

for i in range(100):
    print(i)
    while True:
        PromptResponse = requests.post(
        "http://localhost:11434/api/generate",
        json={
        "model": "phi3:3.8b",
        "prompt": """
        Create ONE unique React button description.s
        Return ONLY valid JSON in this format, no extra text:

        {
        "component": "button",
        "bg": "<Tailwind color like bg-red-500>",
        "special": "<one style like rounded, rounded-full, shadow>",
        "label": "<short label text>"
        }

        Rules:
        - Do NOT add explanations or text outside the JSON.
        - Keep it concise.
        """,
        "stream": False
        }
        )

        data = PromptResponse.json()
        raw = data["response"]
        raw = raw.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()

        import json
        try:
            prompt_obj = json.loads(raw)   
            prompt = f" {prompt_obj['component']},  {prompt_obj['bg']},  {prompt_obj['special']}, label: {prompt_obj['label']}"
            if prompt not in prompts:
                prompts.add(prompt)
                break
        except:
            print("failed")

    CodeResponse = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "deepseek-coder-v2:16b",
        "prompt": f"""
    Generate **only** the React button code based on this prompt:

    {prompt}

    Rules:
    - Use Tailwind CSS for styling.
    - Only output the <button> element in this exact format: <button className="">Label</button> No explanation or Text before just keep it simple and output the Code directly
    - Do NOT include imports, React component wrappers, markdown, comments, or extra text like ``` or jsx or html before the code very Important .
    - Map the structured fields to Tailwind classes:
    - bg color → bg-color (Tailwind)
    - special → e.g. rounded, rounded-full, shadow
    - label → the inner text of the button
    """,
    "stream" : False
    }
    )
    try:
        CodeData = CodeResponse.json()
        Code = CodeData["response"]
    except:
        print("failed 2")
    Code = Code.strip().removeprefix("jsx").removeprefix("html").removeprefix("```json").removeprefix("```").removeprefix("```jsx").removesuffix("```").strip()

    if("jsx" in Code):
        Code = Code[3:].strip()
    Code.replace("`","")

    if("html" in Code):
        Code = Code[4:].strip()

    codes.append(Code)
    print("->->->->->->")
    print(prompt)
    print("-----------")
    print(Code)

PromptPath = os.path.join("Dataset", "prompts")
CodePath = os.path.join("Dataset","Code")

for i, prompt in enumerate(prompts, start=1):
    file_path = os.path.join(PromptPath, f"{i}.txt")
    with open(file_path, "w") as f:
        f.write(prompt)

for i, code in enumerate(codes,start=1):
    file_path = os.path.join(CodePath, f"{i}.txt")
    with open(file_path, "w") as f:
        f.write(code)