from dooGL import *

init_window(800, 600)

running = True
while running:
    running = magic()  # Handles events like mouse & keyboard input

    # Enable scaling grid
    #scale(spacing=100, show_numbers=False, text_color=(1, 0, 0), font=None)

    # 1. Default text (Yellow text on dark green background)
    text(position=(150, 450), text="Default Text", text_color=(1.0, 1.0, 0), background_color=(0, 0.25, 0), size=(200, 50))

    # 2. Rotated red text with blue background
    text(position=(150, 200), text="Rotated Text", text_color=(1.0, 0.0, 0), background_color=(0, 0.0, 0), size=(250, 50), rotation=45)

    # 3. Green text with larger font and pink background
    text(position=(150, 0), text="Green Text", text_color=(0.0, 1.0, 0), background_color=(1.0, 0.0, 1), size=(300, 60))


    # 7. Red outlined text with no background
    text(position=(450, 50), text="Outlined Red Text", text_color=(1.0, 0.0, 0), background_color=(0, 0, 0), size=(300, 60))

    # 8. Custom size text with black background
    text(position=(400, 500), text="Custom Size Text", text_color=(1.0, 0.0, 1.0), background_color=(0.0, 0.0, 0), size=(350, 75))

    # 9. Transparent background with green text
    text(position=(500, 210), text="Transparent Background", text_color=(0.0, 1.0, 0), background_color=(0, 0, 0, 0), size=(300, 60))

    # 10. Black text with no background and small font
    text(position=(600, 300), text="Simple Text", text_color=(0.0, 1.0, 0), background_color=(0, 0, 0), size=(100, 40))

    
    end()  # Refresh the screen
