from sse_connect import app 
from pydantic import BaseModel
import random
from random import randint
from datetime import datetime
print("Initializing endpoints...")


# Endpoint for pie chart data
@app.get("/api/pie-chart-data")
async def get_pie_chart_data():
    # Generate random data for the pie chart (percentage breakdown)
    data = [randint(10, 60) for _ in range(3)]  # Random data for 3 categories
    # Ensure the total is 100 by adjusting the last value
    total = sum(data)
    data[2] = 100 - (data[0] + data[1])

    labels = ["Positive", "Neutral", "Negative"]
    return {"labels": labels, "data": data} 


@app.get("/api/bar-chart-data")
async def get_bar_chart_data():
    # Generate random data for the chart (6 months for example)
    months = ["January", "February", "March", "April", "May", "June"]
    revenue = [randint(3000, 15000) for _ in range(6)]  # Random revenue for 6 months

    return JSONResponse(content={"labels": months, "data": revenue})

@app.get("/api/bubble-chart-data")
async def get_chart_data():
    return {
        "x": [1, 2, 3, 4],
        "y": [random.randint(5, 20) for _ in range(4)],  # Random Y values
        "size": [random.randint(20, 100) for _ in range(4)]  # Random marker sizes
    }


# Endpoint to get initial chart data
@app.get("/api/chart-data")
async def get_chart_data():
    return {
        "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "data": [random.randint(5000, 40000) for _ in range(12)]
    }

# Endpoint to get updated chart data at intervals
@app.get("/api/chart-update")
async def update_chart_data():
    return {
        "data": [random.randint(5000, 40000) for _ in range(12)]
    }


# Endpoint for heatmap data
@app.get("/api/heatmap-data")
async def get_heatmap_data():
    # Generate random data for the heatmap
    z = [[randint(-10, 100) if randint(0, 1) else None for _ in range(5)] for _ in range(3)]  # 3x5 matrix with random numbers
    x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    y = ['Morning', 'Afternoon', 'Evening']

    return {"x": x, "y": y, "z": z}

language_data = [
    {"x": "Mandarin Chinese", "value": 1090000000, "category": "Sino-Tibetan"},
    {"x": "English", "value": 983000000, "category": "Indo-European"},
    {"x": "Hindustani", "value": 544000000, "category": "Indo-European"},
    {"x": "Spanish", "value": 527000000, "category": "Indo-European"},
    {"x": "Arabic", "value": 422000000, "category": "Afro-Asiatic"},
    {"x": "Malay", "value": 281000000, "category": "Austronesian"},
    {"x": "Russian", "value": 267000000, "category": "Indo-European"},
    {"x": "Bengali", "value": 261000000, "category": "Indo-European"},
    {"x": "Portuguese", "value": 229000000, "category": "Indo-European"},
    {"x": "French", "value": 229000000, "category": "Indo-European"},
    {"x": "Hausa", "value": 150000000, "category": "Afro-Asiatic"},
    {"x": "Punjabi", "value": 148000000, "category": "Indo-European"},
    {"x": "Japanese", "value": 129000000, "category": "Japonic"},
    {"x": "German", "value": 129000000, "category": "Indo-European"},
    {"x": "Persian", "value": 121000000, "category": "Indo-European"}
]

# Endpoint to get language data with randomized frequencies
@app.get("/api/language-data")
async def get_language_data():
    # Randomize the population (value) for each language
    for lang in language_data:
        lang["value"] = random.randint(100000000, 1200000000)  # Randomize the frequency in range
    return {"data": language_data}



class ProgressData(BaseModel):
    label: str
    percentage: int
    color: str

def get_color_for_percentage(percentage: int) -> str:
    """Function to return a color based on the percentage value."""
    if percentage >= 80:
        return "bg-success"  # Green for 80% or more
    elif percentage >= 60:
        return "bg-info"  # Blue for 60%-79%
    elif percentage >= 40:
        return "bg-warning"  # Yellow for 40%-59%
    else:
        return "bg-danger"  # Red for below 40%

@app.get("/api/progress-data")
async def get_progress_data():
    # Create data with random percentages and their corresponding colors
    data = [
        {"label": "January", "percentage": random.randint(0, 100), "color": ""},
        {"label": "February", "percentage": random.randint(0, 100), "color": ""},
        {"label": "March", "percentage": random.randint(0, 100), "color": ""},
        {"label": "April", "percentage": random.randint(0, 100), "color": ""},
        {"label": "May", "percentage": random.randint(0, 100), "color": ""}
    ]
    
    # Update color based on percentage
    for entry in data:
        entry["color"] = get_color_for_percentage(entry["percentage"])
    
    return {"data": data}


class EmployeeData(BaseModel):
    name: str
    position: str
    office: str
    age: int
    date_of_joining: str
    salary: str

def generate_random_data():
    positions = ["Software Engineer", "Javascript Developer", "Customer Support", "Product Manager", "Data Scientist"]
    offices = ["New York", "Singapore", "San Francisco", "London", "Tokyo"]
    salary_range = [80000, 100000, 120000, 140000, 160000, 180000, 200000]

    data = []
    for _ in range(5):  # Generate data for 5 employees
        name = f"Employee {random.randint(1, 100)}"
        position = random.choice(positions)
        office = random.choice(offices)
        age = random.randint(22, 50)
        date_of_joining = datetime.now().strftime("%Y/%m/%d")
        salary = f"${random.choice(salary_range):,}"
        
        data.append({
            "name": name,
            "position": position,
            "office": office,
            "age": age,
            "date_of_joining": date_of_joining,
            "salary": salary
        })
    
    return data

@app.get("/api/employee-data")
async def get_employee_data():
    data = generate_random_data()
    return {"data": data}

class SocialMediaData(BaseModel):
    total_likes: int
    total_followers: int
    total_comments: int
    total_shares: int

@app.get("/api/social-media-data", response_model=SocialMediaData)
async def get_social_media_data():
    return SocialMediaData(
        total_likes=random.randint(10000, 500000),
        total_followers=random.randint(100000, 1000000),
        total_comments=random.randint(1000, 100000),
        total_shares=random.randint(5000, 500000)
    )