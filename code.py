try:    
    import psutil   
except ModuleNotFoundError: 
    print("Psutil is not installed. "   
          + "Miner will try to automatically install it "   
          + "If it fails, please manually execute " 
          + "python3 -m pip install psutil")    
    install("psutil")
#yes
try:
    from pypresence import Presence
except ModuleNotFoundError:
    print("Pypresence is not installed. "
          + "Miner will try to automatically install it "
          + "If it fails, please manually execute "
          + "python3 -m pip install pypresence")
    install("pypresence")


   if float(Settings.VER) < float(data["tag_name"]): # If is outdated
            update = input(Style.BRIGHT + get_string("new_version"))
            if update.lower() == "y" or update == "":
                pretty_print(get_string("updating"), "warning", "sys0")

                DATA_DIR = "Duino-Coin PC Miner " + str(data["tag_name"]) # Create new version config folder
                if not Path(DATA_DIR).is_dir():
                    mkdir(DATA_DIR)
#nice
