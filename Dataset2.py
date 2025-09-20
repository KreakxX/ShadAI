import os
import random

colors = [
    "red", "blue", "green", "yellow", "purple", "pink", "indigo", "gray", "slate", "stone",
    "zinc", "neutral", "orange", "amber", "lime", "emerald", "teal", "cyan", "sky", "violet",
    "fuchsia", "rose", "black", "white"
]

prompt_templates = [
    "button, bg-{color}-{intensity}, {special}, text-{color}-{intensity}, label: {label}",
    "Make a {special} {color}-{intensity} button with text-{color}-{intensity} and the label '{label}'",
    "Generate a button labeled '{label}' styled with bg-{color}-{intensity} and {special}",
    "Create a {special} button with bg-{color}-{intensity}, text-{color}-{intensity}, and label '{label}'",
    "A button saying '{label}' using {special}, bg-{color}-{intensity}, and text-{color}-{intensity}"
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
    "rounded-sm", "rounded", "rounded-md", "rounded-lg", "rounded-xl", "rounded-2xl", "rounded-full",

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
for color in colors:
    for intensity in intensities:
        for label in labels:
            for special in specials:
                if i >= 200_000:
                    break
                template = random.choice(prompt_templates)
                prompt = template.format(color=color, intensity=intensity, label=label, special=special)
                code = f'<Button classname="bg-{color}-{intensity} text-{color}-{intensity} {special}">{label}</Button>'
                with open("Dataset/code.txt", "a") as f:
                    f.write(prompt + "\n")

                with open("Dataset/prompts.txt", "a") as f:
                    f.write(code + "\n")

                i += 1


 

