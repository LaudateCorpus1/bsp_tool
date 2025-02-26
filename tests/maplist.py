import os
from typing import Dict, List, Tuple


DirList = Dict[str, List[str]]
# ^ {"Game": ["maps_dir"]}

GameDirList = Dict[str, DirList]
# ^ {"SteamFolder": {**DirList_1, **DirList_2}}
# ^ {"External/Backup": {**DirList_1, **DirList_2}}

goldsrc_dirs: DirList  # GoldSrc titles
source_dirs: DirList  # Source Engine titles
extracted_dirs: DirList  # .bsps from archives (.007, .hfs, .iwd, .ff, .pak, .pk3, .pkg, .sin, .vpk) & non-steam games
sourcemod_dirs: DirList  # Source SDK games @ Steam/steamapps/sourcemods
every_bsp_dir: DirList  # all of the above in one dict (used with external HDD)
group_dirs: GameDirList  # groups folders to install dirs (steam installs, external HDDs etc.)
installed_games: Dict[Tuple[str], List[str]]
# ^ {("SteamFolder", "Game"): ["maps_dir"]}


# TODO: generate by searching for gameinfo.txt files
goldsrc_dirs = {
        "Cry of Fear": ["cryoffear/maps"],  # 235 maps | 1.9 GB | Cry of Fear
        **{f"Half-Life/{mod}": ["maps"] for mod in [
                        "blue_shift",    # 37 maps | 54 MB | Half-Life: Blue Shift
                        "cstrike",   # 25 maps | 81 MB | Counter-Strike
                        "czero",     # 22 maps | 83 MB | Counter-Strike: Condition Zero
                        "czeror",    # 73 maps | 177 MB | Counter-Strike: Condition Zero - Deleted Scenes
                        "dmc",       # 7 maps | 9 MB | Deathmatch: Classic
                        "dod",       # 22 maps | 91 MB | Day of Defeat
                        "gearbox",   # 68 maps | 137 MB | Half-Life: Opposing Force
                        # https://www.moddb.com/mods/natural-selection
                        "ns",        # 27 maps | 124 MB | Natural Selection
                        "ricochet",  # 3 maps | 2 MB | Ricochet
                        "tfc",       # 15 maps | 41 MB | Team Fortress: Classic
                        "valve"]},   # 115 maps | 188 MB | Half-Life
        "Halfquake Trilogy": ["valve/maps"],  # 152 maps | 207 MB
        "Sven Co-op": ["svencoop/maps",  # 107 maps | 521 MB
                       # "svencoop_addon/maps",  # 0 maps | 0 MB
                       # "svencoop_downloads/maps",  # 0 maps | 0 MB
                       "svencoop_event_april/maps"]}  # 4 maps | 31 MB
# ^ {"game_dir": ["map_dir"]}

# TODO: generate by searching for gameinfo.txt files
source_dirs = {
         "Alien Swarm": ["swarm/maps"],  # 9 maps | 299 MB
         "Alien Swarm Reactive Drop": ["reactivedrop/maps"],  # 53 maps | 1.3 GB
         "Blade Symphony": ["berimbau/maps"],  # 21 maps | 1.0 GB
         "Counter-Strike Global Offensive": ["csgo/maps"],  # 38 maps | 5.9 GB
         "counter-strike source": ["cstrike/maps",  # 20 maps | 237 MB
                                   # "cstrike/download/maps"
                                   ],
         "day of defeat source": ["dod/maps"],  # 9 maps | 299 MB
         "Double Action": ["dab/maps"],  # 10 maps | 255 MB
         "Fistful of Frags": ["fof/maps"],  # 39 maps | 1.68 GB
         "Fortress Forever": ["FortressForever/maps"],  # 22 maps | 618 MB
         "G String": ["gstringv2/maps"],  # 76 maps | 2.49 GB | Seriously Impressive
         "GarrysMod": ["garrysmod/maps"],  # 2 maps | 84 MB
         "Half-Life 1 Source Deathmatch": ["hl1mp/maps"],  # 11 maps | 53 MB
         **{f"half-life 2/{mod}": ["maps"] for mod in [
                         "ep2",          # HL2:EP2 |  22 maps | 703 MB
                         "episodic",     # HL2:EP1 |  20 maps | 554 MB
                         "hl1",          # HL:S    | 110 maps | 339 MB
                         "hl2",          # HL2     |  80 maps | 815 MB
                         "lostcoast"]},  # HL2:LC  |   4 maps | 101 MB
         "half-life 2 deathmatch": ["hl2mp/maps"],  # 8 maps | 72 MB
         "Half-Life 2 Update": ["hl2/maps"],  # 76 maps | 2.9 GB
         "left 4 dead": ["left4dead/maps",   # 45 maps | 975 maps
                         "left4dead_dlc3/maps"],  # 3 maps | 67 MB
         "Left 4 Dead 2": ["left4dead2/maps",  # 8 maps | 186 MB
                           "left4dead2_dlc1/maps",  # 3 maps | 60 MB
                           "left4dead2_dlc2/maps",  # 8 maps | 186 MB
                           "left4dead2_dlc3/maps"],  # 21 maps | 481 MB
         "MINERVA": ["metastasis/maps"],  # 6 maps | 201 MB
         "NEOTOKYO": ["neotokyosource/maps"],  # 24 maps | 303 MB
         "nmrih": ["nmrih/maps"],  # 31 maps | 1.1 GB
         "Portal": ["portal/maps"],  # 26 maps | 426 MB
         "Portal 2": ["portal2/maps",  # 106 maps | 2.7 GB
                      "portal2_dlc1/maps",  # 10 maps | 313 MB
                      "portal2_dlc2/maps"],  # 1 map | 687 KB
         "Portal Reloaded": ["portalreloaded/maps"],  # 12 maps | 448 MB
         "SourceFilmmaker": ["game/tf/maps"],  # 71 maps | 3.3 GB
         "Synergy": ["synergy/maps"],  # 21 maps | 407 MB
         "Team Fortress 2": ["tf/maps",  # 194 maps | 5.2 GB
                             "tf/download/maps"],  # 187 maps | 2.6 GB
         "Transmissions Element 120": ["te120/maps"],  # 5 maps | 281 MB
         "Vampire The Masquerade - Bloodlines": ["Vampire/maps"]}  # 101 maps | 430 MB
# ^ {"game_dir": ["map_dir"]}

# TODO: workshop_dirs

extracted_dirs = {
        # IdTechBsp
        "Anachronox": ["maps",  # 98 maps | 377 MB | .dat
                       "anox1.zip/maps"],  # 3 maps | 4 MB | .zip
        "Daikatana": ["pak2/maps"],  # 83 maps | 291 MB | .pak
        "HereticII": ["Htic2-0.pak/maps"],  # 29 maps | 77 MB | .pak
        "Hexen2": ["pak0/maps",  # 4 maps | 6 MB | .pak
                   "pak1/maps"],  # 38 maps | 47 MB | .pak
        "RTCW": ["mp_pak0.pk3/maps",  # 8 maps | 89 MB | .pk3
                 "mp_pakmaps0.pk3/maps",  # 1 map | 8 MB | .pk3
                 "mp_pakmaps1.pk3/maps",  # 1 map | 11 MB | .pk3
                 "mp_pakmaps2.pk3/maps",  # 1 map | 10 MB | .pk3
                 "mp_pakmaps3.pk3/maps",  # 1 map | 14 MB | .pk3
                 "mp_pakmaps4.pk3/maps",  # 1 map | 16 MB | .pk3
                 "mp_pakmaps5.pk3/maps",  # 1 map | 12 MB | .pk3
                 "mp_pakmaps6.pk3/maps",  # 1 map | 11 MB | .pk3
                 "pak0.pk3/maps",  # 32 maps | 234 MB | .pk3
                 "sp_pak4.pk3/maps",  # 3 maps | 24 MB | .pk3
                 # https://www.moddb.com/mods/realrtcw-realism-mod
                 # https://store.steampowered.com/app/1379630/RealRTCW/
                 "realRTCW/maps"],  # 11 maps | 85 MB
        "SiN": ["maps",  # 65 maps | 170 MB | .sin (.pak) | SiN: Gold
                "download/maps"],  # 45 maps | 64 MB | .sin (.pak) | SiN mods
        "SoF": ["pak0/maps"],  # 32 maps | 131 MB | .pak
        "SoF2": ["maps.pk3/maps",  # 48 maps | 409 MB | .pk3
                 "mp.pk3/maps",  # 10 maps | 63 MB | .pk3
                 "update101.pk3/maps",  # 4 maps | 22 MB | .pk3
                 "update102.pk3/maps",  # 5 maps | 51 MB | .pk3
                 "update103.pk3/maps"],  # 4 maps | 31 MB | .pk3
        "StarTrekEliteForce": ["pak0/maps",  # 67 maps | 334 MB | .pak
                               "pak1/maps",  # 4 maps | 20 MB | .pak
                               "pak3/maps"],  # 22 maps | 107 MB | .pak
        "Quake": ["Id1/pak0/maps",  # 21 maps | 10 MB | .pak
                  "Id1/pak1/maps",  # 30 maps | 31 MB | .pak
                  "hipnotic/pak0/maps",  # 18 maps | 30 MB | .pak
                  "rogue/pak0/maps"],  # 23 maps | 28 MB | .pak
        # includes BSP2:
        "Quake/rerelease": ["id1/pak0/maps",  # 55 maps | 49 MB | .pak
                            "id1/pak0/maps/test",  # 14 maps | 1 MB | .pak
                            "dopa/pak0/maps",  # 13 maps | 25 MB | .pak
                            "hipnotic/pak0/maps",  # 18 maps | 30 MB
                            "mg1/pak0/maps",  # 20 maps | 240 MB | .pak
                            "rogue/pak0/maps"],  # 23 maps | 28 MB | .pak
        # http://quake.great-site.net/
        "Alkaline": ["alkaline/pak0/maps",  # 23 maps | 132 MB | .pak
                     "alk1.1/pak0/maps",  # 27 maps | 188 MB | .pak
                     "alkaline_dk/maps"],  # 13 maps | 792 KB | .zip
        # TODO: Quake Arcane Dimensions (https://www.moddb.com/mods/arcane-dimensions/downloads)
        "QuakeII": ["pak0/maps",  # 39 maps | 89 MB | .pak
                    "pak1/maps"],  # 8 maps | 10 MB | .pak
        "QuakeIII": ["maps"],  # 31 maps | 116 MB | .pk3
        # TODO: Quake Champions .pak (Saber3D)
        "QuakeLive": ["pak00/maps"],  # 149 maps | 764 MB | .pk3
        "Warsow": ["maps"],  # 38 maps | 463 MB | .pk3
        # https://www.splashdamage.com/games/wolfenstein-enemy-territory/
        "WolfET": ["pak0.pk3/maps",  # 6 maps | 86 MB | .pk
                   # https://www.moddb.com/mods/et/downloads/etsp
                   "singleplayer/maps",  # 32 maps | 288 MB | .pk3
                   # steamapps\workshop\content\1379630\2600685791 (realRTCW workshop)
                   "realRTCW_singleplayer/maps"],  # 2 maps | 31 MB | .pk3
        # InfinityWardBsp
        "CoD1": ["maps",  # 33 maps | 488 MB | .pk3
                 "maps/MP"],  # 16 maps | 229 MB | .pk3
        "CoD2": ["maps",  # 39 maps | 1.5 GB | .iwd | .d3dbsp
                 "maps/mp"],  # 15 maps | 395 MB | .iwd  | .d3dbsp
        # D3DBsp
        # TODO: Extract CoD4 maps from .ff archives
        # https://wiki.zeroy.com/index.php?title=Call_of_Duty_4:_FastFile_Format
        # https://github.com/Scobalula/Greyhound
        # https://github.com/ZoneTool/zonetool
        # https://github.com/promod/CoD4-Mod-Tools
        # "CoD4": ["devraw/maps",  # 1 map | 17 MB | .d3dbsp  (v17 InfinityWardBsp; not a CoD4 .d3dbsp?)
        "CoD4": ["maps",  # 3 maps | 7 MB | .d3dbsp
                 "maps/mp"],  # 1 map | 4 MB | .d3dbsp
        # GoldSrcBsp
        # https://www.moddb.com/games/james-bond-007-nightfire/downloads/alura-zoe
        "Nightfire": ["ROOT/maps"],  # 53 maps | 405 MB | .007
        # ValveBsp
        "BlackMesa": ["maps"],  # 109 maps | 5.5 GB | .vpk
        "CSMalvinas": ["maps"],  # 1 map | 13 MB | Counter-Strike: Malvinas
        # https://github.com/L-Leite/UnCSO2
        "CSO2": ["maps"],  # 97 maps | 902 MB | Counter-Strike: Online 2 | .pkg
        "DarkMessiah/singleplayer": ["maps"],  # 35 maps | 1.4 GB | .vpk
        "DarkMessiah/multiplayer": ["maps"],  # 11 maps | 564 MB | .vpk
        "Infra": ["maps"],  # 49 maps | 5.5 GB | .vpk
        "TacticalIntervention": ["maps"],  # 26 maps | 3.5 GB | Tactical Intervention
        # https://www.moddb.com/mods/team-fortress/downloads
        "TeamFortressQuake": ["tf25rel/maps",  # 1 map | 1.88 MB | v2.5
                              "tf28/FORTRESS/maps",  # 1 map | 1.88 MB
                              "tfbot080/MAPS"],  # 1 map | 212 KB
        # https://github.com/yretenai/HFSExtract
        "Vindictus": ["maps"],  # 474 maps | 8.1 GB | .hfs
        # RespawnBsp (NOTE: .bsp_lump & .ent sizes not counted)
        "Titanfall": ["maps",  # 26 maps | 6.6 GB | .vpk
                      "depot/r1dev/game/r1/maps",  # 16 maps | 4.2 GB | .vpk
                      "depot/r1pcgold/game/r1/maps",  # 1 map | 1.7 GB | .vpk
                      "depot/r1pcstaging/game/r1/maps",  # 23 maps | 5.8 GB | .vpk
                      "depot/r1pcstaging/game/r1_dlc1/maps"],  # 3 maps | 796 MB | .vpk
        # donated by p0358
        "TitanfallOnline": ["maps",  # 17 maps | 2.0 GB | .pkg
                            "v2905-dated-2017-04-08/maps",  # 13 maps | 1.3 GB | .7z
                            "v4050-datarevision-17228-dated-2017-08-17/maps"],  # 13 maps | 1.3 GB | .7z
        "Titanfall2": ["maps",  # 36 maps | 12.4 GB | .vpk
                       "depot/r2dlc3/game/r2/maps",  # 5 maps | 1.1 GB | .vpk
                       "depot/r2dlc4/game/r2/maps",  # 5 maps | 1.1 GB | .vpk
                       "depot/r2dlc5/game/r2/maps",  # 5 maps | 1.1 GB | .vpk
                       "depot/r2dlc6/game/r2/maps",  # 5 maps | 1.1 GB | .vpk
                       "depot/r2dlc7/game/r2/maps",  # 5 maps | 1.1 GB | .vpk
                       "depot/r2dlc8/game/r2/maps",  # 5 maps | 1.1 GB | .vpk
                       "depot/r2dlc9/game/r2/maps",  # 5 maps | 1.1 GB | .vpk
                       "depot/r2dlc10/game/r2/maps",  # 5 maps | 1.1 GB | .vpk
                       "depot/r2dlc11/game/r2/maps",  # 5 maps | 1.1 GB | .vpk
                       "depot/r2pcprecert/game/r2/maps",  # 4 maps | 1.1 GB | .vpk
                       "depot/r2staging/game/r2/maps"],  # 5 maps | 1.1 GB | .vpk
        # Thanks to https://apexlegends.fandom.com/wiki/Version_History
        # see also: https://github.com/Syampuuh/TitanfallApexLegends
        # TODO: reduce list to smallest possible set with bsp_tool.extensions.diff
        # -- could eventually create an archive of all map related patches
        "ApexLegends": ["maps",  # 9 maps | 3.3 GB | .vpk
                        # season1:  Wild Frontier [19th Mar 2019]
                        # season2:  Battle Charge [2nd Jul 2019]
                        "season2/maps",  # 1 map | 16.9 MB | .vpk
                        # season3:  Meltdown - patch 5  [1st Oct 2019]
                        "season3_30oct19/maps",  # 8 maps | 4.9 GB | .vpk
                        "season3_30oct19/depot/r5launch/game/r2/maps",  # 8 maps | 4.9 GB | .vpk
                        "season3_30oct19/depot/r5staging/game/r2/maps",  # 6 maps | 3.2 GB | .vpk
                        "season3_3dec19/maps",  # 8 maps | 4.6 GB | .vpk
                        "season3_3dec19/depot/r5launch/game/r2/maps",  # 8 maps | 4.6 GB | .vpk
                        "season3_3dec19/depot/r5staging/game/r2/maps",  # 8 maps | 3.0 GB | .vpk
                        # season4:  Assimilation [4th Feb 2020]
                        "season4/depot/r5launch/game/r2/maps",  # 8 maps | 4.6 GB | .vpk
                        "season4/depot/r5staging/game/r2/maps",  # 6 maps | 3.0 GB | .vpk
                        "season4/maps",  # 8 maps | 4.6 GB | .vpk
                        # season5:  Fortune's Favour  [12th May 2020]
                        "season5/maps",  # 3 maps | 1.2 GB | .vpk
                        # season6:  Boosted  [18th Aug 2020]
                        # season7:  Ascension  [4th Nov 2020]
                        # season8:  Mayhem  [2nd Feb 2021]
                        "season8/maps",  # 1 map | 1.9 MB | .vpk
                        # season9:  Legacy  [4th May 2021]
                        "season9/maps",  # 4 maps | 226 MB | .vpk
                        # season10:  Emergence  [3rd Aug 2021]
                        "season10_3aug21/maps",  # 2 maps | 813 MB | .vpk
                        "season10_10aug21/maps",  # 8 maps | 2.8 GB | .vpk
                        "season10_10aug21/depot/r5-100/game/r2/maps",  # 8 maps | 2.8 GB | .vpk
                        "season10_14sep21/maps",  # 2 maps | 962 MB | .vpk
                        "season10_14sep21/depot/r5-100/game/r2/maps",  # 1 map | 797 MB | .vpk
                        "season10_14sep21/depot/r5-101/game/r2/maps",  # 2 maps | 949 MB | .vpk
                        # season11:  Escape  [2nd Nov 2021]
                        "season11/maps",  # 1 map | 10 MB | .vpk
                        "season11/depot/r5-110/game/r2/maps",  # 1 map | 9 MB | .vpk
                        "season11_6nov21/maps",  # 1 map | 760 MB | .vpk
                        "season11_6nov21/depot/r5-110/game/r2/maps",  # 1 map | 749 MB | .vpk
                        "season11_19nov21/maps",  # 10 maps | 1.5 GB | .vpk
                        "season11_19nov21/depot/r5-110/game/r2/maps",  # 8 maps | 2.1 GB | .vpk
                        "season11_19nov21/depot/r5-111/game/r2/maps",  # 10 maps | 1.4 GB | .vpk
                        # Nintendo Switch versions
                        "switch_season9/depot/r5-90/game/r2/maps",  # 7 maps | 2.3 GB | .vpk
                        "switch_season9/maps"],  # 7 maps | 2.4 GB | .vpk
        # RitualBsp
        "FAKK2": ["maps",  # 30 maps | 150 MB | .pk3
                  "download/maps"],  # 6 maps | 25 MB | .pk3
        "Alice": ["maps",  # 42 maps | 196 MB | .pk3
                  "download/maps"],  # 1 map | 61 KB | .pk3
        "MoHAA": ["maps",  # 37 maps | 293 MB | .pk3
                  "maps/briefing",  # 6 maps | 319 KB | .pk3
                  "maps/DM",  # 7 maps | 48 MB | .pk3
                  "maps/obj"],  # 4 maps | 36 MB | .pk3
        "StarTrekEliteForceII": ["download/maps",  # 188 maps | 886 MB | .pk3
                                 "maps"],  # 88 maps | 607 MB | .pk3
        "StarWarsJediKnight": ["assets0.pk3/maps",  # 34 maps | 348 MB | .pk3
                               "assets0.pk3/maps/mp",  # 23 maps | 154 MB | .pk3
                               "assets3.pk3/maps/mp"],  # 4 maps | 32 MB | .pk3
        "StarWarsJediKnightII": ["maps"]}  # 45 maps | 361 MB | .pk3
# ^ {"game_dir": ["map_dir"]}

# https://geshl2.com
# https://www.moddb.com/mods/riot-act
# https://www.moddb.com/mods/map-labs
# TODO: https://openfortress.fun, https://prefortress.ml & https://tf2classic.com  (all currently unavailable)
sourcemod_dirs = {mod: ["maps"] for mod in [
                      "gesource",  # 26 maps | 775 MB | GoldenEye: Source
                      "half-life 2 riot act",  # 5 maps | 159 MB | HL2: Riot Act
                      # Run Think Shoot Live
                      "TFTS",  # 3 maps | 8 MB | Tales from the Source
                      # Map Labs
                      "episodeone",  # 15 maps | 268 MB | Map Labs 2 + Test Tube 15
                      "RunThinkShootLiveVille2",  # 19 maps | 728 MB | Map Labs 3
                      "cromulentville2",  # 21 maps | 342 MB | Test Tube 7
                      "companionpiece2",  # 18 maps | 429 MB | Map Labs 8
                      "eyecandy",   # 41 maps | 652 MB | Test Tube 8
                      "backontrack",  # 32 maps | 787 MB | Map Labs 9
                      "tworooms",  # 39 maps | 496 MB | Test Tube 9
                      "fusionville2",  # 21 maps | 391 MB | Map Labs 10
                      "tunetwo",  # 12 maps | 114 MB | Test Tube 13
                      "lvl2",  # 14 maps | 461 MB | Map Labs 15
                      "thewrapuptwo",  # 27 maps | 226 MB | Test Tube 15
                      "halloweenhorror4",  # 25 maps | 274 MB | Map Labs 16
                      "halflifeeternal"]}  # 13 maps | 123 MB | Test Tube 16

# every_bsp_dir = {**sourcemod_dirs, **extracted_dirs, **goldsrc_dirs, **source_dirs}

# NOTE: ls $group_dir+$game_dir+$maps_dir
group_dirs = {"C:/Program Files (x86)/Steam/steamapps/sourcemods": sourcemod_dirs,
              "D:/SteamLibrary/steamapps/common": {**goldsrc_dirs, **source_dirs},
              "E:/Mod": extracted_dirs,  # Id Software, Respawn Entertainment, Nexon & More
              # "F:/bsps": every_bsp_dir,
              # "/media/bikkie/GAMES/bsps": every_bsp_dir
              }

# NOTE: registering test maps
installed_games = {("./", "tests/maps"): ["Call of Duty 4", "Call of Duty 4/mp",
                                          "Quake 3 Arena",
                                          "Team Fortress 2"]}
for group, games in group_dirs.items():
    if os.path.exists(group):
        for game, map_dirs in games.items():
            if os.path.exists(os.path.join(group, game)):
                installed_games[(group, game)] = map_dirs
