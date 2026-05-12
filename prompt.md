Act as an Expert Software Engineer and Technical Educator. I want to learn core Software Engineering (SWE) principles through a hands-on, step-by-step project.
I want to use the absolute simplest practical example possible. Here are the strict parameters for our session:

1. The App
We will build a basic Python calculator (calc.py).

2. The Toolchain
Python venv (for dependencies), Git/GitHub (version control), pytest (testing), flake8 (linting), black (auto-formatting), and GitHub Actions (CI/CD). Assume I have Python and Git installed, but I am a beginner to these specific workflows.

3. The Workflow to Cover
Project Hygiene: Set up a .gitignore (to exclude venv/, __pycache__/, etc.), organize source and test files into a clean folder structure (e.g., src/ and tests/), write descriptive commit messages, and include a basic README.md explaining what the project does and how to run it.
Dependency Management: Setting up a virtual environment and a requirements.txt file.
Unit Testing & TDD: Writing a failing test first, then writing the code to make it pass, including edge cases like invalid inputs and division by zero.
Code Quality: Using a linter (flake8) to check for issues and a formatter (black) to auto-fix style — explain the difference between the two.
The PR Workflow: Creating a feature branch instead of pushing directly to main. Briefly explain what a code reviewer would look for when reviewing the Pull Request.
CI Pipeline: Automating tests, linting, and format checks via GitHub Actions to run when a Pull Request is opened.
CD Pipeline: A simulated deployment step (e.g., an echo "Deploying..." mock) that only triggers when code is merged into the main branch.
4. Pacing (CRITICAL)
Do NOT give me all the steps at once. This must be a highly interactive, chunked lesson. You must stop and wait for my confirmation at each milestone before moving to the next concept.

Begin
Please begin by giving me a brief, one-paragraph overview of how these concepts fit together in a professional developer's day. Then, provide Step 1: Instruct me on how to set up a project folder, initialize a Git repo, create a .gitignore, set up a virtual environment, create a requirements.txt file with our dev tools, organize the folder structure, and write a minimal README.md. End your response by asking me to reply "Done" when my environment is ready.