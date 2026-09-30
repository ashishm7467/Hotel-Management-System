# Hotel Management System

A command-line hotel management project written in Python. It helps a hotel operator view rooms, record a booking, look up guest information, calculate a bill, and complete checkout.

## Features

- Show rooms that are currently available.
- View room types, occupancy, rates, amenities, complimentary items, and extra-bed charges.
- Book a room and record guest and check-in information.
- Add optional food and extra-bed charges to a booking.
- View guest details and booked rooms.
- Generate an itemized bill.
- Check out a guest and make the room available again.

## Technologies and tools

- Python 3
- Python standard library only
- Terminal or command prompt

## Room inventory

| Room number(s) | Type | Listed occupancy | Rate/night | Food/day | Extra bed/night |
|---|---|---:|---:|---:|---:|
| 101, 102 | Single | 1 | ₹2,000 | ₹500 | ₹700 |
| 103 | Double | 2 | ₹3,000 | ₹700 | ₹800 |
| 201, 202 | Deluxe | 2 | ₹4,500 | ₹900 | ₹1,000 |
| 301 | Suite | 2 | ₹7,000 | ₹1,200 | Not available |

## Installation and run

1. Install Python 3 if it is not already installed.
2. Save the supplied program as `hotel_management.py`.
3. Open a terminal in the folder containing the file.
4. Run:

   ```bash
   python hotel_management.py
   ```

   On Windows, this command may also be used:

   ```powershell
   py hotel_management.py
   ```

5. Choose an operation by entering its number in the menu. Select **8. Exit** when finished.

No package installation is required.

## Testing instructions

Run the program and try these manual checks:

1. Choose **1** and confirm that available rooms are listed.
2. Choose **2** and confirm that room details are displayed.
3. Choose **3**, enter guest information, select an available room, enter a positive number of nights, and try the food and extra-bed choices.
4. Choose **1** again and confirm the booked room is no longer shown as available.
5. Use **4**, **5**, and **6** with the booked room number to view guest information, booked-room information, and the bill.
6. Choose **7**, confirm checkout, and choose **1** to check that the room is available again.

The program keeps its data in memory, so restart it to return to the original room inventory. Use sample details during demonstrations; the program is not designed to protect real guest personal or identity information.

## Screenshots


<img width="567" height="425" alt="Screenshot 2026-09-30 201839" src="https://github.com/user-attachments/assets/0d21374b-8e61-4e45-a59e-8a6148705636" />
<img width="584" height="334" alt="Screenshot 2026-09-30 203319" src="https://github.com/user-attachments/assets/3dd30500-58bd-4fad-b9fe-536f5043b149" />
<img width="491" height="409" alt="Screenshot 2026-09-30 203345" src="https://github.com/user-attachments/assets/f02be2d4-50ee-444e-86c7-81530451239b" />
<img width="472" height="232" alt="Screenshot 2026-09-30 203405" src="https://github.com/user-attachments/assets/204322f9-3152-4f94-af7e-4f2c2c71913c" />
<img width="469" height="523" alt="Screenshot 2026-09-30 203428" src="https://github.com/user-attachments/assets/14977cf5-e685-464f-9255-e8b14a4d219e" />
<img width="440" height="410" alt="Screenshot 2026-09-30 203440" src="https://github.com/user-attachments/assets/15666a2c-550e-4905-a82f-56746720193e" />


## Project files

- `hotel_management.py` — Python program (save the supplied source code under this filename).
- `README.md` — setup, usage, features, and manual testing guide.
- `statement.md` — project problem statement, scope, users, and high-level features.

## Current limitations

- Booking information is stored only in memory and is lost when the program exits.
- The interface is terminal-based and intended for a basic demonstration.
- Some inputs are converted directly to numbers, so invalid input may cause an error.
- The program does not fully enforce the room-specific occupancy values shown in the inventory.

## License

No license was specified with the supplied source code.

