; Set all positioning to absolute
G90  
; Set extruder to relative
M83
; **** Replicator 1 dual start.gcode ****
; Set progress to 0%
M73 P0 ; enable build progress
G162 X Y F3000 ; home XY maximum
G161 Z F1200 ; home Z minimum
G92 Z-5 ; set Z to -5
G1 Z0 ; move Z to 0
G161 Z F100 ; home Z slowly
; Active auto leveling?
M132 X Y Z A B ; recall home offsets
; Select extruder T0
M135 T0 ; load right extruder offsets
; move to 10, 10
G1 X0 Y0 Z10 F9000 
; wait 1 minute
G4 P60000
