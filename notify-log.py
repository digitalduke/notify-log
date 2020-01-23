import dbus

from gi.repository import GLib
from dbus.mainloop.glib import DBusGMainLoop


def process_notification(session_bus, signal_message):
    if signal_message.get_member() == "Notify":
        for arg in signal_message.get_args_list():
            print(arg)


if __name__ == '__main__':
    DBusGMainLoop(set_as_default=True)

    bus = dbus.SessionBus()
    bus.add_match_string_non_blocking("eavesdrop=true, interface='org.freedesktop.Notifications'")
    bus.add_message_filter(process_notification)

    mainloop = GLib.MainLoop()
    mainloop.run()
