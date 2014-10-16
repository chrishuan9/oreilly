__author__ = 'chris'
"""
Starting with the project you created at the end of the last lesson,
add components to the existing framework so that:
-- When the areas occupied by  Frame 1 or Frame 2 are clicked
with mouse button 1, the program should print which frame was clicked
and the X and Y coordinates (relative to the Frame).
-- Frame 3 should contain an Entry and a Text widget. When the button now
labeled "Open" is clicked, the content of the Entry should be used as a file
name, and the content of the file (if any) displayed in the Text widget.
-- The Entry and Text widgets should completely fill Frame 3 and continue to
do so even as the application window is resize.
-- The color of the text displayed in Frame 3's Text widget should change
appropriately when the "Red," "Blue," "Green," or "Black" buttons are clicked.
 +---------------------+--------------------------------+
 |                     |                                |
 |                     |                                |
 |                     |                                |
 |      Frame 1        |                                |
 |                     |                                |
 |                     |                                |
 |                     |                                |
 +---------------------+               Frame 3          |
 |                     |                                |
 |                     |                                |
 |                     |                                |
 |     Frame 2         |                                |
 |                     |                                |
 |                     |                                |
 +----------+----------+----------+----------+----------+
 |    Red   |   Blue   |  Green   |  Black   |   Open   |
 +----------+----------+----------+----------+----------+
 """