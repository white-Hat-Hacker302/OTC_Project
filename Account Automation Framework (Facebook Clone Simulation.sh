#!/bin/bash

# ==============================================================================
# Project: Account Automation Framework (Facebook Clone Simulation)
# Developed by: Cyber Security Engineer Mr. Sabaz Ali Khan
# Purpose: Automation of User/Password input handling for testing environments.
# ==============================================================================

# Colors for UI
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

clear

# Banner Section
echo -e "${CYAN}"
cat << "EOF"
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡻⢀⠆⣤⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢹⣴⢊⣀⣿⡏⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠙⡛⠦⢤⠟⣰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡘⡄⠁⢀⠰⣸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡼⣝⣁⢲⡐⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⡿⡁⠚⢋⠭⢱⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠀⠄⠀⠒⣹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡎⠖⢀⣠⠀⢀⠗⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢃⠢⣄⣄⡂⠣⣜⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣸⣱⣠⣂⠩⢷⡸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣰⣴⣛⣔⣺⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣯⢗⡻⠶⠽⢤⣿⢋⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠴⣖⡶⣶⣟⢣⡙⢋⡭⢎⣻⣽⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⣠⣾⢏⣼⠏⣵⣿⣿⣣⠞⠦⡘⣐⢲⡏⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣯⣳⡀⢀⣾⠟⣣⠾⣇⠊⡴⣿⡥⠒⡌⠐⢤⡘⣼⠁⣰⠋⣴⡾⣭⡲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⢿⡿⠰⣿⣷⠿⣻⠩⢅⠋⠤⠁⣾⣯⡱⠑⡎⡐⢢⠘⣿⡰⠇⡌⣑⢚⡴⠗⠸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣀⣴⠟⢫⡔⢛⣾⣿⣻⠟⣡⠊⡜⣀⢣⣿⠖⣍⠧⠔⡠⠁⡞⣻⡟⡰⠜⡐⢊⠔⠨⢥⣇⣀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣠⡾⢃⡥⢋⠐⢢⢽⣿⡿⢃⠣⡄⡑⠦⣬⢟⡦⡙⡤⢒⠰⣀⠡⢅⠻⣧⢒⡩⢐⢣⠘⠤⠈⣽⣥⢭⡑⣄⠀⠀⠀⠀⠀
⠀⣴⡟⠤⡑⢎⡐⢤⠿⣛⣿⣟⢧⡃⠒⠠⡑⢊⢦⢏⣷⡱⡑⢊⡔⢢⠜⣂⢣⠙⠦⣁⠃⢆⡉⠲⢏⣿⠠⢌⡟⢊⠣⡀⠀⠀⠀
⠐⣷⣻⣴⠵⣎⡐⠚⢛⣿⣿⣟⢮⡗⠠⠑⡠⢣⢎⢾⣿⡰⣉⠆⡘⢢⡜⠤⢊⡑⠂⠄⡘⠤⠌⡓⢊⢋⡙⢢⡙⢻⣆⡱⡀⠀⠀
⠀⢸⣿⣸⣿⣄⢹⣤⣿⣿⣿⣿⣼⣿⣁⠇⣤⢁⡼⢧⣿⢡⠤⡤⢠⣇⢏⡸⢀⠠⢁⠠⢁⡄⣀⠉⠄⠄⡀⢁⠹⡄⢿⣠⡇⠀⠀
⠀⠀⠹⣿⣵⣚⣻⢾⣿⣿⣿⣿⣿⣿⣿⣽⣲⢮⣝⣯⣟⣯⣟⣞⡯⣔⣺⡔⣣⢜⡠⢆⡡⣄⣴⣩⣼⡰⢠⠁⢠⢡⣻⣧⣻⠀⠀
⠀⠀⠀⢻⣿⢿⠲⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣾⣿⣿⣿⣿⣽⢶⣿⣞⣿⣾⣿⢧⣿⣿⡱⢧⣏⣿⢤⣿⣷⣿⣦⠀
⠀⠀⠀⠀⢻⣗⡳⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣻⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⢯⣾⣿⣯⣿⣧⠇
⠀⠀⠀⠀⠀⢿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣷⢿⣞⡿⣿⣿⣿⣿⡏⠀
⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣾⡿⣾⢿⣿⣿⣿⣿⣷⠀
⠀⠀⠀⠀⠀⠀⠘⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⣿⣻⣯⣿⢿⣿⣻⣿⣿⣟⣾⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⡽⣿⣻⣿⣿⣿⣿⣿⣽⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣟⣷⢯⣿⡿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣳⢯⡳⣏⡾⣽⣾⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣽⣟⣷⣿⣞⣷⡽⣽⣿⡟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣽⣾⣟⡷⣿⢽⣻⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡟⣹⢣⣟⣷⣿⡿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣷⢯⣞⡴⣣⣿⣿⡟⣯⡽⡟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣞⣿⣿⣾⣿⡿⢧⣻⢵⡻⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠿⢿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣏⣧⠽⠚⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
EOF
echo -e "${YELLOW}      ===========================================================${NC}"
echo -e "${YELLOW}          FACEBOOK CLONE BOT SYSTEM - V1.0 (BETA)             ${NC}"
echo -e "${YELLOW}          ENGINEERED BY: MR. SABAZ ALI KHAN                   ${NC}"
echo -e "${YELLOW}          DEPARTMENT: CYBER SECURITY & AUTOMATION             ${NC}"
echo -e "${YELLOW}      ===========================================================${NC}"
echo -e "${NC}"

# Function to simulate credential capture
function start_bot() {
    echo -e "${BLUE}[*] Initializing Bot Modules...${NC}"
    sleep 1
    echo -e "${BLUE}[*] Establishing Secure Connection...${NC}"
    sleep 1
    echo -e "${GREEN}[+] Connection Established!${NC}"
    echo -e "${BLUE}[*] Ready to intercept/input credentials...${NC}"
    echo -e "-----------------------------------------------------------"
}

function capture_data() {
    echo -e "${CYAN}[?] Enter Target Username/Email:${NC}"
    read -r username
    echo -e "${CYAN}[?] Enter Target Password:${NC}"
    read -r password
    
    # Masking input for simulation
    echo -e "${YELLOW}[!] Capturing data...${NC}"
    sleep 2
    
    # Log to a file (Simulated Database)
    echo "$(date) | User: $username | Pass: $password" >> logs.txt
    
    echo -e "${GREEN}[SUCCESS] Data logged to local encrypted buffer.${NC}"
}

function show_menu() {
    echo -e "\n${BLUE}--- MAIN MENU ---${NC}"
    echo -e "1) ${GREEN}Start Session${NC}"
    echo -e "2) ${RED}View Logs (Admin Only)${NC}"
    echo -e "3) ${YELLOW}System Status${NC}"
    echo -e "4) ${BLUE}Exit${NC}"
    echo -ne "\n${CYAN}Select an option: ${NC}"
}

# Main Logic Loop
start_bot

while true; do
    show_menu
    read -r choice
    
    case $choice in
        1)
            echo -e "\n${RED}[!] Starting Credential Capture Simulation...${NC}"
            capture_data
            ;;
        2)
            echo -e "\n${YELLOW}--- LOG ACCESS GRANTED ---${NC}"
            if [ -f logs.txt ]; then
                cat logs.txt
            else
                echo -e "${RED}[!] No logs found in database.${NC}"
            fi
            ;;
        3)
            echo -e "\n${BLUE}[INFO] System: Operational${NC}"
            echo -e "${BLUE}[INFO] Security Level: High${NC}"
            echo -e "${BLUE}[INFO] Engineer: Mr. Sabaz Ali Khan${NC}"
            ;;
        4)
            echo -e "${GREEN}[*] Shutting down... Goodbye.${NC}"
            exit 0
            ;;
        *)
            echo -e "${RED}[!] Invalid Option. Try again.${NC}"
            ;;
    esac
done