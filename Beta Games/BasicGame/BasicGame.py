from PicoBoySDK import PicoBoySDK, PlayerObject

# Initialize the PicoBoySDK object
game = PicoBoySDK("BasicGame")

# Load a sprite for the player
player_sprite = game.Load_Sprite("/BasicGame/player.sprt", 16, 16)

# Initialize the player object
player = PlayerObject(game, 60, 60, 16, 16, player_sprite, 2)

# Main game loop
while True:
    # Fill the screen with black
    game.Fill_Screen((0, 0, 0))

    # Check for player movement
    player.Update()

    # Draw a boundary box
    game.Outline_Rect(0, 0, 120, 120, (255, 255, 255))

    # Render a simple obstacle
    game.Fill_Rect(50, 50, 20, 20, (255, 0, 0))

    # Check for collision with the obstacle
    collision = game.Check_Collision(
        player.x, player.y, player.width, player.height,
        50, 50, 20, 20, 0, 1
    )
    if collision:
        game.Create_Text("Collision!", -1, -1, (255, 255, 0))

    # Update the game screen
    game.Update()
