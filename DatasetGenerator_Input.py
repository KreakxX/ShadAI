import os
import random

colors = [
    "red", "blue", "green", "yellow", "purple", "pink", "indigo", "gray", "slate", "stone",
    "zinc", "neutral", "orange", "amber", "lime", "emerald", "teal", "cyan", "sky", "violet",
    "fuchsia", "rose"
]


colorMap = {
    "Red": "red-500",
    "Light Red": "red-300",
    "Dark Red": "red-700",
    "Blue": "blue-500",
    "Light Blue": "blue-300", 
    "Dark Blue": "blue-700",
    "Green": "green-500",
    "Light Green": "green-300",
    "Dark Green": "green-700",
    "Yellow": "yellow-500",
    "Light Yellow": "yellow-300",
    "Dark Yellow": "yellow-700",
    "Purple": "purple-500",
    "Light Purple": "purple-300",
    "Dark Purple": "purple-700",
    "Pink": "pink-500",
    "Light Pink": "pink-300",
    "Dark Pink": "pink-700",
    "Indigo": "indigo-500",
    "Light Indigo": "indigo-300",
    "Dark Indigo": "indigo-700",
    "Gray": "gray-500",
    "Light Gray": "gray-300",
    "Dark Gray": "gray-700",
    "Orange": "orange-500",
    "Light Orange": "orange-300",
    "Dark Orange": "orange-700",
    "Amber": "amber-500",
    "Light Amber": "amber-300",
    "Dark Amber": "amber-700",
    "Lime": "lime-500",
    "Light Lime": "lime-300",
    "Dark Lime": "lime-700",
    "Emerald": "emerald-500",
    "Light Emerald": "emerald-300",
    "Dark Emerald": "emerald-700",
    "Teal": "teal-500",
    "Light Teal": "teal-300",
    "Dark Teal": "teal-700",
    "Cyan": "cyan-500",
    "Light Cyan": "cyan-300",
    "Dark Cyan": "cyan-700",
    "Sky": "sky-500",
    "Light Sky": "sky-300",
    "Dark Sky": "sky-700",
    "Violet": "violet-500",
    "Light Violet": "violet-300",
    "Dark Violet": "violet-700",
    "Fuchsia": "fuchsia-500",
    "Light Fuchsia": "fuchsia-300",
    "Dark Fuchsia": "fuchsia-700",
    "Rose": "rose-500",
    "Light Rose": "rose-300",
    "Dark Rose": "rose-700",
}

simple_templates = [
    "{color_name} {type} Input {label}",
    "{label} {type} Input {color_name}",
    "{type} {color_name} Input {label}",
    "{type} {label} Input {color_name}",
    "{color_name} Input {type} {label}",
    "Input {type} {color_name} '{label}'",
    "{color_name} {label} Input {type}",
    "{type} Input for {label} in {color_name}",
    "{color_name} {label} {type} field",
    "field {type} {color_name} {label}",
]

medium_templates = [
    "Make a {type} {color_name} Input with '{label}'",
    "Create a {color_name} Input of type {type} that says '{label}'",
    "Generate a {color_name} {type} Input labeled '{label}'",
    "Build a {color_name} Input '{label}' of type {type}",
    "Design a {type} {color_name} Input showing '{label}'",
    "I need a {color_name} Input with '{label}' text, type {type}",
    "Can you create a {color_name} Input that displays '{label}' and is {type}?",
    "Please make a {type} {color_name} Input saying '{label}'",
    "A {color_name} {type} Input labeled '{label}'",
    "A {color_name} Input '{label}' of type {type}",
    "Input in {color_name} of type {type} with '{label}' text",
    "Add a {color_name} Input '{label}' with {type}",
    "Insert {color_name} {type} Input '{label}'",
    "Show me a {color_name} Input for '{label}', type {type}",
    "Render {color_name} {type} Input with '{label}'",
    "Display {color_name} Input '{label}' of type {type}",
    "Make {color_name} Input field {type} saying '{label}'",
    "Generate {color_name} text field {type} element '{label}'",
    "Develop a {color_name} {type} Input containing '{label}'",
    "Craft {color_name} {type} Input '{label}' interactively",
    "Build {color_name} UI Input '{label}' of type {type}",
    "Generate {color_name} Input '{label}' with {type}",
    "Design {color_name} Input '{label}' that is {type}",
    "Develop {color_name} {type} Input '{label}'",
    "Build functional {color_name} Input '{label}' ({type})",
    "Create responsive {color_name} '{label}' Input of type {type}",
    "Design modern {color_name} {type} Input '{label}'",
    "Create dynamic {color_name} Input '{label}' of type {type}",
    "Build elegant {color_name} '{label}' Input, type {type}",
    "Design sleek {color_name} Input '{label}' ({type})",
    "Set up a {color_name} Input '{label}' reading as {type}",
    "Create Input: {color_name} '{label}', type {type}",
    "New {color_name} Input: '{label}' ({type})",
    "Quick {color_name} {type} Input with '{label}'",
    "{color_name} Input implementation '{label}' of type {type}",
    "Simple {color_name} Input '{label}' ({type})",
    "Basic {color_name} {type} Input with text '{label}'",
    "{color_name} Input - '{label}' text, type {type}",
    "Add {color_name} Input, text: '{label}', type {type}",
    "Include {color_name} Input saying '{label}', type {type}"
]

complex_templates = [
    "Make a {type} {color_name} Input with '{label}' and {special} styling",
    "Create a {color_name} Input of type {type} that says '{label}' with {special}",
    "Generate a {color_name} Input labeled '{label}', type {type}, using {special}",
    "I need a {color_name} Input '{label}' of type {type} with {special} styling",
    "Can you create a {color_name} {type} Input displaying '{label}' and {special} effects?",
    "Please make a {color_name} Input saying '{label}' ({type}) with {special}",
    "A {special} {color_name} {type} Input labeled '{label}'",
    "{type} Input component with {color_name} color, '{label}' text, and {special}",
    "Add a {color_name} Input '{label}' of type {type} with {special}",
    "How about a {color_name} Input '{label}' ({type}) with {special}?",
    "Erstelle einen {color_name} Input '{label}' von Typ {type} und {special}",
    "Build {color_name} Input '{label}' featuring {special}, type {type}",
    "Create styled {color_name} Input with '{label}' ({type}) using {special}",
    "Generate {special} styled {color_name} '{label}' Input of type {type}",
    "Show {special} {color_name} Input displaying '{label}' ({type})",
    "Develop a {special} {color_name} Input '{label}' of type {type}",
    "Produce a {color_name} Input '{label}' featuring {special} design, type {type}",
    "Craft {special} interactive {color_name} Input '{label}' ({type})",
    "Generate {special} {color_name} action Input '{label}' of type {type}",
    "Design {special} interactive {color_name} Input '{label}' ({type})",
    "Develop {special} {color_name} interface Input '{label}' of type {type}",
    "Build functional {color_name} Input '{label}' featuring {special}, type {type}",
    "Create responsive {color_name} Input '{label}' ({type}) with {special}",
    "Design modern {special} {color_name} Input '{label}' ({type})",
    "Create dynamic {color_name} Input '{label}' with {special}, type {type}",
    "Build elegant {special} {color_name} '{label}' Input ({type})",
    "Design sleek {color_name} Input '{label}' ({type}) featuring {special}",
    "Mach einen {special} {color_name} Input '{label}' von Typ {type}",
    "Generiere {color_name} Input '{label}' ({type}) mit {special} Stil",
    "Baue einen {special} {color_name} '{label}' Input ({type})",
    "Design {color_name} Input '{label}' ({type}) with {special} and rounded corners",
    "{color_name} Input '{label}' ({type}) using {special} plus shadow",
    "Custom {color_name} Input '{label}' ({type}) with {special} styling",
    "Advanced {color_name} Input '{label}' ({type}) featuring {special}",
    "{color_name} Input '{label}' ({type}) styled with {special} effects",
    "Professional {color_name} Input '{label}' ({type}) with {special}",
    "Modern {color_name} Input '{label}' ({type}) using {special} design",
    "{color_name} '{label}' Input ({type}) with {special} animation",
    "Enhanced {color_name} Input '{label}' ({type}) with {special}",
]


labels = [
"Enter username", "Enter email", "Enter password", "Confirm password",
"Enter phone number", "Enter OTP", "Enter security code", 
"Enter PIN", "Confirm email", "Enter full name",
"First name", "Last name", "Full name", "Middle name", "Date of birth",
"Street address", "City", "State", "ZIP code", "Country", 
"Company name", "Job title", "Organization", "Website URL",
"Enter email address", "Enter phone number", "Enter contact name",
"Your message", "Type a message", "Type your reply", 
"Search contacts", "Enter subject", "Enter feedback",
"Card number", "Cardholder name", "Expiry date", "CVV",
"Billing address", "Shipping address", "Enter coupon code",
"Enter promo code", "Enter IBAN", "Enter account number",
"Search...", "Search products", "Search users", "Search posts",
"Type to search", "Filter results", "Enter query", "Find location",
"Search articles", "Enter keyword",
"Enter title", "Enter description", "Add comment", 
"Write a note", "Enter task", "Enter reminder", 
"Write review", "Enter bio", "Add caption", "Enter hashtag",
"Enter task", "Add reminder", "Enter note", "Enter title", "Enter description",
"Add tags", "Enter category", "Write comment", "Add label", "Enter project name",
"Enter event name", "Enter appointment details", "Enter meeting link",
"Write instructions", "Enter goal", "Enter milestone", "Enter checklist item",
"Enter URL", "Enter filename", "Enter code snippet", "Enter hashtag",
"Enter phrase", "Type password hint", "Enter question", "Enter answer"

]

intensities = [
    "50", "100", "200", "300", "400", "500", "600", "700", "800", "900"
]

basic_specials = [
    "px-4 py-2", "px-3 py-2", "rounded", "rounded-md", "shadow", "border",
    "px-2 py-1", "px-6 py-2", "rounded-sm", "shadow-sm"
]

intermediate_specials = [
    "rounded-lg", "rounded-xl", "shadow-md", "px-6 py-3", "font-semibold", 
    "border-2", "hover:opacity-75", "transition-colors", "font-medium",
    "text-sm", "shadow-lg", "px-8 py-2"
]

types = [
    "file", "text", "number", "password", "url", "date", "time", "email"
]

advanced_specials = [
    "rounded-2xl", "rounded-full", "shadow-lg", "shadow-xl", "px-8 py-4",
    "font-bold", "text-lg", "hover:bg-opacity-80", "active:scale-95",
    "focus:ring-2", "transition-all", "duration-300", "ease-in-out",
    "border-dashed", "uppercase", "w-full", "text-xl", "font-black",
    "border-4", "hover:shadow-xl", "transform",
    "text-2xl", "font-extrabold", "border-dotted", "border-double",
    "hover:scale-105", "active:translate-y-1", "focus:ring-4", "focus:ring-offset-2",
    "disabled:opacity-50", "disabled:cursor-not-allowed", "hover:rotate-1",
     "backdrop-blur",
    "ring-2", "ring-offset-2", "ring-opacity-50", "shadow-2xl",
    "text-3xl", "tracking-wider", "leading-tight", "whitespace-nowrap",
    "overflow-hidden", "text-ellipsis", "min-w-0", "max-w-xs",
     "hover:bg-opacity-90 active:bg-opacity-100",
    "transform hover:-translate-y-0.5",
    "transition-shadow hover:shadow-lg",
    "focus:outline-none focus:ring",
    "hover:brightness-110 active:brightness-90",
    "group-hover:scale-105",
    "motion-safe:hover:scale-110",
    "active:shadow-inner",
    "hover:contrast-125"
]
def consolidate_styles(styles_list):
    """Prevent duplicate or conflicting styles."""
    styles = styles_list.split()
    
    exclusive_groups = {
        'padding': [s for s in styles if s.startswith(('px-', 'py-'))],
        'rounded': [s for s in styles if s.startswith('rounded')],
        'shadow': [s for s in styles if s.startswith('shadow')],
        'border': [s for s in styles if s.startswith('border')],
        'font': [s for s in styles if s.startswith('font')],
        'text': [s for s in styles if s.startswith('text-')]
    }
    
    final_styles = set()
    for group in exclusive_groups.values():
        if group:
            final_styles.add(group[-1])
    
    other_styles = [s for s in styles if not any(
        s in group for group in exclusive_groups.values()
    )]
    final_styles.update(other_styles)
    
    return ' '.join(sorted(final_styles))

def get_styling_for_template_complexity(template_type, variation_seed):
    random.seed(variation_seed)  
    
    if template_type == "simple":
        options = basic_specials
        count = 1
    elif template_type == "medium":
        options = basic_specials + intermediate_specials
        count = random.randint(1, 2)
    else:  
        options = basic_specials + intermediate_specials + advanced_specials
        count = random.randint(2, 4)
    raw_styles = ' '.join(random.sample(options, k=min(count, len(options))))
    return consolidate_styles(raw_styles)

prompts_set = set()
codes_set = set()
prompts_list = []
codes_list = []


target_samples = 2_500_000
attempts = 0
max_attempts = target_samples * 3  


while len(prompts_list) < target_samples and attempts < max_attempts:
    attempts += 1
    
    template_type = random.choices(
        ["simple", "medium", "complex"], 
        weights=[20, 45, 35]  
    )[0]
    
    if template_type == "simple":
        template = random.choice(simple_templates)
    elif template_type == "medium":
        template = random.choice(medium_templates)
    else:
        template = random.choice(complex_templates)
    
    use_map = random.choice([True, False])
    if use_map:
        color_key = random.choice(list(colorMap.keys()))
        color_class = colorMap[color_key]
        color, intensity = color_class.split("-")
        color_name = color_key
    else:
        color = random.choice(colors)
        intensity = random.choice(intensities)
        if intensity in ["200", "300", "400", "500"]:
            color_name = f"Light {color.capitalize()}"
        elif intensity in ["800", "900","950"]:
            color_name = f"Dark {color.capitalize()}"
        else:
            color_name = color.capitalize()
    
    label = random.choice(labels)
    type = random.choice(types)
    chosen_specials = get_styling_for_template_complexity(template_type, attempts)
    
    try:
        prompt = template.format(
            color=color,
            intensity=intensity,
            label=label,
            special=chosen_specials,
            color_name=color_name,
            type=type
        )
    except KeyError:
        available_vars = {
            'color': color,
            'intensity': intensity,
            'label': label,
            'special': chosen_specials,
            'color_name': color_name,
            'type': type
        }
        import re
        template_vars = re.findall(r'\{(\w+)\}', template)
        format_dict = {var: available_vars[var] for var in template_vars if var in available_vars}
        prompt = template.format(**format_dict)
    
    code = f'<Input type="{type}" placeholder="{label}" className="bg-{color}-{intensity} {consolidate_styles(chosen_specials)}"></Input>'
    
    if prompt not in prompts_set and code not in codes_set:
        prompts_set.add(prompt)
        codes_set.add(code)
        prompts_list.append(prompt)
        codes_list.append(code)
        
    
with open("Input_Dataset_2_5m/code.txt", "w", encoding="utf-8") as f:
    for code in codes_list:
        f.write(code + "\n")

with open("Input_Dataset_2_5m/prompts.txt", "w", encoding="utf-8") as f:
    for prompt in prompts_list:
        f.write(prompt + "\n")
