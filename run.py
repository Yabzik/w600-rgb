from micropyserver import MicroPyServer
srv = MicroPyServer()

from machine import Pin, PWM

def write_set(sets):
    f = open('rgb', 'w')
    f.write(' '.join(sets))
    f.close()

def read_set():
    f = open('rgb')
    sb = f.read()
    f.close()
    return sb.split(' ')

def set_rgb(sets):
    write_set(sets)
    pwm_red.duty(int(sets[0]))
    pwm_green.duty(int(sets[1]))
    pwm_blue.duty(int(sets[2]))


def show_index(request):
    html_file = open("index.html")
    html = html_file.read()
    html_file.close()
    srv.send(html, content_type="Content-Type: text/html")

def reboot(request):
    srv.send('rebootin')
    import machine
    machine.reset()

def rgb(request):
    srv.send('ok')
    params = request.split("\n")[0].split(' ')[1].replace('/rgb?', '').split('&')
    for i in range(3):
        params[i] = params[i][2:]

    print(params)

    set_rgb(params)

# R - PB16
# G - PB18
# B - PB15
pwm_green = PWM(Pin(Pin.PB_16), channel=2, freq=2500, duty=0)
pwm_red = PWM(Pin(Pin.PB_18), channel=0, freq=2500, duty=0)
pwm_blue = PWM(Pin(Pin.PB_15), channel=3, freq=2500, duty=0)
set_rgb(read_set())

srv.add_route("/", show_index)
srv.add_route("/reboot", reboot)
srv.add_route("/rgb", rgb)
srv.start()