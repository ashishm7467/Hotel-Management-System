# Hotel Management System — Project Statement

## 1. Problem Statement

Managing room availability, guest bookings, and stay charges requires accurate records. When these details are handled manually, staff may have difficulty identifying available rooms, keeping track of a booking, or preparing the final bill. This project provides a simple Python-based system to organize these basic hotel operations through a menu-driven command-line program.

## 2. Scope of the Project

The system supports basic front-desk tasks for a small hotel with a predefined set of rooms. A user can view available rooms and room information, create a booking by entering guest and stay details, choose optional food and extra-bed services, review booking details, generate a bill, and check out a guest.

Room information and booking records are maintained in Python dictionaries while the program is running. The current project is limited to a single terminal session and does not include permanent data storage, reservations across specific dates, online booking, payment processing, staff accounts, or a graphical interface.

## 3. Target Users

- **Hotel reception staff:** For demonstrating or managing basic room booking and checkout tasks.
- **Students:** For learning Python functions, dictionaries, loops, conditionals, and user input through a practical example.
- **Project evaluators and instructors:** For reviewing a small, menu-driven hotel management application.

## 4. High-Level Features

- **Room availability:** Lists rooms currently marked as available.
- **Room details:** Displays room type, listed occupancy, rates, amenities, complimentary items, and extra-bed charges.
- **Guest check-in and booking:** Collects guest information and stay length, assigns an available room, and updates its status.
- **Optional services:** Adds food and extra-bed charges when selected and available.
- **Guest and booking lookup:** Displays booking information using a room number.
- **Bill generation:** Shows room, food, and extra-bed charges with the total amount.
- **Checkout:** Displays the final bill and, after confirmation, removes the in-memory booking and marks the room available again.
