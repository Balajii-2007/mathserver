from django.shortcuts import render

def index(request):
    result = None
    if request.method == 'POST':
        try:
            intensity = float(request.POST.get('intensity', '0'))
            resistance = float(request.POST.get('resistance', '0'))
            power = intensity * intensity * resistance
            result = f'Power (P) = {power:.2f} W'
        except (ValueError, TypeError):
            result = 'Please enter valid positive numbers.'
    
    return render(request, "mathapp/index.html", {'result': result})
