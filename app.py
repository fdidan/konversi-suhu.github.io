from browser import document, console, alert

input = document['input']
button = document['btn']
output0 = document['output0']
output1 = document['output1']
output2 = document['output2']
select = document['select']

def getNum(x):
    temp = x
    try:
        temp = int(x)
    except ValueError:
        temp = float(x)
    finally:
        if temp != '' and type(temp) is str:
            alert('Harap masukkan angka')
            temp = ''
            input.value = temp
            return temp
        else:
            return temp

def formula(x, y):
    if x == 'Celcius':
        fahrenheit = 'Fahrenheit = ' + str(y * (9/5) + 32)
        kelvin = 'Kelvin = ' + str(y + 273)
        reamur = 'Reamur = ' + str((4/5) * y)
        return fahrenheit, kelvin, reamur
    elif x == 'Fahrenheit':
        celcius = 'Celcius = ' + str((5/9) * (y - 32))
        kelvin = 'Kelvin = ' + str((5/9) * (y - 32) + 273)
        reamur = 'Reamur = ' + str((4/9) * (y - 32))
        return celcius, kelvin, reamur
    elif x == 'Kelvin':
        celcius = 'Celcius = ' + str(y - 273)
        fahrenheit = 'Fahrenheit = ' + str((9/5) * (y - 273) + 32)
        reamur = 'Reamur = ' + str((4/5) * (y - 273))
        return celcius, fahrenheit, reamur
    elif x == 'Reamur':
        celcius = 'Celcius = ' + str((5/4) * y)
        fahrenheit = 'Fahrenheit = ' + str((9/4) * y + 273)
        kelvin = 'Kelvin = ' + str((5/4) * y + 273)
        return celcius, fahrenheit, kelvin
    else :        
        return 0


def main(ev):
    num = getNum(input.value)
    result = formula(select.value, num)
    output0.textContent = result[0]
    output1.textContent = result[1]
    output2.textContent = result[2]

def keyEnter(ev):
    console.log(f"{ev.code}")
    traceKey = f"{ev.code}"
    if traceKey == 'Enter':
        main(0)
        
button.bind('click', main)
input.bind("keypress", keyEnter)
