# Graphic User Interface

The ``gui`` package contains the code necessary for the graphics user interface of the application.

The primary class in this package is ``GUI``, which creates and manages the gui for the application.

It consists of a number of elements, with varying degrees of configurability.

## Elements

This section describes the three element groups ``Video Stream``, ``Main Controls Column``
and ``Miscellaneous Controls``.

### Video Stream

A main element of the interface is the video stream. It is placed in the upper left corner of the window. The default
configuration simply displays a static ``.png`` image.

### Main Controls Column

All primary controls are displayed in the column to the right of the video stream. These controls are:

* **Drive** Enables the user to change between high drive, and low drive
* **Gear** Enables the user to change gear
* **Throttle** Enables the user to change throttle
* **Direction** Enables the user to change vehicle direction

### Miscellaneous Controls

The miscellaneous controls group is by far the most customizable, as it is where all vehicle-specific controls are
displayed and available. Examples of controls in this section could be *lights controls*, *vanity features*, *music*,
etc.

## Configuration

This section described how the aforementioned elements are configured.

### Video Stream

To define what is shown in the video stream element, a ``VideoViewer`` defining the new behaviour is simply specified in
the ``GUI`` constructor

### Main Controls Column

Each of the elements in this column, can be enabled/disabled as needed, to be compatible with different types of
vehicles

This is done through the ``enabled`` parameter in the ``GUI`` constructor. This parameter defaults to all-enabled, and
id specified by passing a map between element-identifiers and booleans. If an element is set to ``True`` it is displayed
and usable, if it is ``False`` it is displayed but disabled, if it is not present in the map, it is not displayed.

By passing an empty dictionary none of the elements are displayed. The identifying strings are as follows:

* **Drive** ``drive``
* **Gear** ``gear``
* **Throttle** ``throttle``
* **Direction** ``direction``

### Miscellaneous Controls

As with the different sections in the ``Main Controls Column`` the ``Miscellaneous Controls`` can be
enabled/disabled/non-display by specifying in the same dictionary, using the key ``misc``.

If the section is displayed it is configured by passing a list of ``MiscControlSpec`` to the ``misc_controls``
constructor parameter.

Each of these needs the following:

* ``display_name`` which is the name displayed in the user interface
* ``on_update`` which is the function that is called when the user interacts with the element
* ``param_type`` specifies the ``type`` of input expected; i.e ``bool``, ``int`` etc.
* ``row`` specifies the row inside the *Misc. Controls* frame for which this element is displayed
* ``column`` specifies the column inside the *Misc. Controls* frame for which this element is displayed
* ``description`` is the description to be displayed in the GUI - defaults to ``None``