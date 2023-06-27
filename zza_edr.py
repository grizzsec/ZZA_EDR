import pyinotify
import os

class ZZAEDRHandler(pyinotify.ProcessEvent):
    def __init__(self, config):
        super().__init__()
        self.config = config

    def process_default(self, event):
        if self.config["monitor_all_events"]:
            event_type = self.get_event_type(event)
            print(f"{event_type}: {event.pathname}")

            # Ejecutar acción de respuesta al evento detectado
            self.execute_response_action(event_type, event.pathname)

    def process_IN_CREATE(self, event):
        if self.config["monitor_file_creation"]:
            print(f"Archivo creado: {event.pathname}")
            self.execute_response_action("Creación", event.pathname)

    def process_IN_DELETE(self, event):
        if self.config["monitor_file_deletion"]:
            print(f"Archivo eliminado: {event.pathname}")
            self.execute_response_action("Eliminación", event.pathname)

    def process_IN_MODIFY(self, event):
        if self.config["monitor_file_modification"]:
            print(f"Archivo modificado: {event.pathname}")
            self.execute_response_action("Modificación", event.pathname)

    def process_IN_ACCESS(self, event):
        if self.config["monitor_file_access"]:
            print(f"Archivo accedido: {event.pathname}")
            self.execute_response_action("Acceso", event.pathname)

    @staticmethod
    def get_event_type(event):
        if event.mask & pyinotify.IN_CREATE:
            return "Creación"
        elif event.mask & pyinotify.IN_DELETE:
            return "Eliminación"
        elif event.mask & pyinotify.IN_MODIFY:
            return "Modificación"
        elif event.mask & pyinotify.IN_ACCESS:
            return "Acceso"
        else:
            return "Desconocido"

    @staticmethod
    def execute_response_action(event_type, file_path):
        # Agrega aquí la lógica para realizar acciones de respuesta según el tipo de evento y el archivo afectado
        # Por ejemplo, puedes enviar una notificación, generar un registro, bloquear el archivo, etc.
        print(f"Acción de respuesta ejecutada para el evento {event_type} en el archivo {file_path}")

def start_zza_edr_monitoring(path, config):
    wm = pyinotify.WatchManager()
    handler = ZZAEDRHandler(config)
    notifier = pyinotify.Notifier(wm, handler)

    events = pyinotify.IN_CLOSE_WRITE | pyinotify.IN_DELETE | pyinotify.IN_MODIFY | pyinotify.IN_ACCESS
    wm.add_watch(path, events, rec=True)

    print(f"ZZA EDR - Monitoreando el directorio: {path}")
    notifier.loop()

# Configuración personalizada
config = {
    "monitor_all_events": False,
    "monitor_file_creation": True,
    "monitor_file_deletion": True,
    "monitor_file_modification": True,
    "monitor_file_access": False
}

# Preguntas al usuario para personalizar la configuración
print("ZZA EDR - Configuración:")
config["monitor_all_events"] = input("¿Desea monitorear todos los eventos? (s/n): ").lower() == "s"
config["monitor_file_creation"] = input("¿Desea monitorear la creación de archivos? (s/n): ").lower() == "s"
config["monitor_file_deletion"] = input("¿Desea monitorear la eliminación de archivos? (s/n): ").lower() == "s"
config["monitor_file_modification"] = input("¿Desea monitorear la modificación de archivos? (s/n): ").lower() == "s"
config["monitor_file_access"] = input("¿Desea monitorear el acceso a archivos? (s/n): ").lower() == "s"

# Ejemplo de uso con la configuración personalizada
start_zza_edr_monitoring("/path/to/directory", config)
