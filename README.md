# python_pinger

This is a simpple script in python to check if a host is up or down.

Only create a class instance

	pinger = Pinger()

And call the methods

For example, for to do ping to 1 host 

	pinger.do_list_ping()

And if you want to do ping to multiple hosts edit the method get_ips and put your IPS in the list, and the call the method

	pinger.do_list_ping()