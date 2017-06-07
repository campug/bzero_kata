# bzero kata
This repository is the code used at the CamPUG meeting of Tuesday 6th June 2017

There are some slides that are an introduction to Bluetooth used to set the context for this practical
programming session based on BlueZ (which is the official Bluetooth protocol stack on Linux). 

BlueZ has an API (using the DBus software bus) for Python which provides the backdrop for this hands on challenge. 

Barry has created a mock of DBus's GetManagedObjects() so tests can be run on any operating system without real Bluetooth hardware. 
The mock GetManagedObjects() method returns all the information the system knows about Bluetooth devices within range. 

The challenge will be to extract certain key information from the returned nested dictionaries. 

More instructions are available in the PDF
