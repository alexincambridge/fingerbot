import time
from servo import Servo

# Crear objetos Servo asignados a pines GPIO
power = Servo(pin_id=0)
vol_up = Servo(pin_id=1)
vol_down = Servo(pin_id=2)

power.write(0)
vol_up.write(0)
vol_down.write(50)

def move_servo_slowly(servo, target_position, delay=0.05, step=1):
    current_position = servo.read()
    while abs(current_position - target_position) > step:  # Evitar bucle infinito
        if current_position < target_position:
            current_position += step
        else:
            current_position -= step
        servo.write(current_position)
        time.sleep(delay)
    servo.write(target_position)  # Garantizar posición final exacta

# Función para "Reinicio"
def reinicio(delay = 0.5):
    print("Ejecutando 'Reinicio': Presionando Power y Vol Down por 10 segundos...")
    move_servo_slowly(power, 40)    # Mover el servo power lentamente
    time.sleep(delay)
    move_servo_slowly(vol_down, 0) # Mover el servo vol_down lentamente
    time.sleep(delay)
    move_servo_slowly(power, 0)     # Regresar a la posición inicial
    move_servo_slowly(vol_down, 0)  # Regresar a la posición inicial
    print("Reinicio completo.\n")

# Función para "Boot Loader"
def boot_loader(delay=0.5):
    print("Ejecutando 'Boot Loader': Presionando Power y Vol Up por 10 segundos...")
    move_servo_slowly(power, 20)    # Mover el servo power lentamente
    move_servo_slowly(vol_up, 20)   # Mover el servo vol_up lentamente
    time.sleep(delay)
    move_servo_slowly(power, 0)     # Regresar a la posición inicial
    move_servo_slowly(vol_up, 0)    # Regresar a la posición inicial
    print("Boot Loader completo.\n")

# Función para "Factory Reset"
def factory_reset():
    print("Ejecutando 'Factory Reset': Presionando Power, Vol Up y Vol Down por 10 segundos...")
    move_servo_slowly(power, 20)    # Mover el servo power lentamente
    move_servo_slowly(vol_down, 0)  # Mover el servo vol_down lentamente
    move_servo_slowly(vol_up, 20)   # Mover el servo vol_up lentamente
    time.sleep(1)
    move_servo_slowly(power, 0)     # Regresar a la posición inicial
    move_servo_slowly(vol_down, 20) # Regresar a la posición inicial
    move_servo_slowly(vol_up, 0)    # Regresar a la posición inicial
    print("Factory Reset completo.\n")

# Función principal para elegir la acción
def main():
    while True:
        print("Elige una acción: ")
        print("1. Reinicio")
        print("2. Boot Loader")
        print("3. Factory Reset")
    
        choice = input("Ingresa el número de la acción: ")

        if choice == '1':
            reinicio()
        elif choice == '2':
            boot_loader()
        elif choice == '3':
            factory_reset()
        elif choice == '4':
            print("Saliendo del programa.")
            break  # Salir del bucle y terminar el programa
        else:
            print("Opción inválida. Por favor intenta de nuevo.\n")

if __name__ == "__main__":
    main()
