from pybricks.hubs import PrimeHub
from pybricks.parameters import Button
from pybricks.tools import wait
import sys

# Initialize Hub
hub = PrimeHub()

def main():
    """Simple menu to run different programs"""
    
    option = 1  # Start with option 1
    
    while True:
        # Always show current option number
        hub.display.number(option)
        
        # Wait for button press
        pressed = hub.buttons.pressed()
        
        if Button.LEFT in pressed:
            # Previous option (1, 2, 3)
            option = option - 1 if option > 1 else 3
            wait(300)
            
        elif Button.RIGHT in pressed:
            # Next option (1, 2, 3)  
            option = option + 1 if option < 3 else 1
            wait(300)
            
        elif Button.CENTER in pressed:
            # Execute the program corresponding to current displayed number
            hub.display.char("R")  # R for Running
            wait(500)
            
            try:
                if option == 1:
                    # Run MoveForward
                    # Remove from cache if already imported
                    if 'MoveForward' in sys.modules:
                        del sys.modules['MoveForward']
                    import MoveForward
                    if hasattr(MoveForward, 'main'):
                        MoveForward.main()
                    hub.display.number(1)  # Show option 1 completed
                    
                elif option == 2:
                    # Run CheckColorTurn
                    # Remove from cache if already imported
                    if 'CheckColorTurn' in sys.modules:
                        del sys.modules['CheckColorTurn']
                    import CheckColorTurn
                    if hasattr(CheckColorTurn, 'main'):
                        CheckColorTurn.main()
                    hub.display.number(2)  # Show option 2 completed
                    
                elif option == 3:
                    # Exit
                    hub.display.char("E")  # E for Exit
                    wait(2000)
                    break
                    
                wait(2000)  # Show result for 2 seconds
                
            except ImportError:
                hub.display.char("F")  # F for File not found
                wait(3000)
            except Exception:
                hub.display.char("X")  # X for error
                wait(3000)
        
        wait(50)  # Small delay

if __name__ == "__main__":
    main()