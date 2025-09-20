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
    "Blue": "blue-500",
    "Light Blue": "blue-300",
    "Green": "green-500",
    "Light Green": "green-300",
    "Yellow": "yellow-500",
    "Light Yellow": "yellow-300",
    "Purple": "purple-500",
    "Light Purple": "purple-300",
    "Pink": "pink-500",
    "Light Pink": "pink-300",
    "Indigo": "indigo-500",
    "Light Indigo": "indigo-300",
    "Gray": "gray-500",
    "Light Gray": "gray-300",
    "Slate": "slate-500",
    "Light Slate": "slate-300",
    "Stone": "stone-500",
    "Light Stone": "stone-300",
    "Zinc": "zinc-500",
    "Light Zinc": "zinc-300",
    "Neutral": "neutral-500",
    "Light Neutral": "neutral-300",
    "Orange": "orange-500",
    "Light Orange": "orange-300",
    "Amber": "amber-500",
    "Light Amber": "amber-300",
    "Lime": "lime-500",
    "Light Lime": "lime-300",
    "Emerald": "emerald-500",
    "Light Emerald": "emerald-300",
    "Teal": "teal-500",
    "Light Teal": "teal-300",
    "Cyan": "cyan-500",
    "Light Cyan": "cyan-300",
    "Sky": "sky-500",
    "Light Sky": "sky-300",
    "Violet": "violet-500",
    "Light Violet": "violet-300",
    "Fuchsia": "fuchsia-500",
    "Light Fuchsia": "fuchsia-300",
    "Rose": "rose-500",
    "Light Rose": "rose-300",
}


prompt_templates = [
    "button, bg-{color}-{intensity}, {special}, text-{color}-{intensity}, label: {label}",
    "Make a {special} {color}-{intensity} button with text-{color}-{intensity} and the label '{label}'",
    "Generate a button labeled '{label}' styled with bg-{color}-{intensity} and {special}",
    "Create a {special} button with bg-{color}-{intensity}, text-{color}-{intensity}, and label '{label}'",
    "A button saying '{label}' using {special}, bg-{color}-{intensity}, and text-{color}-{intensity}",
    "A {special} Button with bg-{color}-{intensity}, and text-{color}-{intensity} saying '{label}'",
    "Create a button labeled '{label}' using {special} style, background {color}-{intensity} and text {color}-{intensity}",
    "Design a {special} button with background {color}-{intensity}, text color {color}-{intensity} and label '{label}'",
    "Button with '{label}' text, bg-{color}-{intensity} and {special}, text in {color}-{intensity}",
    "Generate a {special} button that says '{label}' with bg-{color}-{intensity} and text-{color}-{intensity}",
    "Make a '{label}' button styled as {special}, background {color}-{intensity} and foreground {color}-{intensity}",
    "Build a {special} button showing '{label}' with bg-{color}-{intensity} and text-{color}-{intensity}",
    "Produce a button labeled '{label}' using bg-{color}-{intensity}, text-{color}-{intensity}, and style {special}",
    "A '{label}' button featuring {special} with background color {color}-{intensity} and text color {color}-{intensity}"
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
    "Like Post", "Follow", "Unfollow", "Add Friend", "Remove Friend", "Message", "Reply", "Forward", "Quote", "Copy Link"
]
intensities = [
    "50", "100", "200", "300", "400", "500", "600", "700", "800", "900"
]

specials = [
    "rounded-sm", "rounded-md", "rounded-lg", "rounded-xl", "rounded-2xl", "rounded-full",

    "border", "border-2", "border-4", "border-0", "border-dashed", "border-dotted", "border-double",

    "px-2 py-1", "px-3 py-2", "px-4 py-2", "px-6 py-3", "px-8 py-4",

    "hover:bg-opacity-80", "hover:opacity-75", "hover:underline", "active:scale-95",
    "focus:outline-none", "focus:ring-2", "focus:ring-4", "focus:ring-offset-2",

    "disabled:opacity-50", "disabled:cursor-not-allowed",

    "shadow-sm", "shadow", "shadow-md", "shadow-lg", "shadow-xl",

    "font-bold", "font-semibold", "text-lg", "text-xl", "text-2xl", "text-3xl", "text-sm"
]


prompts = []
codes = []

i = 0
for i in range(350_000):
    use_map = random.choice([True, False])
    color = ""
    intensity = ""
    if use_map:
        color = random.choice(colors)
        intensity = random.choice(intensities)

    else:
        color_class = colorMap[random.choice(list(colorMap.keys()))]  
        color, intensity = color_class.split("-")

    label = random.choice(labels)
    chosen_specials = " ".join(random.sample(specials, k=random.randint(1,3)))
    template = random.choice(prompt_templates)
    prompt = template.format(color=color, intensity=intensity, label=label, special=chosen_specials)
    code = f'<Button classname="bg-{color}-{intensity} text-{color}-{intensity} {chosen_specials}">{label}</Button>'
    with open("Dataset/code.txt", "a") as f:
        f.write(code + "\n")

    with open("Dataset/prompts.txt", "a") as f:
        f.write(prompt + "\n")

    i+=1



# for color in colors:
#     for intensity in intensities:
#         for label in labels:
#             for special in specials:
#                 if i >= 200_000:
#                     break
#                 template = random.choice(prompt_templates)
#                 prompt = template.format(color=color, intensity=intensity, label=label, special=special)
#                 code = f'<Button classname="bg-{color}-{intensity} text-{color}-{intensity} {special}">{label}</Button>'
               
#                 i += 1


 



