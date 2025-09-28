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

intensities = ["50", "100", "200", "300", "400", "500", "600", "700", "800", "900"]

login_titles = [
    "Login to your account", "Sign in to your account", "Welcome back", "Access your account",
    "Login", "Sign In", "Member Login", "User Login", "Account Access", "Sign in",
    "Welcome Back!", "Please Sign In", "Account Login", "User Sign In", "Member Access",
    "Login Here", "Sign In Here", "Enter Your Account", "Access Dashboard", "Continue to Account"
]

login_descriptions = [
    "Enter your email below to login to your account",
    "Enter your credentials to access your account", 
    "Please enter your email and password to continue",
    "Sign in with your email and password",
    "Welcome back! Please enter your details",
    "Enter your login credentials below",
    "Please provide your account information",
    "Fill in your details to access your account"
]

login_button_texts = [
    "Login", "Sign In", "Log In", "Continue", "Access Account", "Enter",
    "Sign in", "Log in", "Submit", "Proceed", "Go", "Next"
]

register_titles = [
    "Create your account", "Sign up for free", "Join us today", "Get started",
    "Register", "Sign Up", "Create Account", "Join Now", "New Account",
    "Start your journey", "Welcome!", "Join our community", "Register here"
]

register_descriptions = [
    "Create your account to get started",
    "Enter your details to create a new account",
    "Join us by creating your free account",
    "Sign up to access all features",
    "Please fill in your information to register",
    "Get started by creating your account",
    "Register to unlock all features",
    "Create your account in just a few steps"
]

register_button_texts = [
    "Register", "Sign Up", "Create Account", "Join Now", "Get Started",
    "Create an Account", "Sign Up Free", "Start Now", "Register Free"
]

email_labels = [
    "Email", "Email Address", "Your Email", "Email*", "E-mail", 
    "Username", "Username/Email", "Login ID", "Account Email"
]

email_placeholders = [
    "m@example.com", "your@email.com", "email@domain.com", "user@example.com",
    "Enter your email", "Your email here", "Email address", "Type your email"
]

password_labels = [
    "Password", "Password*", "Your Password", "Enter Password", 
    "Login Password", "Account Password", "Create Password"
]

forgot_password_texts = [
    "Forgot your password?", "Forgot password?", "Reset password", 
    "Can't remember password?", "Lost password?", "Password help"
]

oauth_buttons = [
    {"text": "Continue with Google"},
    {"text": "Continue with Apple"},
    {"text": "Continue with GitHub"},
    {"text": "Continue with Facebook"},
    {"text": "Continue with Twitter"},
    {"text": "Continue with LinkedIn"},
    {"text": "Continue with Microsoft"},
    {"text": "Continue with Discord"}
]

card_styles = [
    "", "shadow-lg", "shadow-xl", "border-2", "rounded-xl", "rounded-2xl",
    "shadow-md border", "bg-white shadow-lg", "border border-gray-200"
]

button_styles = [
    "", "rounded-lg", "font-semibold", "h-12", "px-6", "shadow-sm",
    "rounded-md font-medium", "py-3", "text-lg", "hover:opacity-90"
]

form_layouts = [
    "flex flex-col gap-6", "space-y-6", "grid gap-6", "flex flex-col space-y-4",
    "grid gap-4", "space-y-8", "flex flex-col gap-4"
]

field_layouts = [
    "grid gap-3", "space-y-2", "flex flex-col gap-2", "grid gap-2",
    "space-y-3", "flex flex-col space-y-1"
]

def get_color_scheme(use_colormap=True):
    if use_colormap:
        color_key = random.choice(list(colorMap.keys()))
        primary_color = colorMap[color_key]
        color_name, intensity = primary_color.split("-")
        intensity_num = int(intensity)
        
        if intensity_num >= 500:
            accent_intensity = max(300, intensity_num - 200)
            button_intensity = min(900, intensity_num + 100)
        else:
            accent_intensity = min(600, intensity_num + 100)
            button_intensity = min(700, intensity_num + 200)
            
        return {
            "primary": f"{color_name}-{intensity}",
            "accent": f"{color_name}-{accent_intensity}",
            "button": f"{color_name}-{button_intensity}",
            "color_name": color_key
        }
    else:
        color = random.choice(colors)
        base_intensity = random.choice([300, 400, 500, 600, 700])
        
        accent_intensity = max(200, base_intensity - 100)
        button_intensity = min(800, base_intensity + 100)
        
        return {
            "primary": f"{color}-{base_intensity}",
            "accent": f"{color}-{accent_intensity}",
            "button": f"{color}-{button_intensity}",
            "color_name": color.capitalize()
        }

def generate_oauth_buttons(num_buttons,colors_scheme, button_style="" ):
    selected_buttons = random.sample(oauth_buttons, num_buttons)
    oauth_html = ""
    
    for btn in selected_buttons:
        oauth_html += f'''<Button variant="outline" className="w-full text-white border border-{colors_scheme['accent']} bg-{colors_scheme['accent']} {button_style}">
                  {btn['text']}
                </Button>
'''
    
    return oauth_html.rstrip('\n')

def generate_form_code(is_login=True):
    colors_scheme = get_color_scheme(random.choice([True, False]))
    
    if is_login:
        title = random.choice(login_titles)
        description = random.choice(login_descriptions)
        main_button_text = random.choice(login_button_texts)
        alt_text = random.choice(["Don't have an account?", "New user?", "Need an account?"])
        alt_link = random.choice(["Sign up", "Register", "Create account"])
        include_forgot = random.choice([True, False])
    else:
        title = random.choice(register_titles)
        description = random.choice(register_descriptions)
        main_button_text = random.choice(register_button_texts)
        alt_text = random.choice(["Already have an account?", "Existing user?", "Have an account?"])
        alt_link = random.choice(["Sign in", "Login", "Log in"])
        include_forgot = False  
    
    email_label = random.choice(email_labels)
    email_placeholder = random.choice(email_placeholders)
    password_label = random.choice(password_labels)
    num_oauth = random.randint(0, 3)  
    
    card_style = random.choice(card_styles)
    button_style = random.choice(button_styles)
    form_layout = random.choice(form_layouts)
    field_layout = random.choice(field_layouts)
    
    forgot_password_link = ""
    if include_forgot and is_login:
        forgot_text = random.choice(forgot_password_texts)
        forgot_password_link = f'''                  <a
                    href="#"
                    className="ml-auto inline-block text-sm text-{colors_scheme['accent']} underline-offset-4 hover:underline"
                  >
                    {forgot_text}
                  </a>'''
    
    oauth_section = ""
    if num_oauth > 0:
        oauth_buttons_html = generate_oauth_buttons(num_oauth,colors_scheme, button_style)
        oauth_section = f'''
{oauth_buttons_html}'''
    
    form_code = f'''<Card{' className="'+ "bg-"+colors_scheme['primary'] + " " + card_style + '"' if card_style else ''}>
        <CardHeader>
          <CardTitle>{title}</CardTitle>
          <CardDescription>
            {description}
          </CardDescription>
        </CardHeader>
        <CardContent>
          <form>
            <div className="{form_layout}">
              <div className="{field_layout}">
                <Label htmlFor="email">{email_label}</Label>
                <Input
                  id="email"
                  type="email"
                  placeholder="{email_placeholder}"
                  required
                  className="bg-{colors_scheme['accent']} border border-{colors_scheme['accent']}"
                />
              </div>
              <div className="{field_layout}">
                <div className="flex items-center">
                  <Label className="text-{colors_scheme['accent']}" htmlFor="password">{password_label}</Label>{forgot_password_link}
                </div>
                <Input className="bg-{colors_scheme['accent']} border border-{colors_scheme['accent']}"
  id="password" type="password" required />
              </div>
              <div className="flex flex-col gap-3">
                <Button type="submit" className="w-full text-{colors_scheme['accent']} bg-{colors_scheme['button']} {button_style}">
                  {main_button_text}
                </Button>{oauth_section}
              </div>
            </div>
            <div className="mt-4 text-center text-sm text-{colors_scheme['accent']}">
              {alt_text}{" "}
              <a href="#" className="underline underline-offset-4">
                {alt_link}
              </a>
            </div>
          </form>
        </CardContent>
      </Card>'''
    
    return form_code, colors_scheme, title, is_login

def generate_prompt(form_details, colors_scheme):
    """Generiert entsprechenden Prompt"""
    template_type = random.choices(
        ["simple", "medium", "complex"], 
        weights=[20, 40, 40]
    )[0]
    
    form_type = "login" if form_details['is_login'] else "register"
    title = form_details['title'].lower()
    
    if template_type == "simple":
        templates = [
            f"Create a {colors_scheme['color_name'].lower()} {form_type} form",
            f"Build {colors_scheme['color_name'].lower()} {title} component",
            f"Generate {colors_scheme['color_name'].lower()} {form_type} interface",
            f"Make {colors_scheme['color_name'].lower()} {title} form"
        ]
        return random.choice(templates)
    
    elif template_type == "medium":
        templates = [
            f"Create a {colors_scheme['color_name'].lower()} {form_type} form with email and password fields",
            f"Build a {colors_scheme['color_name'].lower()} {title} component with social login options",
            f"Generate a {form_type} interface with OAuth buttons and {colors_scheme['color_name'].lower()} colors",
            f"Make a {title} form {colors_scheme['color_name'].lower()} with multiple signin options"
        ]
        return random.choice(templates)
    
    else: 
        features = ["modern design", "rounded corners", "shadow effects", "responsive layout"]
        feature = random.choice(features)
        templates = [
            f"Create a {form_type} form with {colors_scheme['color_name'].lower()} theme and {feature}",
            f"Build a {title} component using {colors_scheme['color_name'].lower()} colors and {feature}",
            f"Generate a {form_type} interface with {colors_scheme['color_name'].lower()} styling and {feature}",
            f"Design a {title} form featuring {colors_scheme['color_name'].lower()} buttons and {feature}"
        ]
        return random.choice(templates)

prompt_set = set()
code_set = set()
prompts = []
codes = []

target_samples = 2_500_000
attempts = 0
max_attempts = target_samples * 3


while len(prompts) < target_samples and attempts < max_attempts:
    attempts += 1
    
    is_login = random.choice([True, False])
    
    form_code, colors_scheme, title, form_type = generate_form_code(is_login)
    
    form_details = {
        'title': title,
        'is_login': is_login
    }
    prompt = generate_prompt(form_details, colors_scheme)
    
    if prompt not in prompt_set and form_code not in code_set:
        prompt_set.add(prompt.lower())
        code_set.add(form_code)
        prompts.append(prompt.lower())
        codes.append(form_code)



with open("Login_Form_Dataset_2_5m/code.txt", "w", encoding="utf-8") as f:
    for code in codes:
        f.write(code + "\n")

with open("Login_Form_Dataset_2_5m/prompts.txt", "w", encoding="utf-8") as f:
    for prompt in prompts:
        f.write(prompt + "\n")
