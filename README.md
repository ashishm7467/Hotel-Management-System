# Hotel Management System

## Introduction

The Hotel Management System is a Python program for managing rooms and guest bookings at VIT's Paradise hotel. It runs in a terminal and uses a menu to perform different tasks.

## Rooms

The program has six rooms:

- Rooms 101 and 102: Single rooms
- Room 103: Double room
- Rooms 201 and 202: Deluxe rooms
- Room 301: Suite

Each room has its own price, occupancy, food charge, facilities, and complimentary items. Some rooms also have an extra bed available for an additional charge.

## Main Menu

1. **Available Rooms** - Shows rooms that are marked as available.
2. **Room Details** - Shows details and prices for all rooms.
3. **Book Room** - Takes guest and booking details and books an available room.
4. **Guest Details** - Finds booking details using a room number.
5. **Booked Rooms** - Shows the first booked room it finds and the guest name.
6. **Generate Bill** - Shows room, food, and extra bed charges.
7. **Check-out** - Completes checkout and makes the room available again after confirmation.
8. **Exit** - Shows a thank-you message.

## Booking and Bill

During booking, the program asks for the number of people, guest details, room number, number of nights, and food and extra bed choices. It allows up to three people in a room. The bill includes the room charge and any selected food or extra bed charge.

## How to Run

1. Save the Python code in a file named `hotel.py`.
2. Open a terminal in the folder where the file is saved.
3. Type `python hotel.py` and press Enter.
4. Choose an option from the menu.

## Note

Room and booking information is stored only while the program is running. It is not saved after the program is closed.
