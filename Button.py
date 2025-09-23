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
    "{color_name} button {label}",
    "{color_name} btn {label}",
    "{label} button {color_name}",
    "{color_name} {label} btn",
    "btn {label}",
    "button {label}",
    "{label} btn",
    "{label} button",
    "{color_name} button '{label}'",
    "{color_name} '{label}' button",
    "{color_name} {label}",
    "{label} {color_name}",
    "{color_name} element {label}",
    "{label} in {color_name}",
    "{color_name} styled {label}",
    "{color_name} {label} element",
    "{label} {color_name} btn",
    "{color_name} UI {label}",
    "{label} {color_name} component",
    "{color_name} clickable {label}",
    "{label} styled {color_name}",
    "{color_name} interactive {label}",
    "{label} control {color_name}",
    "{color_name} action {label}",
    "{label} trigger {color_name}",
]

medium_templates = [
    "Make a {color_name} button with '{label}'",
    "Create a {color_name} button that says '{label}'",
    "Generate a {color_name} button labeled '{label}'",
    "Build a {color_name} '{label}' button",
    "Design a {color_name} button showing '{label}'",
    "I need a {color_name} button with '{label}' text",
    "Can you create a {color_name} button that displays '{label}'?",
    "Please make a {color_name} button saying '{label}'",
    "A {color_name} button labeled '{label}'",
    "A {color_name} '{label}' button",
    "Button in {color_name} with '{label}' text",
    "Add a {color_name} '{label}' button",
    "Insert {color_name} button '{label}'",
    "Show me a {color_name} button for '{label}'",
    "Give me a {color_name} '{label}' element",
    "Render {color_name} button with '{label}'",
    "Display {color_name} '{label}' button",
    "Create {color_name} element for '{label}'",
    "Make {color_name} component saying '{label}'",
    "Generate {color_name} UI element '{label}'",
    "Develop a {color_name} button containing '{label}'",
    "Construct {color_name} '{label}' control",
    "Produce a {color_name} clickable '{label}' item",
    "Craft {color_name} interactive button '{label}'",
    "Build {color_name} UI control for '{label}'",
    "Generate {color_name} action button '{label}'",
    "Create clickable {color_name} '{label}' element",
    "Design interactive {color_name} button '{label}'",
    "Make {color_name} trigger element '{label}'",
    "Develop {color_name} interface button '{label}'",
    "Construct a {color_name} '{label}' interface",
    "Generate {color_name} user control '{label}'",
    "Build functional {color_name} button '{label}'",
    "Create responsive {color_name} '{label}' button",
    "Design modern {color_name} button '{label}'",
    "Generate styled {color_name} '{label}' control",
    "Make interactive {color_name} '{label}' component",
    "Create dynamic {color_name} button '{label}'",
    "Build elegant {color_name} '{label}' button",
    "Design sleek {color_name} button '{label}'",
]

complex_templates = [
    "Make a {color_name} button with '{label}' and {special} styling",
    "Create a {color_name} button that says '{label}' with {special}",
    "Generate a {color_name} button labeled '{label}' using {special}",
    "I need a {color_name} button with '{label}' and {special} styling",
    "Can you create a {color_name} button that displays '{label}' and has {special}?",
    "Please make a {color_name} button saying '{label}' with {special} effects",
    "A {special} {color_name} button labeled '{label}'",
    "Button component with {color_name} color, '{label}' text, and {special}",
    "Add a {color_name} '{label}' button with {special}",
    "How about a {color_name} '{label}' button with {special}?",
    "Erstelle einen {color_name} Button mit '{label}' und {special}",
    "Design a {special} {color_name} element for '{label}'",
    "Build {color_name} button '{label}' featuring {special}",
    "Create styled {color_name} button with '{label}' using {special}",
    "Generate {special} styled {color_name} '{label}' button",
    "Make {color_name} component '{label}' with {special} design",
    "Show {special} {color_name} button displaying '{label}'",
    "Render {color_name} '{label}' element with {special}",
    "Develop a {special} {color_name} button containing '{label}'",
    "Construct {special} {color_name} '{label}' control with styling",
    "Produce a {color_name} button '{label}' featuring {special} design",
    "Craft {special} interactive {color_name} button '{label}'",
    "Build {color_name} UI control '{label}' with {special} appearance",
    "Generate {special} {color_name} action button '{label}'",
    "Create {color_name} clickable '{label}' element with {special}",
    "Design {special} interactive {color_name} button '{label}'",
    "Make {color_name} trigger element '{label}' using {special}",
    "Develop {special} {color_name} interface button '{label}'",
    "Construct a {color_name} '{label}' interface with {special}",
    "Generate {special} {color_name} user control '{label}'",
    "Build functional {color_name} button '{label}' featuring {special}",
    "Create responsive {color_name} '{label}' button with {special}",
    "Design modern {special} {color_name} button '{label}'",
    "Generate styled {color_name} '{label}' control using {special}",
    "Make interactive {special} {color_name} '{label}' component",
    "Create dynamic {color_name} button '{label}' with {special}",
    "Build elegant {special} {color_name} '{label}' button",
    "Design sleek {color_name} button '{label}' featuring {special}",
    "Mach einen {special} {color_name} Button für '{label}'",
    "Generiere {color_name} Button '{label}' mit {special} Stil",
    "Baue einen {special} {color_name} '{label}' Button",
    "Erstelle {color_name} Element '{label}' mit {special}",
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
    "Buy Now", "Get Quote", "Call Now", "Email Us", "Schedule", "Book Appointment", "Try Free", "Demo", "Tour",
    "Get Started", "Learn More", "Try Now", "Book Demo", "Free Quote", "Contact", "Support", "Feedback",
    "Purchase", "Upgrade Now", "Go Premium", "Subscribe", "Join Now", "Register", "Sign In", "Dashboard",
    "Activate", "Deactivate", "Approve", "Reject", "Publish", "Draft", "Archive", "Restore", "Backup", "Sync",
    "Export", "Import", "Copy", "Paste", "Cut", "Undo", "Redo", "Find", "Replace", "Sort",
    "Merge", "Split", "Combine", "Separate", "Group", "Ungroup", "Lock", "Unlock", "Pin", "Unpin",
    "Mark as Read", "Mark as Unread", "Star", "Unstar", "Flag", "Unflag", "Hide", "Show", "Collapse", "Expand",
    "Maximize", "Minimize", "Fullscreen", "Exit", "Zoom In", "Zoom Out", "Reset Zoom", "Fit to Screen", "Center", "Align",
    "Bold", "Italic", "Underline", "Strike", "Highlight", "Clear Format", "Font Size", "Font Color", "Background", "Border",
    "Insert", "Remove", "Move Up", "Move Down", "First", "Last", "Previous", "Random", "Shuffle", "Repeat",
    "Connect", "Disconnect", "Link", "Unlink", "Attach", "Detach", "Mount", "Unmount", "Load", "Unload",
    "Begin", "End", "Launch", "Terminate", "Execute", "Run", "Compile", "Build", "Deploy", "Test",
    "Debug", "Profile", "Monitor", "Track", "Analyze", "Report", "Log", "Audit", "Verify", "Validate",
    "Configure", "Setup", "Initialize", "Reset", "Restore", "Factory Reset", "Calibrate", "Optimize", "Enhance", "Improve"
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

advanced_specials = [
    "rounded-2xl", "rounded-full", "shadow-lg", "shadow-xl", "px-8 py-4",
    "font-bold", "text-lg", "hover:bg-opacity-80", "active:scale-95",
    "focus:ring-2", "transition-all", "duration-300", "ease-in-out",
    "border-dashed", "uppercase", "w-full", "text-xl", "font-black",
    "border-4", "hover:shadow-xl", "transform", "cursor-pointer",
    "text-2xl", "font-extrabold", "border-dotted", "border-double",
    "hover:scale-105", "active:translate-y-1", "focus:ring-4", "focus:ring-offset-2",
    "disabled:opacity-50", "disabled:cursor-not-allowed", "hover:rotate-1",
    "bg-gradient-to-r", "from-current", "to-transparent", "backdrop-blur",
    "ring-2", "ring-offset-2", "ring-opacity-50", "shadow-2xl",
    "text-3xl", "tracking-wider", "leading-tight", "whitespace-nowrap",
    "overflow-hidden", "text-ellipsis", "min-w-0", "max-w-xs"
]

def get_styling_for_template_complexity(template_type, variation_seed):
    """Enhanced styling generation with more variety"""
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
    
    return " ".join(random.sample(options, k=min(count, len(options))))

prompts_set = set()
codes_set = set()
prompts_list = []
codes_list = []

os.makedirs("Buttons", exist_ok=True)

target_samples = 1_000_000
attempts = 0
max_attempts = target_samples * 3  


while len(prompts_list) < target_samples and attempts < max_attempts:
    attempts += 1
    
    template_type = random.choices(
        ["simple", "medium", "complex"], 
        weights=[30, 40, 30]  
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
        if intensity in ["50", "100", "200", "300"]:
            color_name = f"Light {color.capitalize()}"
        elif intensity in ["700", "800", "900"]:
            color_name = f"Dark {color.capitalize()}"
        else:
            color_name = color.capitalize()
    
    label = random.choice(labels)
    
    chosen_specials = get_styling_for_template_complexity(template_type, attempts)
    
    try:
        prompt = template.format(
            color=color,
            intensity=intensity,
            label=label,
            special=chosen_specials,
            color_name=color_name
        )
    except KeyError:
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
    
    if prompt not in prompts_set and code not in codes_set:
        prompts_set.add(prompt)
        codes_set.add(code)
        prompts_list.append(prompt)
        codes_list.append(code)
        
    
with open("Buttons/code.txt", "w", encoding="utf-8") as f:
    for code in codes_list:
        f.write(code + "\n")

with open("Buttons/prompts.txt", "w", encoding="utf-8") as f:
    for prompt in prompts_list:
        f.write(prompt + "\n")
