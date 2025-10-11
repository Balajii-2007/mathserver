# Ex.05 Design a Website for Server Side Processing
# Date:10/10/2025
# AIM:
To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side.

# FORMULA:
P = I2R
P --> Power (in watts)
 I --> Intensity
 R --> Resistance

# DESIGN STEPS:
## Step 1:
Clone the repository from GitHub.

## Step 2:
Create Django Admin project.

## Step 3:
Create a New App under the Django Admin project.

## Step 4:
Create python programs for views and urls to perform server side processing.

## Step 5:
Create a HTML file to implement form based input and output.

## Step 6:
Publish the website in the given URL.

# PROGRAM :
```
math.html

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Incandescent Bulb Power Calculator</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #b409a3;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
    }

    .circle-wrapper {
      width: 400px;
      height: 400px;
      background: rgb(122, 2, 149);
      border-radius: 50%;
      display: flex;
      justify-content: center;
      align-items: center;
      box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }

    .calculator {
      background: white;
      padding: 25px;
      border-radius: 12px;
      width: 80%;
      text-align: center;
    }

    h2 {
      color: #b50a90;
      margin-bottom: 15px;
      font-size: 18px;
    }

    label {
      display: block;
      margin: 10px 0 5px;
      font-weight: bold;
      text-align: left;
      font-size: 14px;
    }

    input {
      width: 100%;
      padding: 8px;
      border: 1px solid #b40ab4;
      border-radius: 6px;
      margin-bottom: 10px;
    }

    button {
      background: #cf08e5;
      color: white;
      border: none;
      padding: 10px;
      border-radius: 6px;
      cursor: pointer;
      width: 100%;
      font-size: 15px;
    }

    button:hover {
      background: #850456;
    }

    #result {
      margin-top: 15px;
      font-size: 16px;
      font-weight: bold;
      color: #df1899;
    }

    @media (max-width: 450px) {
      .circle-wrapper {
        width: 2cm;
        height: 2cm;
        border-radius: 50%;
      }

      .calculator {
        width: 80%;
      }
    }
  </style>
</head>
<body>

  <div class="circle-wrapper">
    <div class="calculator">
      <h2>Power Calculator</h2>
      <form onsubmit="calculatePower(event)">
        <label for="intensity">Intensity (I) :</label>
        <input type="number" id="intensity" step="any" required>

        <label for="resistance">Resistance (R) :</label>
        <input type="number" id="resistance" step="any" required>

        <button type="submit">Calculate Power</button>
      </form>
      <p id="result"></p>
    </div>
  </div>

  <script>
    function calculatePower(event) {
      event.preventDefault();

      let I = parseFloat(document.getElementById("intensity").value);
      let R = parseFloat(document.getElementById("resistance").value);

      if (isNaN(I) || isNaN(R) || I < 0 || R < 0) {
        document.getElementById("result").innerText = "⚠ Please enter valid positive numbers.";
        return;
      }

      let P = I * I * R;
      document.getElementById("result").innerText = "Power (P) = " + P.toFixed(2) + " Watts";
    }
  </script>

</body>
</html>

views.py

from django.shortcuts import render

def power_calculator(request):
    context = {}
    context['result'] = "0"
    context['I'] = "0"
    context['R'] = "0"
    context['steps'] = ""

    if request.method == 'POST':
        print("POST method is used")
        I = request.POST.get('intensity', '0')
        R = request.POST.get('resistance', '0')

        try:
            I = float(I)
            R = float(R)
            P = I * I * R   # Formula: P = I² × R
            result = round(P, 2)

            context['result'] = result
            context['I'] = I
            context['R'] = R
            context['steps'] = f"P = I² × R = {I}² × {R} = {round(I*I, 2)} × {R} = {result} W"

            print("Intensity:", I)
            print("Resistance:", R)
            print("Power:", result)

        except:
            context['result'] = "Invalid Input"

    return render(request, 'mathapp/math.html', context)

urls.py

from django.contrib import admin
from django.urls import path
from mathapp import views  # Ensure 'mathapp' is your app name

urlpatterns = [
    path('admin/', admin.site.urls),

    # Route for power calculator
    path('', views.power_calculator, name='power_calculator'),
]
```
# SERVER SIDE PROCESSING:
![BALAJI 5(1)](https://github.com/user-attachments/assets/0d8d59ac-041c-4612-bf6c-b536e70c6f0f)

# HOMEPAGE:
![BALAJI 5](https://github.com/user-attachments/assets/bdfcc3df-486c-4900-af20-31c1590ee6c9)

# RESULT:
The program for performing server side processing is completed successfully.
