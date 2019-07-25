#main menu materials

brunch = "Resources/graphics/Main_Mune_buttom/Brunch35172.png"

exit_Button_Down = "Resources/graphics/Main_Mune_buttom/Exit_Selected10060.png"
exit_Button_Up = "Resources/graphics/Main_Mune_buttom/Exit_Unelected10060.png"

option_Button_Down = "Resources/graphics/Main_Mune_buttom/option_Selected10060.png"
option_Button_Up = "Resources/graphics/Main_Mune_buttom/option_Unselected10060.png"

play_Button_Down = "Resources/graphics/Main_Mune_buttom/Play_selected14050.png"
play_Button_Up = "Resources/graphics/Main_Mune_buttom/Play_Unselected14050.png"

train_Anime = "Resources/graphics/Start_Main_Bg0.5.png"
main_Menu_Logo = "Resources/graphics/Main_Menu_Logo_0.35.png"
dancing_Penguin = "Resources/graphics/tiaowu410205.png"

main_Menu_BGM = "Resources/music/mainMenu.mp3"


#Gaming UI materials

start_Button_Up = 'Resources/graphics/Game_UI/Roll_Unselected_0.65.png'
start_Button_Down = 'Resources/graphics/Game_UI/Roll_Selected_0.65.png'

setting_Button_Up = 'Resources/graphics/Game_UI/Setting_Unselected_0.65.png'
setting_Button_Down = 'Resources/graphics/Game_UI/Setting_Selected_0.65.png'

blank_Background = "Resources/graphics/bg1280720.png"
gaming_Map = "Resources/graphics/Game_UI/Game_UI_v2_720p.png"
gaming_UI_Logo = "Resources/graphics/title400.jpg"

player_Profile = "Resources/graphics/player150200.PNG"
player_Anime1 = "Resources/graphics/player_syn.anime2_12864.png"
player_Anime2 = "Resources/graphics/player_syn.anime4_25664.png"

gaming_UI_BGM = "Resources/music/inGame.mp3"

Dice_Anime = "Resources/graphics/Dice/dice_1to6_correct_600x100.png"
chalk_Font = "Resources/fonts/Chalkduster.ttf"  

station_Description_File_PATH = "Resources/files/mappppp.csv"
station_Description_File = open(station_Description_File_PATH,encoding='utf-8')
station_Description_File.readline()

block_Index = []
station_Name = []
station_Description = []


for line in station_Description_File:
	items = line.strip().split(',')
	block_Index.append(int(items[0]))
	station_Name.append(items[1])

	i = 2
	try: 
		station_Description.append(items[2])
	except:
		station_Description.append("Surprise~~~")


	print(items[1])



