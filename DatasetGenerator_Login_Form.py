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

titles = [
    "Login to your account", "Sign in to your account", "Welcome back", "Access your account",
    "Login", "Sign In", "Member Login", "User Login", "Account Access", "Sign in",
    "Welcome Back!", "Please Sign In", "Account Login", "User Sign In", "Member Access",
    "Login Here", "Sign In Here", "Enter Your Account", "Access Dashboard", "Continue to Account"
]

descriptions = [
    "Enter your email below to login to your account",
    "Enter your credentials to access your account", 
    "Please enter your email and password to continue",
    "Sign in with your email and password",
    "Welcome back! Please enter your details",
    "Enter your login credentials below",
    "Please provide your account information",
    "Fill in your details to access your account",
    "Enter your information to sign in",
    "Please sign in to continue",
    "Use your account credentials to sign in",
    "Enter your email and password to proceed",
    "Login with your registered email address",
    "Provide your credentials to access the system",
    "Enter your account details below",
    "Sign in using your email and password",
    "Please enter your login information",
    "Access your account with your credentials"
]

email_labels = [
    "Email", "Email Address", "Your Email", "Email*", "E-mail", 
    "Username", "Username/Email", "Login ID", "Account Email", "Your Email Address"
]

email_placeholders = [
    "m@example.com", "your@email.com", "email@domain.com", "user@example.com",
    "john@example.com", "example@mail.com", "name@company.com", "you@domain.com",
    "Enter your email", "Your email here", "Email address", "Type your email"
]

password_labels = [
    "Password", "Password*", "Your Password", "Enter Password", 
    "Login Password", "Account Password", "Password (required)", "Pass"
]

forgot_password_texts = [
    "Forgot your password?", "Forgot password?", "Reset password", 
    "Can't remember password?", "Lost password?", "Password help",
    "Trouble signing in?", "Need help?", "Forgot?", "Reset"
]

login_button_texts = [
    "Login", "Sign In", "Log In", "Continue", "Access Account", "Enter",
    "Sign in", "Log in", "Submit", "Proceed", "Go", "Next"
]

extraLoginButtons = [
  "Login with Google",
  "Login with Apple",
  "Login with GitHub",
  "Login with Facebook",
  "Login with Twitter / X",
  "Login with LinkedIn",
  "Login with Microsoft",
  "Login with Discord",
  "Login with Slack",
  "Login with Notion",
  "Login with Spotify",
  "Login with Reddit"
]


prompt_set = set()
code_set = set()
prompts = []
codes = []

target_samples = 2_500_000
attempts = 0
max_attempts = target_samples * 3  


while len(prompts) < target_samples and attempts < max_attempts:
    attempts += 1 
    card_type = random.choice([1,2])
    login_card_type = random.choice([1,2,3])
    if card_type == 1:
      print("Register")
    else:
      print("login")
   

    if login_card_type == 1:
        print("1")
    elif login_card_type == 2:
        print("2")
    else:
        print("3")

    