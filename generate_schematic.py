import resource
import os
import sys

# Configure environment variables for KiCad 8 symbol libraries.
# This ensures SKiDL can locate the schematic symbols on macOS.
os.environ['KICAD8_SYMBOL_DIR'] = '/Applications/KiCad/KiCad.app/Contents/SharedSupport/symbols'

# Ensure output files are generated in the script's directory.
script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir:
    os.chdir(script_dir)

# Add local node_modules/.bin to PATH so SKiDL can find netlistsvg
bin_dir = os.path.abspath(os.path.join(script_dir, '..', 'node_modules', '.bin'))
os.environ['PATH'] += os.pathsep + bin_dir

symbol_dir = "/Applications/KiCad/KiCad.app/Contents/SharedSupport/symbols"


os.environ["KICAD_SYMBOL_DIR"] = symbol_dir
os.environ["KICAD6_SYMBOL_DIR"] = symbol_dir
os.environ["KICAD7_SYMBOL_DIR"] = symbol_dir
os.environ["KICAD8_SYMBOL_DIR"] = symbol_dir

os.environ["KICAD_CONFIG_HOME"] = (
    os.path.expanduser("~/Library/Preferences/kicad/10.0")
)



print("KICAD_SYMBOL_DIR =", os.environ.get("KICAD_SYMBOL_DIR"))
print("KICAD6_SYMBOL_DIR =", os.environ.get("KICAD6_SYMBOL_DIR"))
print("KICAD7_SYMBOL_DIR =", os.environ.get("KICAD7_SYMBOL_DIR"))
print("KICAD8_SYMBOL_DIR =", os.environ.get("KICAD8_SYMBOL_DIR"))
print("KICAD_CONFIG_HOME =", os.environ.get("KICAD_CONFIG_HOME"))

try:
    from skidl import *
except ImportError:
    print("SKiDL library is not installed in the current environment.")
    print("Please install it using: pip install skidl")
    sys.exit(1)

# Set KiCad 8 as the default schematic design tool (matching installed version 8.0.1)
set_default_tool(KICAD8)

# Initialize a clean netlist/circuit
reset()

# --------------------------------------------------------------------
# Define your components and connections below:
# --------------------------------------------------------------------
rapid1 = Part(
    "Switch",
    "SW_Push",
    value="RAPID",
    footprint="RetroPad:Silicone_Membrane_Pad_11mm_(7.5mm)"
)

rapid1.ref = "RAPID1"

btn1 = Part(
    "Switch",
    "SW_Push",
    value="BTN1",
    footprint="RetroPad:Silicone_Membrane_Pad_11mm_(7.5mm)"
)

btn1.ref = "BTN1"

btn2 = Part(
    "Switch",
    "SW_Push",
    value="BTN2",
    footprint="RetroPad:Silicone_Membrane_Pad_11mm_(7.5mm)"
)

btn2.ref = "BTN2"

btn3 = Part(
    "Switch",
    "SW_Push",
    value="BTN3",
    footprint="RetroPad:Silicone_Membrane_Pad_11mm_(7.5mm)"
)

btn3.ref = "BTN3"

#not left most
u1 = Part(
    "MCU_Microchip_ATtiny",
    "ATtiny814-SS",
    value="ATtiny814-SS",
    footprint="Package_SO:SOIC-14_3.9x8.7mm_P1.27mm"
)

u1.ref = "U1"

c1 = Part(
    "Device",
    "C_Small",
    value="0.1uF",
    footprint="Capacitor_SMD:CP_Elec_4x4.5"
)

c1.ref = "C1"

r3 = Part(
    "Device",
    "R_US",
    value="330",
    footprint="Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder"
)

r3.ref = "R3"

r4 = Part(
    "Device",
    "R_US",
    value="1K",
    footprint="Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder"
)

r4.ref = "R4"

j2 = Part(
    "Connector_Generic",
    "Conn_01x06",
    value="UPDI",
    footprint="Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical"
)

j2.ref = "J2"

d1 = Part(
    "Device",
    "LED",
    value="RAPID",
    footprint="LED_THT:LED_D3.0mm"
)

d1.ref = "D1"

r1 = Part(
    "Device",
    "R_US",
    value="1K",
    footprint="Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder"
)

r1.ref = "R1"

r5 = Part(
    "Device",
    "R_US",
    value="1K",
    footprint="Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder"
)

r5.ref = "R5"

r2 = Part(
    "Device",
    "R_US",
    value="1K",
    footprint="Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder"
)

r2.ref = "R2"

r6 = Part(
    "Device",
    "R_US",
    value="1K",
    footprint="Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder"
)

r6.ref = "R6"
j1 = Part(
    "Connector_Generic",
    "Conn_01x09",
    value="DB9_Male",
    footprint="Connector_Dsub:DSUB-9_Pins_Vertical_P2.77x2.84mm"
)

j1.ref = "J1"

jump1 = Part(
    "Switch",
    "SW_Push",
    value="JUMP",
    footprint="RetroPad:Silicone_Membrane_Pad_11mm_(7.5mm)"
)

jump1.ref = "JUMP1"


up1 = Part(
    "Switch",
    "SW_Push",
    value="UP",
    footprint="RetroPad:Silicone_Membrane_Pad_11mm_(7.5mm)"
)

up1.ref = "UP1"

down1 = Part(
    "Switch",
    "SW_Push",
    value="DOWN",
    footprint="RetroPad:Silicone_Membrane_Pad_11mm_(7.5mm)"
)

down1.ref = "DOWN1"

left1 = Part(
    "Switch",
    "SW_Push",
    value="LEFT",
    footprint="RetroPad:Silicone_Membrane_Pad_11mm_(7.5mm)"
)

left1.ref = "LEFT1"

right1 = Part(
    "Switch",
    "SW_Push",
    value="RIGHT",
    footprint="RetroPad:Silicone_Membrane_Pad_11mm_(7.5mm)"
)

right1.ref = "RIGHT1"

r7 = Part(
    "Device",
    "R_US",
    value="0",
    footprint="Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder"
)

r7.ref = "R7"

r8 = Part(
    "Device",
    "R_US",
    value="0",
    footprint="Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder"
)

r8.ref = "R8"

r9 = Part(
    "Device",
    "R_US",
    value="0",
    footprint="Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder"
)

r9.ref = "R9"

r10 = Part(
    "Device",
    "R_US",
    value="0",
    footprint="Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder"
)

r10.ref = "R10"

r11 = Part(
    "Device",
    "R_US",
    value="0",
    footprint="Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder"
)

r11.ref = "R11"

h2 = Part(
    "Mechanical",
    "MountingHole_Pad",
    value="MountingHole",
    footprint="MountingHole:MountingHole_4mm_Pad_Via"
)

h2.ref = "H2"

h1 = Part(
    "Mechanical",
    "MountingHole_Pad",
    value="MountingHole",
    footprint="MountingHole:MountingHole_4mm_Pad_Via"
)

h1.ref = "H1"


#Net definitions


gnd_net= Net("GND")
rapid_net = Net("RAPID")
fire_net  = Net("FIRE")
btn2_net  = Net("BTN2")
btn3_net  = Net("BTN3")

# Common ground side of all buttons.
gnd_net += rapid1[1]
gnd_net += btn1[1]
gnd_net += btn2[1]
gnd_net += btn3[1]

rapid_net += rapid1[2]
fire_net  += btn1[2]
btn2_net  += btn2[2]
btn3_net  += btn3[2]

#U1's net

vcc_net  = Net("+5V")
reset_net = Net("RESET")
out_btn2_net = Net("OUT_BTN2")
out_btn3_net = Net("OUT_BTN3")
 #btn1_net=Net("BTN1")
vcc_net+= u1["VCC"]
gnd_net += u1["GND"]
out_btn3_net+=u1["PA5"]
out_btn2_net+=u1["PA6"]
rapid_net+=u1["PB0"]
fire_net+=u1["PB1"] #btn1_net+=u1["PB1"]
btn2_net+=u1["PB2"]
btn3_net+=u1["PB3"]
fire_net += u1["PA7"]
reset_net+=u1["~{RESET}/PA0"]

vcc_net+=c1["2"]
gnd_net+=c1["1"]
## doubt
vcc_net   += j2["Pin_4"]
reset_net += j2["Pin_5"]
gnd_net   += j2["Pin_6"]

fire_net += d1["A"]     # LED anode
gnd_net+=r3["1"]

d1_k_net = Net("D1_K")
d1_k_net+=d1["K"]
d1_k_net+=r3["2"]

fire_net+=r4["2"]
gnd_net+=r4["1"]

out_btn3_net+=r1["2"]

potx_net=Net("POTX")
potx_net+=r1["1"]
potx_net+=r5["2"]
gnd_net+=r5["1"]

poty_net=Net("POTY")
out_btn2_net+=r2["2"]
poty_net+=r2["1"]
gnd_net+=r6["1"]
poty_net+=r6["2"]

#right left 
right_net = Net("RIGHT")
left_net  = Net("LEFT")
down_net  = Net("DOWN")
up_net    = Net("UP")
poty_net  += j1["Pin_1"]
potx_net  += j1["Pin_2"]

right_net += j1["Pin_3"]

gnd_net   += j1["Pin_4"]

left_net  += j1["Pin_5"]

vcc_net   += j1["Pin_6"]

down_net  += j1["Pin_7"]

fire_net  += j1["Pin_8"]

up_net    += j1["Pin_9"]

gnd_net += r7["1"]
gnd_net += r8["1"]
gnd_net += r9["1"]
gnd_net += r10["1"]
gnd_net += r11["1"]
up_net += jump1["2"]
up_net += up1["2"]

down_net += down1["2"]
left_net += left1["2"]
right_net += right1["2"]



jump_gnd_net = Net("JUMP_GND")

jump_gnd_net += jump1["1"]
jump_gnd_net += r7["2"]

up_gnd_net = Net("UP_GND")

up_gnd_net += r8["2"]
up_gnd_net += up1["1"]
down_gnd_net = Net("DOWN_GND")

down_gnd_net += down1["1"]
down_gnd_net += r9["2"]
left_gnd_net = Net("LEFT_GND")

left_gnd_net += left1["1"]
left_gnd_net += r10["2"]

right_gnd_net = Net("RIGHT_GND")

right_gnd_net +=right1["1"]
right_gnd_net += r11["2"]

gnd_net += h1["1"]
gnd_net += h2["1"]

# Power flags.

pwr_flag_vcc = Part(
    "power",
    "PWR_FLAG",
    footprint="TestPoint:TestPoint_Pad_D1.0mm"
)

pwr_flag_gnd = Part(
    "power",
    "PWR_FLAG",
    footprint="TestPoint:TestPoint_Pad_D1.0mm"
)

vcc_net += pwr_flag_vcc["1"]
gnd_net += pwr_flag_gnd["1"]




unused_mcu = Net("UNUSED_MCU")
unused_mcu += u1["PA1"]
unused_mcu += u1["PA2"]
unused_mcu += u1["PA3"]
unused_mcu += u1["PA4"]

unused_updi = Net("UNUSED_UPDI")
unused_updi += j2["Pin_1"]
unused_updi += j2["Pin_2"]
unused_updi += j2["Pin_3"]



# --------------------------------------------------------------------
# Generate Schematic Netlists
# --------------------------------------------------------------------
print("Generating Netlist, XML, and SVG schematic representations...")
generate_netlist(file_='retropad.net')
generate_xml(file_='retropad.xml')
generate_svg(file_='retropad')
print(rapid1)
print(u1)
print(j1)
print("\nRunning ERC...\n")
ERC()
print("Rapid footprint:", rapid1.footprint)

print("Schematic generation code executed successfully!")


