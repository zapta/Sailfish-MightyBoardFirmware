# platforms.py -- build settings for each "standard" firmware build.
#
#   Individuals can extend the list of known platforms by supplying
#   the file ~/.sailfish_platforms.py containing additional entries
#   for the platforms{} dictionary.  In the following example, an
#   entry is defined for a platform named "franken-board"
#
#     % cat ~/.sailfish_platforms.py
#     platforms['franken-board'] = {
#         'mcu' : 'atmega2560',
#         'programmer' : 'stk500v2',
#         'board_directory' : 'mighty_one',
#         'defines' : [ 'CORE_XY', 'BUILD_STATS', 'ALTERNATE_UART',
#                       'HEATERS_ON_STEROIDS', 'MAX31855',
#                       '__DELAY_BACKWARD_COMPATIBLE__',
#                       '__PROG_TYPES_COMPAT__' ]
#     }
#
#  It can then be built with the simple command
#
#     % scons platform=franken-board
#
#  which would be largely equivalent to
#
#     % scons platform=mighty_one-2560 core_xy=1 heaters_on_steroids=1 \
#          alt_uart=1 max31855=1
#
#  It misses setting -DBUILD_STATS since there is no command line option
#  to select that.

from os.path import expanduser, isfile

platforms = {

# This is a dictionary of platform names to build.
# Each platform to build is itself a dictionary containing build settings.
# The settings are
#
#   mcu        -- Processor name (e.g., atmega1280)
#   programmer -- avrdude programmer type (e.g., stk500v1)
#   board_directory -- Name of the motherboard specific board directory to
#                      use under firmware/src/MightyBoard/Motherboard/boards/
#                      (e.g., mighty_one)
#   defines    -- List of #defines to establish.  Any string prefixed with '-'
#                 will be removed from the list of #defines to establish.
#	 PLATFORM_THE_REPLICATOR_STR -- The "Replicator" string
#        PLATFORM_MACHINE_ID         -- Machine ID
#        PLATFORM_TOOLHEAD_OFFSET_X  -- X distance between toolheads
#        PLATFORM_SPLASH1_MSG        -- First line of the splash message
#                                       *** MAKE SURE THIS IS EXACTLY 20 ***
#                                       *** CHARACTERS IN LENGTH         ***
#	 PLATFORM_ENDSTOP_INVERT     -- bitmask for endstop inversion (0bN--BAZYX,
#                                       N means all endstop inverted)
#        PLATFORM_HOME_DIRECTION     -- bitmask for home direction (0b---BAZYX),
#                                       AB max - to never halt on edge in stepper
#                                       interface.
#        PLATFORM_AXIS_INVERT        -- bitmask for axis inversion (0b---BAZYX)
#        PLATFORM_AXIS_OFFSETS       -- distance delta between toolheads and the
#                                       ideal 'center' of the toolhead system, in
#                                       steps.
#        PLATFORM_AXIS_LENGTHS       -- maximum lengths of all axis (X/Y/Z/A/B)
#        PLATFORM_AXIS_STEPS_PER_MM  -- steps per mm for all axis (X/Y/Z/A/B),
#                                       all values multiplied by 1,000,000.
#   squeeze    -- Source files to compile --mcall-prologues so as to save
#                 code space.

    'mighty_one' :
        { 'mcu' : 'atmega1280',
          'programmer' : 'stk500v1',
          'board_directory' : 'mighty_one',
          'squeeze' : [ 'Menu.cc', 'Interface.cc', 'InterfaceBoard.cc',
                        'LiquidCrystalSerial.cc', 'DigiPots.cc',
                        'Eeprom.cc', 'EepromMap.cc', 'Piezo.cc',
                        'UtilityScripts.cc', 'RGB_LED.cc',
                        'StandardButtonArray.cc',
  '[ os.path.basename(f) for f in glob.glob(\'../../src/MightyBoard/Motherboard/boards/mighty_one/*.cc\') ]' ],
          'defines' : [ 'HAS_RGB_LED', 'EEPROM_MENU_ENABLE',
                        'PLATFORM_SPLASH1_MSG=\\\"Sailfish Replicator1\\\"' ]
          },

    'mighty_one-corexy' :
        { 'mcu' : 'atmega1280',
          'programmer' : 'stk500v1',
          'board_directory' : 'mighty_one',
          'squeeze' : [ 'Menu.cc', 'Interface.cc', 'InterfaceBoard.cc',
                        'LiquidCrystalSerial.cc', 'DigiPots.cc',
                        'Eeprom.cc', 'EepromMap.cc', 'Piezo.cc',
                        'UtilityScripts.cc',
  '[ os.path.basename(f) for f in glob.glob(\'../../src/MightyBoard/Motherboard/lib_sd/*.c\') ]',
  '[ os.path.basename(f) for f in glob.glob(\'../../src/MightyBoard/Motherboard/boards/mighty_one/*.cc\') ]' ],
          'defines' : [ 'CORE_XY', 'HEATERS_ON_STEROIDS', 'BUILD_STATS',
                        'COOLING_FAN_PWM', 'HAS_RGB_LED', 'EEPROM_MENU_ENABLE',
                        'PLATFORM_SPLASH1_MSG=\\\"Sailfish Rep1 CoreXY\\\"' ]
        },

    'mighty_one-2560' :
        { 'mcu' : 'atmega2560',
          'programmer' : 'stk500v2',
          'board_directory' : 'mighty_one',
          'defines' : [ 'BUILD_STATS', 'ALTERNATE_UART', 'AUTO_LEVEL',
                        'PSTOP_ZMIN_LEVEL', 'HAS_RGB_LED',
                        'PLATFORM_SPLASH1_MSG=\\\"Sailfish Replicator1\\\"',
                        'EEPROM_MENU_ENABLE', 'RGB_LED_MENU' ]
        },

    'mighty_one-2560-corexy' :
        { 'mcu' : 'atmega2560',
          'programmer' : 'stk500v2',
          'board_directory' : 'mighty_one',
          'defines' : [ 'CORE_XY', 'BUILD_STATS', 'ALTERNATE_UART',
                        'HEATERS_ON_STEROIDS', 'AUTO_LEVEL', 'HAS_RGB_LED',
                        'PSTOP_ZMIN_LEVEL', 'COOLING_FAN_PWM',
                        'PLATFORM_SPLASH1_MSG=\\\"Sailfish Rep1 CoreXY\\\"',
                        'EEPROM_MENU_ENABLE', 'RGB_LED_MENU' ]
        },

    'mighty_one-2560-clone-r1' :
        { 'mcu' : 'atmega2560',
          'programmer' : 'stk500v2',
          'board_directory' : 'mighty_one',
          'defines' : [ 'CORE_XY', 'BUILD_STATS', 'ALTERNATE_UART',
                        'HEATERS_ON_STEROIDS', 'AUTO_LEVEL', 'HAS_RGB_LED',
                        'PSTOP_ZMIN_LEVEL', 'COOLING_FAN_PWM',
                        'PLATFORM_SPLASH1_MSG=\\\" Sailfish Clone R1 \\\"',
                        'PLATFORM_THE_REPLICATOR_STR=\\\"CloneR1\\\"',
                        'PLATFORM_AXIS_OFFSETS={14444L, 1444L, 8667L, 8667L}',
                        'PLATFORM_AXIS_LENGTHS={300L, 195L, 210L, 100000L, 100000L}',
                        'PLATFORM_AXIS_STEPS_PER_MM={88888889, 88888889, 400000000, 96275202, 96275202}',
                        'EEPROM_MENU_ENABLE', 'CLONE_R1', 'RGB_LED_MENU' ]
        },

    'mighty_one-2560-max31855-corexy' :
        { 'mcu' : 'atmega2560',
          'programmer' : 'stk500v2',
          'board_directory' : 'mighty_one',
          'defines' : [ 'CORE_XY', 'BUILD_STATS', 'ALTERNATE_UART',
                        'HAS_RGB_LED', 'HEATERS_ON_STEROIDS', 'AUTO_LEVEL',
                        'MAX31855', 'PSTOP_ZMIN_LEVEL', 'COOLING_FAN_PWM',
                        'PLATFORM_SPLASH1_MSG=\\\"Sailfish Rep1 CoreXY\\\"',
                        'EEPROM_MENU_ENABLE', 'RGB_LED_MENU' ]
        },

    'mighty_one-2560-max31855' :
        { 'mcu' : 'atmega2560',
          'programmer' : 'stk500v2',
          'board_directory' : 'mighty_one',
          'defines' : [ 'BUILD_STATS', 'ALTERNATE_UART', 'MAX31855',
                        'AUTO_LEVEL', 'PSTOP_ZMIN_LEVEL', 'HAS_RGB_LED',
                        'PLATFORM_SPLASH1_MSG=\\\"Sailfish Replicator1\\\"',
                        'EEPROM_MENU_ENABLE', 'RGB_LED_MENU' ]
        },

    'mighty_two' :
        { 'mcu' : 'atmega1280',
          'programmer' : 'stk500v1',
          'board_directory' : 'mighty_two',
          'defines' : [ 'SINGLE_EXTRUDER', 'BUILD_STATS', 'HAS_RGB_LED',
                        'PLATFORM_SPLASH1_MSG=\\\"Sailfish Replicator2\\\"',
                        'PLATFORM_TOOLHEAD_OFFSET_X=35.0',
                        'PLATFORM_THE_REPLICATOR_STR=\\\"Replicator 2\\\"',
                        'PLATFORM_MACHINE_ID=0xB015',
                        'PLATFORM_AXIS_OFFSETS={13463L, 13463L, 6643L, 6377L}',
                        'PLATFORM_AXIS_LENGTHS={285L, 152L, 155L, 100000L, 100000L}',
                        'PLATFORM_AXIS_STEPS_PER_MM={88573186, 88573186, 400000000, 96275202, 96275202}',
                        'EEPROM_MENU_ENABLE' ],
          'squeeze' : [ 'Menu.cc', 'Interface.cc', 'InterfaceBoard.cc',
                        'LiquidCrystalSerial.cc', 'DigiPots.cc',
                        'Eeprom.cc', 'EepromMap.cc', 'Piezo.cc',
                        'UtilityScripts.cc', 'TemperatureTable.cc',
                        'Thermistor.cc', 'Thermocouple.cc', 'Heater.cc',
                        'CoolingFan.cc', 'PID.cc',
  '[ os.path.basename(f) for f in glob.glob(\'../../src/MightyBoard/Motherboard/lib_sd/*.c\') ]',
  '[ os.path.basename(f) for f in glob.glob(\'../../src/MightyBoard/Motherboard/boards/mighty_two/*.cc\') ]' ]
        },

    'mighty_two-corexy' :
        { 'mcu' : 'atmega1280',
          'programmer' : 'stk500v1',
          'board_directory' : 'mighty_two',
          'defines' : [ 'CORE_XY', 'SINGLE_EXTRUDER', 'BUILD_STATS', 'HAS_RGB_LED',
                        'PLATFORM_SPLASH1_MSG=\\\"Sailfish Rep2 CoreXY\\\"',
                        'PLATFORM_TOOLHEAD_OFFSET_X=35.0',
                        'PLATFORM_THE_REPLICATOR_STR=\\\"Replicator 2\\\"',
                        'PLATFORM_MACHINE_ID=0xB015',
                        'PLATFORM_AXIS_OFFSETS={13463L, 13463L, 6643L, 6377L}',
                        'PLATFORM_AXIS_LENGTHS={285L, 152L, 155L, 100000L, 100000L}',
                        'PLATFORM_AXIS_STEPS_PER_MM={88573186, 88573186, 400000000, 96275202, 96275202}',
                        'EEPROM_MENU_ENABLE' ],
          'squeeze' : [ 'Menu.cc', 'Interface.cc', 'InterfaceBoard.cc',
                        'LiquidCrystalSerial.cc', 'DigiPots.cc',
                        'Eeprom.cc', 'EepromMap.cc', 'Piezo.cc',
                        'UtilityScripts.cc', 'TemperatureTable.cc',
                        'Thermistor.cc', 'Thermocouple.cc', 'Heater.cc',
                        'CoolingFan.cc', 'PID.cc',
  '[ os.path.basename(f) for f in glob.glob(\'../../src/MightyBoard/Motherboard/lib_sd/*.c\') ]',
  '[ os.path.basename(f) for f in glob.glob(\'../../src/MightyBoard/Motherboard/boards/mighty_two/*.cc\') ]' ]
        },

    'mighty_two-2560' :
        { 'mcu' : 'atmega2560',
          'programmer' : 'stk500v2',
          'board_directory' : 'mighty_two',
          'defines' : [ 'SINGLE_EXTRUDER', 'BUILD_STATS', 'ALTERNATE_UART',
                        'PLATFORM_SPLASH1_MSG=\\\"Sailfish Replicator2\\\"',
                        'PLATFORM_TOOLHEAD_OFFSET_X=35.0',
                        'PLATFORM_THE_REPLICATOR_STR=\\\"Replicator 2\\\"',
                        'PLATFORM_MACHINE_ID=0xB015',
                        'PLATFORM_AXIS_OFFSETS={13463L, 13463L, 6643L, 6377L}',
                        'PLATFORM_AXIS_LENGTHS={285L, 152L, 155L, 100000L, 100000L}',
                        'PLATFORM_AXIS_STEPS_PER_MM={88573186, 88573186, 400000000, 96275202, 96275202}',
                        'AUTO_LEVEL', 'PSTOP_ZMIN_LEVEL', 'HAS_RGB_LED',
                        'EEPROM_MENU_ENABLE', 'RGB_LED_MENU' ]
        },

    'mighty_twox' :
        { 'mcu' : 'atmega1280',
          'programmer' : 'stk500v1',
          'board_directory' : 'mighty_two',
          'squeeze' : [ 'Menu.cc', 'Interface.cc', 'InterfaceBoard.cc',
                        'LiquidCrystalSerial.cc', 'DigiPots.cc',
                        'Eeprom.cc', 'EepromMap.cc', 'Piezo.cc',
                        'UtilityScripts.cc', 'TemperatureTable.cc',
                        'Thermistor.cc', 'Thermocouple.cc', 'Heater.cc',
                        'CoolingFan.cc', 'PID.cc',
  '[ os.path.basename(f) for f in glob.glob(\'../../src/MightyBoard/Motherboard/boards/mighty_two/*.cc\') ]' ],
          'defines' : [ 'BUILD_STATS', 'HAS_RGB_LED',
                        'PLATFORM_SPLASH1_MSG=\\\"  Sailfish Rep 2X   \\\"',
                        'PLATFORM_TOOLHEAD_OFFSET_X=35.0',
                        'PLATFORM_THE_REPLICATOR_STR=\\\"Replicator 2X\\\"',
                        'PLATFORM_MACHINE_ID=0xB017',
                        'PLATFORM_AXIS_OFFSETS={13463L, 13463L, 6643L, 6377L}',
                        'PLATFORM_AXIS_LENGHTS={246L, 152L, 155L, 100000L, 100000L}',
                        'PLATFORM_AXIS_STEPS_PER_MM={88573186, 88573186, 400000000, 96275202, 96275202}',
                        'EEPROM_MENU_ENABLE' ]
        },

    'mighty_twox-2560' :
        { 'mcu' : 'atmega2560',
          'programmer' : 'stk500v2',
          'board_directory' : 'mighty_two',
          'defines' : [ 'BUILD_STATS', 'ALTERNATE_UART', 'AUTO_LEVEL',
                        'PSTOP_ZMIN_LEVEL', 'HAS_RGB_LED',
                        'PLATFORM_SPLASH1_MSG=\\\"  Sailfish Rep 2X   \\\"',
                        'PLATFORM_TOOLHEAD_OFFSET_X=35.0',
                        'PLATFORM_THE_REPLICATOR_STR=\\\"Replicator 2X\\\"',
                        'PLATFORM_MACHINE_ID=0xB017',
                        'PLATFORM_AXIS_OFFSETS={13463L, 13463L, 6643L, 6377L}',
                        'PLATFORM_AXIS_STEPS_PER_MM={88573186, 88573186, 400000000, 96275202, 96275202}',
                        'EEPROM_MENU_ENABLE', 'RGB_LED_MENU' ]
        },

    'ff_creator' :
        { 'mcu' : 'atmega1280',
          'programmer' : 'stk500v1',
          'board_directory' : 'mighty_one',
          'squeeze' : [ 'Menu.cc', 'Interface.cc', 'InterfaceBoard.cc',
                        'LiquidCrystalSerial.cc', 'DigiPots.cc',
                        'Eeprom.cc', 'EepromMap.cc', 'Piezo.cc',
                        'UtilityScripts.cc' ],
          'defines' : [ 'FF_CREATOR', 'HEATERS_ON_STEROIDS', 'HAS_RGB_LED',
                        'PLATFORM_SPLASH1_MSG=\\\"Sailfish FF Creator \\\"',
                        'PLATFORM_TOOLHEAD_OFFSET_X=34.0',
                        'PLATFORM_THE_REPLICATOR_STR=\\\"FF Creator\\\"',
                        'EEPROM_MENU_ENABLE' ]
        },

    'ff_creator-2560' :
        { 'mcu' : 'atmega2560', 
          'programmer' : 'stk500v2',
          'board_directory' : 'mighty_one',
          'defines' : [ 'FF_CREATOR', 'BUILD_STATS', 'ALTERNATE_UART',
                        'PLATFORM_SPLASH1_MSG=\\\"Sailfish FF Creator \\\"',
                        'PLATFORM_TOOLHEAD_OFFSET_X=34.0',
                        'PLATFORM_THE_REPLICATOR_STR=\\\"FF Creator\\\"',
                        'HEATERS_ON_STEROIDS', 'AUTO_LEVEL',
                        'PSTOP_ZMIN_LEVEL', 'HAS_RGB_LED', 'RGB_LED_MENU',
                        'EEPROM_MENU_ENABLE' ]
        },

    'ff_creatorx-2560' :
        { 'mcu' : 'atmega2560',
          'programmer' : 'stk500v2',
          'board_directory' : 'mighty_one',
          'defines' : [ 'BUILD_STATS', 'ALTERNATE_UART', 'FF_CREATOR_X',
                        'PLATFORM_SPLASH1_MSG=\\\"Sailfish FF CreatorX\\\"',
                        'PLATFORM_TOOLHEAD_OFFSET_X=34.0',
                        'PLATFORM_THE_REPLICATOR_STR=\\\"Creator X / Pro\\\"',
                        'HEATERS_ON_STEROIDS', 'AUTO_LEVEL',
                        'PSTOP_ZMIN_LEVEL', 'HAS_RGB_LED', 'RGB_LED_MENU',
                        'EEPROM_MENU_ENABLE' ]
        },

    'wanhao_dup4' :
        { 'mcu' : 'atmega1280',
          'programmer' : 'stk500v1',
          'board_directory' : 'mighty_one',
          'squeeze' : [ 'Menu.cc', 'Interface.cc', 'InterfaceBoard.cc',
                        'LiquidCrystalSerial.cc','DigiPots.cc',
                        'Eeprom.cc', 'EepromMap.cc', 'Piezo.cc',
                        'UtilityScripts.cc' ],
          'defines' : [ 'WANHAO_DUP4', 'HEATERS_ON_STEROIDS',
                        'PLATFORM_SPLASH1_MSG=\\\"Sailfish Wanhao Dup4\\\"',
                        'PLATFORM_THE_REPLICATOR_STR=\\\"Wanhao Duplicator\\\"',
                        'PLATFORM_AXIS_OFFSETS={13763L, 13763L, 6919L, 6919L}',
                        'HAS_RGB_LED', 'EEPROM_MENU_ENABLE' ]
        },

    'zyyx-1280' :
        { 'mcu' : 'atmega1280',
          'programmer' : 'stk500v1',
          'board_directory' : 'mighty_one',
          'squeeze' : [ 'Menu.cc', 'Interface.cc', 'InterfaceBoard.cc',
                        'LiquidCrystalSerial.cc','DigiPots.cc',
                        'Eeprom.cc', 'EepromMap.cc', 'Piezo.cc',
                        'UtilityScripts.cc' ],
          'defines' : [ 'SINGLE_EXTRUDER', 'ZYYX_3D_PRINTER',
                        'PLATFORM_SPLASH1_MSG=\\\" Sailfish ZYYX 3DP  \\\"',
                        'PLATFORM_THE_REPLICATOR_STR=\\\"ZYYX 3D Printer\\\"',
                        'PLATFORM_AXIS_OFFSETS={11957L, 11957L, 10186L, 10186L}',
                        'PLATFORM_AXIS_LENGTHS={270L, 230L, 195L, 100000L, 100000L}',
                        'PLATFORM_AXIS_STEPS_PER_MM={88573186, 88573186, 400000000, 96275202, 96275202}',
                        'AUTO_LEVEL', 'AUTO_LEVEL_ZYYX', 'PSTOP_ZMIN_LEVEL' ]
        },

    'zyyx-2560' :
        { 'mcu' : 'atmega2560',
          'programmer' : 'stk500v2',
          'board_directory' : 'mighty_one',
          'defines' : [ 'EEPROM_MENU_ENABLE', 'BUILD_STATS', 'SINGLE_EXTRUDER',
                        'ALTERNATE_UART', 'ZYYX_3D_PRINTER',
                        'PLATFORM_SPLASH1_MSG=\\\" Sailfish ZYYX 3DP  \\\"',
                        'PLATFORM_THE_REPLICATOR_STR=\\\"ZYYX 3D Printer\\\"',
                        'PLATFORM_AXIS_OFFSETS={11957L, 11957L, 10186L, 10186L}',
                        'PLATFORM_AXIS_LENGTHS={270L, 230L, 195L, 100000L, 100000L}',
                        'PLATFORM_AXIS_STEPS_PER_MM={88573186, 88573186, 400000000, 96275202, 96275202}',
                        'HEATERS_ON_STEROIDS', 'AUTO_LEVEL', 'AUTO_LEVEL_ZYYX',
                        'PSTOP_ZMIN_LEVEL', 'ZYYX_LEVEL_SCRIPT' ]
        },

    'zyyx-dual-2560' :
        { 'mcu' : 'atmega2560',
          'programmer' : 'stk500v2',
          'board_directory' : 'mighty_one',
          'defines' : [ 'EEPROM_MENU_ENABLE', 'BUILD_STATS',
                        'ALTERNATE_UART', 'ZYYX_3D_PRINTER',
                        'PLATFORM_SPLASH1_MSG=\\\" Sailfish ZYYX 3DP  \\\"',
                        'PLATFORM_THE_REPLICATOR_STR=\\\"ZYYX 3D Printer\\\"',
                        'PLATFORM_AXIS_OFFSETS={11957L, 11957L, 10186L, 10186L}',
                        'PLATFORM_AXIS_LENGTHS={270L, 230L, 195L, 100000L, 100000L}',
                        'PLATFORM_AXIS_STEPS_PER_MM={88573186, 88573186, 400000000, 96275202, 96275202}',
                        'HEATERS_ON_STEROIDS', 'AUTO_LEVEL', 'AUTO_LEVEL_ZYYX',
                        'PSTOP_ZMIN_LEVEL', 'ZYYX_LEVEL_SCRIPT' ]
        },

    'azteeg-x3-xymax' :
        { 'mcu' : 'atmega2560',
          'programmer' : 'stk500v2',
          'board_directory' : 'azteeg_x3',
          'defines' : [ 'BUILD_STATS', 'HEATERS_ON_STEROIDS',
                        'PLATFORM_SPLASH1_MSG=\\\"Sailfish Azteeg XYmx\\\"',
                        'PLATFORM_THE_REPLICATOR_STR=\\\"Azteeg X3\\\"',
                        'PLATFORM_AXIS_OFFSETS={14309L, 14309L, 7060L, 6778L}',
                        'AUTO_LEVEL', 'PSTOP_ZMIN_LEVEL', 'COOLING_FAN_PWM',
                        'EEPROM_MENU_ENABLE', 'HAS_RGB_LED', 'RGB_LED_MENU' ]
        },

    'azteeg-x3-xymax-corexy' :
        { 'mcu' : 'atmega2560',
          'programmer' : 'stk500v2',
          'board_directory' : 'azteeg_x3',
          'defines' : [ 'CORE_XY', 'BUILD_STATS', 'HEATERS_ON_STEROIDS',
                        'PLATFORM_SPLASH1_MSG=\\\"Sailfish Azteeg XYmx\\\"',
                        'PLATFORM_THE_REPLICATOR_STR=\\\"Azteeg X3\\\"',
                        'PLATFORM_AXIS_OFFSETS={14309L, 14309L, 7060L, 6778L}',
                        'AUTO_LEVEL', 'PSTOP_ZMIN_LEVEL', 'COOLING_FAN_PWM',
                        'EEPROM_MENU_ENABLE', 'HAS_RGB_LED', 'RGB_LED_MENU' ]
        },

    'azteeg-x3-xymin' :
        { 'mcu' : 'atmega2560',
          'programmer' : 'stk500v2',
          'board_directory' : 'azteeg_x3',
          'defines' : [ 'BUILD_STATS', 'HEATERS_ON_STEROIDS', 'XY_MIN_HOMING',
                        'PLATFORM_SPLASH1_MSG=\\\"Sailfish Azteeg XYmn\\\"',
                        'PLATFORM_THE_REPLICATOR_STR=\\\"Azteeg X3\\\"',
                        'PLATFORM_AXIS_OFFSETS={14309L, 14309L, 7060L, 6778L}',
                        'AUTO_LEVEL', 'PSTOP_ZMIN_LEVEL', 'COOLING_FAN_PWM',
                        'EEPROM_MENU_ENABLE', 'HAS_RGB_LED', 'RGB_LED_MENU' ]
        },

    'azteeg-x3-xymin-corexy' :
        { 'mcu' : 'atmega2560',
          'programmer' : 'stk500v2',
          'board_directory' : 'azteeg_x3',
          'defines' : [ 'CORE_XY', 'BUILD_STATS', 'HEATERS_ON_STEROIDS',
                        'PLATFORM_SPLASH1_MSG=\\\"Sailfish Azteeg XYmn\\\"',
                        'PLATFORM_THE_REPLICATOR_STR=\\\"Azteeg X3\\\"',
                        'PLATFORM_AXIS_OFFSETS={0L, 0L, 0L, 0L}',
                        'AUTO_LEVEL', 'PSTOP_ZMIN_LEVEL', 'COOLING_FAN_PWM',
                        'EEPROM_MENU_ENABLE', 'HAS_RGB_LED', 'RGB_LED_MENU',
                        'XY_MIN_HOMING' ]
        },
}

# Load data from ~/.sailfish_platforms.py

tmp_dict = { 'platforms' : {} }
home = expanduser('~')
if home[-1] != '/':
    home += '/'
site_file = home + '.sailfish_platforms.py'

if isfile(site_file):
    with open(site_file) as f:
        exec(f.read(), tmp_dict)

    if 'platforms' in tmp_dict:
        tmp_platforms = tmp_dict['platforms']
        for key in tmp_platforms:
            platforms[key] = tmp_platforms[key]

if __name__ == '__main__':
    list = ''
    for key in platforms:
        list += key + ' '
    print list[:-1]
