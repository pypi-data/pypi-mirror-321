import os
import sys
import time
import threading
import psutil
import subprocess
import qrcode
import zipfile
import platform
import getpass

# Importa la clase XSleep desde el módulo _xsleep
from timexus import XSleep

class ExtraFunctions:

    @staticmethod
    def monitor_file_changes(filepath, callback):
        """
        Supervisa un archivo específico y ejecuta una función de devolución de llamada (callback) si el archivo cambia.

        Args:
            filepath (str): La ruta del archivo a supervisar.
            callback (callable): La función a ejecutar cuando el archivo cambie.
        """
        last_modified = os.path.getmtime(filepath)
        while True:
            current_modified = os.path.getmtime(filepath)
            if current_modified != last_modified:
                last_modified = current_modified
                callback()
            XSleep.seconds(1)  # Usa XSleep.seconds() en lugar de time.sleep()

    @staticmethod
    def get_network_status():
        """
        Devuelve el estado de la conexión a Internet (conectado o no).
        """
        try:
            # Intenta hacer una conexión a un servidor conocido
            socket.create_connection(("www.google.com", 80))
            return True
        except OSError:
            return False

    @staticmethod
    def get_system_temperature():
        """
        Obtiene la temperatura actual de la CPU si el hardware lo admite.
        """
        try:
            temps = psutil.sensors_temperatures()
            if temps:
                # Considera la primera temperatura como la de la CPU
                for entry in temps['coretemp']:
                    if 'Core 0' in entry.label:
                        return entry.current
                return None
            else:
                print("No se pudo obtener la temperatura de la CPU.")
                return None
        except Exception as e:
            print(f"Error al obtener la temperatura: {e}")
            return None

    @staticmethod
    def list_usb_devices():
        """
        Enumera todos los dispositivos USB conectados al sistema.
        """
        try:
            devices = psutil.disk_partitions(all=True)
            usb_devices = [d for d in devices if 'removable' in d.opts]
            return usb_devices
        except Exception as e:
            print(f"Error al listar los dispositivos USB: {e}")
            return []

    @staticmethod
    def compress_files(file_paths, output_path, compression_level=5):
        """
        Comprime una lista de archivos en un archivo .zip con un nivel de compresión ajustable.

        Args:
            file_paths (list): Lista de rutas de archivos a comprimir.
            output_path (str): Ruta donde se guardará el archivo .zip.
            compression_level (int): Nivel de compresión (0-9, donde 9 es la máxima compresión).
        """
        if not 0 <= compression_level <= 9:
            raise ValueError("El nivel de compresión debe estar entre 0 y 9")
        try:
            with zipfile.ZipFile(output_path, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=compression_level) as zf:
                for file_path in file_paths:
                    if os.path.isfile(file_path):
                        zf.write(file_path, os.path.basename(file_path))
                    else:
                        print(f"Advertencia: {file_path} no es un archivo válido y no se incluirá en el zip")
            print(f"Archivos comprimidos en: {output_path}")
        except Exception as e:
            print(f"Error al comprimir archivos: {e}")

    @staticmethod
    def extract_zip(zip_path, extract_to):
        """
        Extrae un archivo .zip en la ruta especificada.

        Args:
            zip_path (str): Ruta del archivo .zip a extraer.
            extract_to (str): Directorio donde se extraerán los archivos.
        """
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to)
            print(f"Archivos extraídos en: {extract_to}")
        except Exception as e:
            print(f"Error al extraer el archivo zip: {e}")

    @staticmethod
    def generate_qr_code(data, filename="qrcode.png"):
        """
        Genera un código QR a partir de un texto o URL y lo guarda como una imagen.

        Args:
            data (str): El texto o URL para el código QR.
            filename (str): El nombre del archivo de imagen a guardar (por defecto "qrcode.png").
        """
        try:
            img = qrcode.make(data)
            img.save(filename)
            print(f"Código QR generado y guardado como {filename}")
        except Exception as e:
            print(f"Error al generar el código QR: {e}")
            return None

    @staticmethod
    def get_power_mode():
        """
        Retorna el modo de energía del sistema (por ejemplo: "Alto rendimiento", "Ahorro de energía").
        """
        try:
            if platform.system() == "Windows":
                # Ejecuta el comando powercfg para obtener el plan de energía actual
                output = subprocess.check_output(["powercfg", "/getactivescheme"], text=True)
                return output.strip()
            elif platform.system() == "Linux":
                # Intenta leer el archivo de configuración de energía
                with open("/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor", "r") as f:
                    return f.read().strip()
            elif platform.system() == "Darwin":
                # Ejecuta el comando pmset para obtener la configuración de energía actual
                output = subprocess.check_output(["pmset", "-g", "active"], text=True)
                return output.strip()
            else:
                return "Plataforma no soportada"
        except Exception as e:
            print(f"Error al obtener el modo de energía: {e}")
            return None

    @staticmethod
    def lock_system():
        """
        Bloquea la sesión actual del sistema operativo.
        """
        try:
            if sys.platform.startswith("win32"):
                ctypes.windll.user32.LockWorkStation()
            elif sys.platform.startswith("linux"):
                subprocess.run(["xdg-screensaver", "lock"])
            elif sys.platform.startswith("darwin"):
                subprocess.run(["/System/Library/CoreServices/Menu Extras/User.menu/Contents/Resources/CGSession", "-suspend"])
            else:
                print("Bloqueo de sistema no soportado en esta plataforma.")
        except Exception as e:
            print(f"Error al bloquear el sistema: {e}")

    @staticmethod
    def get_process_memory_usage(pid):
        """
        Devuelve el uso actual de memoria en bytes de un proceso específico por su ID.

        Args:
            pid (int): El ID del proceso.

        Returns:
            int: El uso de memoria en bytes, o None si hay un error.
        """
        try:
            process = psutil.Process(pid)
            return process.memory_info().rss
        except psutil.NoSuchProcess:
            print(f"No se encontró un proceso con el PID {pid}.")
            return None
        except Exception as e:
            print(f"Error al obtener el uso de memoria del proceso: {e}")
            return None