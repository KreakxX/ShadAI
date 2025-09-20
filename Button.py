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

prompt_templates = [
    "{color_name} button {label}",
    "{color_name} btn {label}",
    "{label} button {color_name}",
    "{color_name} {label} btn",
    "{color_name} button '{label}'",
    "{color_name} '{label}' button",
    
    "Make a {color_name} button with '{label}'",
    "Create a {color_name} button that says '{label}'",
    "Generate a {color_name} button labeled '{label}'",
    "Build a {color_name} '{label}' button",
    "Design a {color_name} button showing '{label}'",
    "Make a {color_name} '{label}' button",
    "Create {color_name} button '{label}'",
    "Generate {color_name} '{label}' button",
    
    "Make a {color_name} button with '{label}' and {special} styling",
    "Create a {color_name} button that says '{label}' with {special}",
    "Generate a {color_name} button labeled '{label}' using {special}",
    "Build a {color_name} '{label}' button with {special} style",
    "Design a {color_name} button showing '{label}' and {special}",
    "{color_name} button {label} with {special}",
    "{color_name} btn {label} {special}",
    "{special} {color_name} button {label}",
    
    "I need a {color_name} button with '{label}' text",
    "Can you create a {color_name} button that displays '{label}'?",
    "Please make a {color_name} button saying '{label}'",
    "Show me a {color_name} button with '{label}' label",
    "Give me a {color_name} '{label}' button",
    "I want a {color_name} button that says '{label}'",
    "Let me have a {color_name} button for '{label}'",
    
    "I need a {color_name} button with '{label}' and {special} styling",
    "Can you create a {color_name} button that displays '{label}' and has {special}?",
    "Please make a {color_name} button saying '{label}' with {special} effects",
    "Show me a {color_name} button with '{label}' label and {special} style",
    "Give me a {color_name} '{label}' button with {special}",
    "I want a {color_name} button that says '{label}' and looks {special}",
    "Let me have a {color_name} button for '{label}' with {special}",
    
    "A {color_name} button labeled '{label}'",
    "A {color_name} '{label}' button",
    "Button in {color_name} with '{label}' text",
    "Button '{label}' in {color_name}",
    "Button saying '{label}' in {color_name}",
    "{color_name} colored button with '{label}'",
    "{color_name} colored '{label}' button",
    
    "A {special} {color_name} button labeled '{label}'",
    "A {special} {color_name} '{label}' button",
    "Button in {color_name} with '{label}' text and {special}",
    "Button '{label}' in {color_name} with {special} styling",
    "Button saying '{label}' in {color_name} using {special}",
    "{special} {color_name} colored button with '{label}'",
    "{special} {color_name} colored '{label}' button",
    
    "btn {label}",
    "button {label}",
    "{label} btn",
    "{label} button",
    "btn {label} {special}",
    "button {label} {special}",
    "{label} btn {special}",
    "{label} button {special}",
    
    "Button component with {color_name} color and '{label}' text",
    "Render {color_name} button with '{label}' label",
    "Button element in {color_name} showing '{label}'",
    "{color_name} button component displaying '{label}'",
    "Button with {color_name} background and '{label}' content",
    
    "Button component with {color_name} color, '{label}' text, and {special}",
    "Render {color_name} button with '{label}' label and {special} styling",
    "Button element in {color_name} showing '{label}' with {special}",
    "{color_name} button component displaying '{label}' using {special}",
    "Button with {color_name} background, '{label}' content, and {special}",
    
    "Add a {color_name} '{label}' button",
    "Insert {color_name} button '{label}'",
    "Place a {color_name} '{label}' button",
    "Put a {color_name} button saying '{label}'",
    "Create {color_name} button for '{label}'",
    
    "Add a {color_name} '{label}' button with {special}",
    "Insert {color_name} button '{label}' styled with {special}",
    "Place a {color_name} '{label}' button using {special}",
    "Put a {color_name} button saying '{label}' with {special} design",
    "Create {color_name} button for '{label}' with {special} styling",
    
    "How about a {color_name} '{label}' button?",
    "What about a {color_name} button for '{label}'?",
    "Could you make a {color_name} '{label}' button?",
    "Can I get a {color_name} button with '{label}'?",
    "Would you create a {color_name} '{label}' button?",
    
    "How about a {color_name} '{label}' button with {special}?",
    "What about a {color_name} button for '{label}' using {special}?",
    "Could you make a {color_name} '{label}' button with {special}?",
    "Can I get a {color_name} button with '{label}' and {special} styling?",
    "Would you create a {color_name} '{label}' button using {special}?",
    
    "Erstelle einen {color_name} Button mit '{label}'",
    "Mach einen {color_name} '{label}' Button",
    "Generiere {color_name} Button '{label}'",
    "{color_name} Button mit '{label}' Text",
    "{color_name} '{label}' Button",
    "Button in {color_name} mit '{label}'",
    
    "Erstelle einen {color_name} Button mit '{label}' und {special}",
    "Mach einen {color_name} '{label}' Button mit {special}",
    "Generiere {color_name} Button '{label}' mit {special} Stil",
    "{color_name} Button mit '{label}' Text und {special}",
    "{color_name} '{label}' Button mit {special}",
    "Button in {color_name} mit '{label}' und {special}",
    
    "'{label}' button in {color_name}",
    "Button '{label}' styled as {color_name}",
    "'{label}' in {color_name} button",
    "Button labeled '{label}' in {color_name}",
    "'{label}' {color_name} button",
    
    "'{label}' button in {color_name} with {special}",
    "Button '{label}' styled as {color_name} {special}",
    "'{label}' in {color_name} button with {special}",
    "Button labeled '{label}' in {color_name} using {special}",
    "'{label}' {color_name} button with {special}",
]

labels = [
    "Sign Up", "Log In", "Submit", "Cancel", "OK", "Next", "Back", "Continue", "Start", "Stop",
    "Download", "Upload", "Save", "Delete", "Edit", "View", "Share", "Like", "Dislike", "Comment",
    "Retry", "Refresh", "Search", "Filter", "Apply", "Reset", "Confirm", "Decline", "Yes", "No",
    "Accept", "Deny", "Allow", "Block", "Send", "Receive", "Buy", "Sell", "Order", "Pay",
    "Subscribe", "Unsubscribe", "Register", "Join", "Leave", "Close", "Open", "Details", "More", "Less",
    "Settings", "Options", "Help", "Info", "Contact", "Support", "Report", "Download PDF", "Print", "Preview",
    "Upload File", "Choose File", "Select", "Deselect", "Enable", "Disable", "Start Free Trial", "Get Started", "Upgrade", "Downgrade",
    "Book Now", "Reserve", "Check In", "Check Out", "Continue as Guest", "Try Again", "Proceed", "Finish", "Install", "Update",
    "Watch", "Listen", "Play", "Pause", "Stop", "Record", "Forward", "Rewind", "Skip", "Shuffle",
    "Like Post", "Follow", "Unfollow", "Add Friend", "Remove Friend", "Message", "Reply", "Forward", "Quote", "Copy Link",
    "Add to Cart", "Checkout", "Login", "Logout", "Home", "About", "Contact Us", "Learn More", "Subscribe Now", "Free Trial",
    "Buy Now", "Get Quote", "Call Now", "Email Us", "Schedule", "Book Appointment", "Try Free", "Demo", "Tour"
]

intensities = [
    "50", "100", "200", "300", "400", "500", "600", "700", "800", "900"
]

specials = [
    "rounded-sm", "rounded-md", "rounded-lg", "rounded-xl", "rounded-2xl", "rounded-full",
    "border", "border-2", "border-4", "border-dashed", "border-dotted", "border-double",
    "px-2 py-1", "px-3 py-2", "px-4 py-2", "px-6 py-3", "px-8 py-4",
    "hover:bg-opacity-80", "hover:opacity-75", "hover:underline", "active:scale-95",
    "focus:outline-none", "focus:ring-2", "focus:ring-4", "focus:ring-offset-2",
    "disabled:opacity-50", "disabled:cursor-not-allowed",
    "shadow-sm", "shadow", "shadow-md", "shadow-lg", "shadow-xl",
    "font-bold", "font-semibold", "text-lg", "text-xl", "text-2xl", "text-3xl", "text-sm",
    "uppercase", "lowercase", "capitalize", "italic", "underline",
    "transition-colors", "transition-all", "duration-200", "duration-300", "ease-in-out",
    "cursor-pointer", "w-full", "w-auto", "min-w-fit", "flex items-center justify-center"
]

# Dataset-Ordner erstellen falls nicht vorhanden
os.makedirs("Buttons", exist_ok=True)

with open("Buttons/code.txt", "w", encoding="utf-8") as f:
    pass
with open("Buttons/prompts.txt", "w", encoding="utf-8") as f:
    pass

for i in range(1_000_000):
    use_map = random.choice([True, False])
    
    if use_map:
        color_key = random.choice(list(colorMap.keys()))
        color_class = colorMap[color_key]
        color, intensity = color_class.split("-")
        color_name = color_key  
    else:
        color = random.choice(colors)
        intensity = random.choice(intensities)
        if intensity in ["50", "100", "200", "300"]:
            color_name = f"Light {color.capitalize()}"
        elif intensity in ["700", "800", "900"]:
            color_name = f"Dark {color.capitalize()}"
        else:
            color_name = color.capitalize()
    
    label = random.choice(labels)
    chosen_specials = " ".join(random.sample(specials, k=random.randint(1, 4)))
    template = random.choice(prompt_templates)
    
    try:
        prompt = template.format(
            color=color, 
            intensity=intensity, 
            label=label, 
            special=chosen_specials,
            color_name=color_name
        )
    except KeyError as e:
        available_vars = {
            'color': color,
            'intensity': intensity, 
            'label': label,
            'special': chosen_specials,
            'color_name': color_name
        }
        import re
        template_vars = re.findall(r'\{(\w+)\}', template)
        format_dict = {var: available_vars[var] for var in template_vars if var in available_vars}
        prompt = template.format(**format_dict)
    
    code = f'<Button className="bg-{color}-{intensity} {chosen_specials}">{label}</Button>'
    
    with open("Buttons/code.txt", "a") as f:
        f.write(code + "\n")
    
    with open("Buttons/prompts.txt", "a") as f:
        f.write(prompt + "\n")
