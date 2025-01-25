# heos-link-control-proxy
A proxy that will accept messages from a Denon Heos Link and proxy them to a non Denon receiver.

This allows the Link to be connected to a non Denon/Marantz receiver but still:
1) Power on the amplifier
2) Set the source of the amplifier to the one that the HEOS link is connected to
3) Set the volume of the amplifier

The non Denon receiver will need some way to be controlled via IP setup. Initial implementation of this proxy will use Home Assistant
However Pioneer/Onkyo have IP control so a module could be written for them.
