# Sentiment-analyzer

Follow these instructions to set up and run the project locally.
### Prerequisites

Make sure you have the following installed on your machine:

- Python (3.7 or higher)
- pip (Python package installer)
- Django

### Installation

1. **Clone the Repository:**
```
git clone https://github.com/vinay-s36/Sentiment-analyzer.git
```
2. **Navigate to the Project Directory:**
```
cd Sentiment-analyzer
```
3. **Create a Virtual Environment (Optional but recommended):**
```
python -m venv venv
```
4. **Activate the Virtual Environment:**
- On Windows:
```
venv\Scripts\activate
```
- On macOS/Linux:
```
source venv/bin/activate
```
5. **Install Dependencies:**
```
pip install -r requirements.txt
```
6. **Run Migrations:**
```
python manage.py migrate
```
7. **Downloading KNN Model:**
   - Click on the following link to download the model file: [knn_model](https://www.dropbox.com/scl/fi/zp9yviz08ju6mwodkfqyx/knn_model.pkl?rlkey=et671cy106ob7kki0hkwsb708&dl=0)
   - Save the downloaded model file (knn_model.pkl) in the **'backendapp'** directory.
     
8. **Run the Development Server:**
```
python manage.py runserver
```
The development server will start running at `http://127.0.0.1:8000/`

### Happy coding! 🚀

### Contributors: [Vivek](https://github.com/VivekGuruduttK28) [Vanesh](https://github.com/Vanesh37) [Vishal](https://github.com/VykSI)
