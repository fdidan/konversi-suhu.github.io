from browser import document, console, alert

input = document['suhu']
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
    if x == 'celcius':
        fahrenheit = 'Fahrenheit = ' + str(y * 1.8 + 32)
        kelvin = 'Kelvin = ' + str(y + 273)
        reamur = 'Reamur = ' + str(0.8 * y)
        return fahrenheit, kelvin, reamur
    elif x == 'fahrenheit':
        celcius = 'Celcius = ' + str(5/9 * (y - 32))
        kelvin = 'Kelvin = ' + str(5/9 * (y - 32) + 273)
        reamur = 'Reamur = ' + str(4/9 * (y - 32))
        return celcius, kelvin, reamur
    elif x == 'kelvin':
        celcius = 'Celcius = ' + str(5/9 * (y - 32))
        fahrenheit = 'Fahrenheit = ' + str(5/9 * (y - 32) + 273)
        reamur = 'Reamur = ' + str(4/9 * (y - 32))
        return celcius, fahrenheit, reamur
    elif x == 'reamur':
        celcius = 'Celcius = ' + str(5/9 * (y - 32))
        fahrenheit = 'Fahrenheit = ' + str(5/9 * (y - 32) + 273)
        kelvin = 'Reamur = ' + str(4/9 * (y - 32))
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