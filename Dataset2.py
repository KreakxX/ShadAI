import os

colors = [
    "red", "blue", "green", "yellow", "purple", "pink", "indigo", "gray", "slate", "stone",
    "zinc", "neutral", "orange", "amber", "lime", "emerald", "teal", "cyan", "sky", "violet",
    "fuchsia", "rose", "black", "white"
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

special = [
    "rounded-sm", "rounded", "rounded-md", "rounded-lg", "rounded-xl", "rounded-2xl", "rounded-full",

    "border", "border-2", "border-4", "border-0", "border-dashed", "border-dotted", "border-double",

    "px-2 py-1", "px-3 py-2", "px-4 py-2", "px-6 py-3", "px-8 py-4",

    "hover:bg-opacity-80", "hover:opacity-75", "hover:underline", "active:scale-95",
    "focus:outline-none", "focus:ring-2", "focus:ring-4", "focus:ring-offset-2",

    "disabled:opacity-50", "disabled:cursor-not-allowed",

    "shadow-sm", "shadow", "shadow-md", "shadow-lg", "shadow-xl",

    "uppercase", "lowercase", "capitalize", "tracking-wide", "font-bold", "font-semibold", "font-medium"
]

prompts = []
codes = []


for color in colors:
    for intensity in intensities:
        for label in labels:
            for special in special:
                prompt = f"button, bg-{color}-{intensity}, {special}, label: {label} "
                code = f'<Button classname="bg-{color}-{intensity} {special}">{label}</Button>'
                prompts.append(prompt)
                codes.append(code)


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