import dbus
import time

import colorama
from colorama import Fore, Style

from gi.repository import GLib
from dbus.mainloop.glib import DBusGMainLoop


def process_notification(session_bus, signal_message):
    """
    Process message and print payload to stdout.

        session_bus: SessionBus (current login message bus)
        message: SignalMessage (which can be sent or received over a D-Bus)

        Message arguments depend on a member. For the 'org.freedesktop.Notifications.Notify' there are:
            String app_name
            UInt32 replaces_id
            String app_icon
            String summary
            String body
            Array of [String] actions
            Dict of {String, Variant} hints
            Int32 timeout
    """
    if not signal_message.get_member() == "Notify":
        return

    message = signal_message.get_args_list()
    app_title = message[0]
    message_title = message[3]
    message_body = message[4]
    current_time = f'{time.localtime().tm_hour}:{time.localtime().tm_min}'
    print(f'---[ {Fore.YELLOW}{app_title}{Style.RESET_ALL} at {current_time} ]---')
    print(f'{message_title}')
    print(f'{message_body}', end='\n\n')


if __name__ == '__main__':
    colorama.init()
    DBusGMainLoop(set_as_default=True)

    bus = dbus.SessionBus()
    bus.add_match_string_non_blocking("eavesdrop=true, interface='org.freedesktop.Notifications'")
    bus.add_message_filter(process_notification)

    mainloop = GLib.MainLoop()
    mainloop.run()
