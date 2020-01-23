import dbus

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
