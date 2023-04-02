Delta V, is a 2d puzzle game based upon orbital mechanics. Players will navigate through space by adjusting their spacecraft's velocity, using gravity assists from celestial bodies to conserve fuel. The game will feature a variety of challenging levels, each with unique objectives and obstacles, such as asteroid fields and black holes. The game will also include a level editor, allowing players to create and share their own custom levels with the community.

// Main Menu
enum class MainMenu {
  StartGame,
  Settings,
  Credits,
  Quit
};

// Start Game Sub Menu
enum class StartGameMenu {
  NewGame,
  Continue,
  SelectLevel,
  BackToMainMenu
};

// Settings Sub Menu
enum class SettingsMenu {
  Audio,
  Controls,
  BackToMainMenu
};

// Credits Sub Menu
enum class CreditsMenu {
  ViewCredits,
  BackToMainMenu
};

