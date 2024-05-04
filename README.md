# Parking Management System Repository

Welcome to our GitHub repository dedicated to the Parking Management System. This project is designed to facilitate efficient parking space management for a company operating various parking lots across a city. Our system handles different types of parking spaces, varying pricing zones, user types, and more.

## System Overview

This repository contains the source code and documentation for a comprehensive parking management database. The system is built to accommodate different vehicle types and parking preferences (outdoor, covered), and provides a dynamic pricing model based on the parking zone.

### Key Features

- **Multiple Parking Types:** Supports spaces for cars, motorcycles, and trucks.
- **Dynamic Pricing:** Prices vary by location such as downtown, industrial areas, and commercial zones.
- **User Types:** Handles both occasional users and subscribers, with different payment and access systems.
- **Loyalty Program:** Implements a loyalty system to reward frequent users and encourage new subscriptions.

### System Components

1. **Parking**
   - Each parking lot has an address, designated zone, and publicly displayed information about total and available spots.

2. **Zone**
   - Each zone has a unique name and associated pricing.

3. **Parking Space**
   - Identified by a number and attributes including location type (outdoor or covered) and designated vehicle type.

4. **Reservations**
   - Links a vehicle to a specific parking space with details on pricing and reservation duration.

5. **User Management**
   - Handles user information including name, subscription details, and vehicle data.

6. **Transactions**
   - Manages payment details, including method and processing location (online, kiosk, or booth).

7. **Tickets**
   - Issued for entry, with time-stamped details and vehicle information.

### Use Cases

- **Entry and Exit Management:** A vehicle arriving at the entry barrier is processed via license plate recognition. Subscribers or users with reservations are granted automatic entry.
- **Dynamic Availability Checks:** The system provides real-time updates on parking availability.
- **Subscription and Payment Handling:** Users can manage their subscriptions and make payments through various channels.

### Queries and Reports

- Retrieve current availability in any parking lot.
- Track usage frequency and average duration for any user.
- Verify participation in the loyalty program.
- Generate transaction reports with custom filters.

### System Constraints

- No entry if the parking lot is full.
- Unpaid tickets prevent exit.
- Subscriptions and reservations are vehicle-specific.

## Technologies Used

The project utilizes various technologies for backend management and frontend interfaces, ensuring robust data handling and user-friendly access.

## How to Navigate

This repository is organized into directories for each major component of the system. Detailed documentation for setup, deployment, and operation is available within each directory.

Thank you for visiting our repository. We believe this system offers a streamlined approach to parking management, enhancing user experience and operational efficiency.

