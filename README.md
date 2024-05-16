Python is the most preffered language for test automation
This is a web automation demo in  python using pytest framework
It logs in to https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
Navigates to leave on the drawer menu
Fills out a form
# prerequisites
install pycharm IDE
install pytest
install git
git clone <repository_name>
# Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Unix/Mac

# Install or update dependencies
pip install -r requirements.txt
# run
pytest --html=report.html
