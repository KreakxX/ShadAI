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
        Create ONE unique React button description.
        Return ONLY valid JSON in this format, no extra text:
        
        {
        "component": "button",
        "bg": "<single Tailwind background color like bg-red-500, bg-blue-600, bg-green-400>",
        "special": "<EXACTLY ONE style: rounded OR rounded-full OR shadow OR border OR none>",
        "label": "<short button text like Save, Cancel, Submit>"
        }
        
        Critical Rules:
        - Use EXACTLY ONE special style, never combine multiple
        - If special is "none", use literally "none"
        - Background must be a valid Tailwind bg-color class
        - Return pure JSON only, no explanations
        - No markdown formatting or extra text
        """,
        "stream": False
        }
        )
                
        import json
        try:
            data = PromptResponse.json()
            raw = data["response"]
            raw = raw.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
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
Generate React button code based EXACTLY on this prompt:

{prompt}

STRICT Rules:
- Use ONLY the classes specified in the prompt
- If bg is specified → use that exact Tailwind background class
- If special is "rounded" → add "rounded-lg" Not just rounded it needs to be "rounded-lg" class ONLY (no border, no shadow)
- If special is "rounded-full" → add "rounded-full" class ONLY (no border, no shadow)
- If special is "shadow" → add "shadow" class ONLY (no rounded, no border)
- If special is "border" → add "border" class ONLY (no rounded, no shadow)
- If special is "none" → add NO special styling classes
- Use label text exactly as specified
- Output format: <button className="bg-color special-class">Label</button>
- NEVER combine special classes - only ONE special class allowed
- NO extra classes, NO creativity, NO additional styling
- NO imports, wrappers, comments, or markdown
- NO text before or after the button element
""",
        "stream" : False
        }
        )
    try:
        CodeData = CodeResponse.json()
        Code = CodeData["response"]
        Code = Code.strip().removeprefix("jsx").removeprefix("html").removeprefix("```json").removeprefix("```").removeprefix("```jsx").removesuffix("```").strip()
        if("jsx" in Code):
            Code = Code[3:].strip()
            Code.replace("`","")
         
        if("html" in Code):
            Code = Code[4:].strip()
         
        codes.append(Code)
     
    except:
        print("failed 2")
     
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