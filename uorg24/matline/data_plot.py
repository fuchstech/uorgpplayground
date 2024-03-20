import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

ser = serial.Serial('COM4', 115200, timeout=1)  # Portunuzu ayarlayın
ser.flush()

# Verileri saklamak için listeler
motor_speeds = []
positions = []

fig, ax = plt.subplots()
line1, = ax.plot(motor_speeds, label='Motor Speed')
line2, = ax.plot(positions, label='Position', linestyle='--')
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Real-Time Motor Speed and Position')
plt.legend()

def read_line():
    line_buffer = ""
    while True:
        if ser.in_waiting > 0:
            char = ser.read().decode('utf-8', errors='ignore')
            if char == '<':  # Başlangıç işaretini bulduk
                line_buffer = ""
            elif char == '>':  # Bitiş işaretini bulduk, tamponlanan veriyi döndür
                return line_buffer
            else:
                line_buffer += char

def animate(i):
    line = read_line()  # Yeni okuma fonksiyonumuzu kullan
    if line:
        try:
            motor_speed, position = line.split(", ")  # Verileri ayır
            motor_speed = int(motor_speed.split(": ")[1])
            position = int(position.split(": ")[1])
            motor_speeds.append(motor_speed)
            positions.append(position)
            if len(motor_speeds) > 30:  # Eski verileri sınırla
                motor_speeds.pop(0)
                positions.pop(0)
            line1.set_data(range(len(motor_speeds)), motor_speeds)
            line2.set_data(range(len(positions)), positions)
            ax.relim()
            ax.autoscale_view()
        except ValueError:
            print("Veri ayrıştırma hatası.")
        except IndexError as e:
            print(f"Liste index hatası: {e}")

ani = FuncAnimation(fig, animate, interval=50)

plt.show()
