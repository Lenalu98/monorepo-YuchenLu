**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 4

<hr>

**Use Case**: _Drawing on the Canvas_

**Primary Actor**: _User_

**Goal in Context**: _Allow the user to simulate drawing, enabling free drawing on the canvas by pressing and dragging the mouse._

**Preconditions**: _The program is running and ready to accept user input. The canvas is displayed on the graphical interface. The color is selected and ready for drawing_

**Trigger**: _User initiates a drawing action on the canvas by interacting with the mouse, by pressing the left mouse button_

**Scenario**: _User positions the mouse pointer over the canvas. User presses and holds down the left mouse button, signifying the start of the drawing action. The program detects the mouse button press and starts tracking mouse movement. As the user moves the mouse (drags), the program changes pixel colors on the canvas to simulate a pencil drawing. User releases the left mouse button, indicating the end of the drawing action._

**Exceptions**: _Mouse Input Error: Program fails to detect mouse input accurately, affecting the drawing experience. Remedy: Prompt the user to check mouse functionality or restart the program._
_Canvas Overload: Extensive drawing saturates the canvas or slows down the program. Remedy: Notify the user, suggesting canvas clearance or starting anew._
_Out of Canvas Bounds: User attempts to draw outside canvas boundaries. Remedy: Inform and prompt drawing within defined limits._

**Priority**: _High_

**When available**: _First release_

**Channel to actor**: _Mouse input, when left button of mouse is clicked and dragged_

**Secondary Actor**: _None_

**Channels to Secondary Actors**: _None_

**Open Issues**: _How can the program provide real-time feedback to the user during the drawing process? And what about undo/redo functions for users?_

<hr>

(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
